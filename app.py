import os
from flask import Flask, render_template, request
import pandas as pd
import json
from dotenv import load_dotenv
import vertexai
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel, Part, Content
import numpy as np
import os
import json
import tempfile
load_dotenv() 
# Initialize Flask app
app = Flask(__name__)

# Configure the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory where files will be saved
app.config['ALLOWED_EXTENSIONS'] = {'csv'}  # Allowed file extensions

# # Vertex AI setup
# PROJECT_ID = os.getenv("PROJECT_ID")  # Load project ID from .env
# LOCATION = os.getenv("LOCATION")  # Load location from .env
# credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
# vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

# Load the environment variable that contains the JSON credentials
credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

if credentials_json:
    try:
        credentials = json.loads(credentials_json)
        print("Google application credentials loaded successfully.")

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix="-google-credentials.json")
        with open(temp_file.name, "w") as f:
            json.dump(credentials, f)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_file.name
        print(f"Google application credentials set to temporary file: {temp_file.name}")

        try:
            credentials = service_account.Credentials.from_service_account_file(temp_file.name)
            vertexai.init(
                project=os.getenv('PROJECT_ID'),
                location=os.getenv('LOCATION'),
                credentials=credentials
            )
            print("Vertex AI initialized successfully.")
            # Keep temp_file open until after vertexai.init()
        except Exception as e:
            print(f"Failed to initialize Vertex AI: {e}")
            exit(1)
        finally:
            # Ensure the file is deleted even if exceptions occur
            os.remove(temp_file.name)

    except json.JSONDecodeError as e:
        print(f"Error decoding the JSON credentials: {e}")
        exit(1)
else:
    print("Environment variable GOOGLE_APPLICATION_CREDENTIALS_JSON is not set.")
    exit(1)


# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Helper function to convert non-serializable types to native Python types
def convert_to_native_types(data):
    if isinstance(data, dict):
        return {key: convert_to_native_types(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_native_types(item) for item in data]
    elif isinstance(data, pd.Timestamp):
        return str(data)  # Convert pandas Timestamp to string
    elif isinstance(data, (np.int64, np.float64)):
        return data.item()  # Convert numpy types to Python native types
    return data

def identify_column_kind(profiling_report):  # Takes profiling_report as input
    """Identifies column kinds using Gemini."""
    model = GenerativeModel("gemini-1.5-flash-002")  # or "gemini-pro"
    prompt = f"""
        You are a helpful AI assistant that analyzes data column characteristics. You have been given a dataset with the following column characteristics: {json.dumps(profiling_report)}
        Based on this information, determine the column's type (numeric, categorical, nominal, ordinal) and identify which columns contain sensitive data. Sensitive data can include information that could identify an individual, such as personal identification numbers, contact information, financial information, or health-related information. Columns that should be marked as sensitive include names, email addresses, phone numbers, SSNs, bank account numbers, medical records, and other private, confidential, or identifying information like unique ids. Sensitive data should be marked as sensitive (true/false). Return your answer as a JSON array of objects, where each object has the following format:
        ```json
          {{
            "column_name": "column_name",
            "type": "your_predicted_type",
            "sensitive": your_predicted_sensitivity // true or false
          }}
        """
    response = model.generate_content([Content(parts=[Part.from_text(prompt)], role="user")])
    return {"predictions": response.text}

def generate_synthetic_data(x, num_records):  # Takes profiling_report (x) and number of records as input
    """Generates synthetic data using LLM (Gemini) while maintaining provided statistics."""
    model = GenerativeModel("gemini-1.5-flash-002")  
    # Construct the prompt dynamically based on the profiling report (x)
    prompt = f"""
    You are a helpful AI assistant that generates synthetic data while ensuring the generated data maintains the original statistical properties provided. 
    You have been given a dataset with the following column characteristics: {x}.
    
    Please generate synthetic data for the following columns, respecting the statistics for each column:
    
    - For **numeric columns**, ensure the **mean**, **standard deviation**, **skewness**, and **kurtosis** match the provided values.
    - For **categorical columns**, generate data that follows the **frequency count** and **proportion** for each category.
    - For **ordinal columns**, respect the **frequency count**, **mode**, and **proportions** for the ordinal values.
    - For **sensitive columns**, such as **names**, **SSNs**, **email addresses**, **phone numbers**, **Unique IDs**, ensure the data is **masked or transformed** to preserve privacy.
    
    Generate exactly {num_records} records and return only the synthetic data in **CSV format** with the following structure and The synthetic data should respect the original distribution and characteristics (e.g., mean, proportions) for each column type. only provide csv no other content:
    ```
    column1_name,column2_name,...,columnN_name
    value1,value2,...,valueN
    value1,value2,...,valueN
    ```
    """
    response = model.generate_content([Content(parts=[Part.from_text(prompt)], role="user")])
    
    # Return the response (synthetic data in CSV format)
    return response.text

# Caesar Cipher for masking sensitive data
def caesar_cipher_mask(text, shift=3):
    """
    Applies a Caesar Cipher to mask the input text.
    """
    masked_text = ''.join([chr(((ord(char) + shift - 32) % 95) + 32) if char.isprintable() else char for char in text])
    return masked_text


# # Load the DataFrame and create the profiling report
# df = pd.read_csv("uploads/sysn.csv")

# Function to profile the dataset and compute statistics for different types
def profile_data(df):
    profile = {}
    for column in df.columns:
        column_stats = {}
        column_stats['dtype'] = str(df[column].dtype)
        column_stats['unique_values'] = int(df[column].nunique())
        column_stats['sample_values'] = str(df[column].sample(10).tolist())  # Get 10 sample values
        
        profile[column] = column_stats
    return profile

# In your home route, convert the necessary data before passing to the template
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the number of records from the user input
        num_records = int(request.form['num_records'])
        
        # Check if a file was uploaded
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        
        # If there is no file or the file name is empty, return an error
        if file.filename == '':
            return 'No selected file'
        
        # If the file has an allowed extension, save it
        if file and allowed_file(file.filename):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Load the DataFrame and create the profiling report
            df = pd.read_csv(file_path)
            profiling_report = profile_data(df)
            
            # Pass profiling_report to identify_column_kind
            column_kinds = identify_column_kind(profiling_report)

            # Clean up and parse the response
            json_string = column_kinds['predictions'].strip("```json\n")  # Remove backticks and newline
            try:
                parsed_json = json.loads(json_string)
                
                # Mask sensitive data based on the 'sensitive' field in parsed_json
                masked_data = {}
                for item in parsed_json:
                    column_name = item['column_name']
                    column_type = item['type']
                    sensitive = item['sensitive']

                    # If numeric column is sensitive, change type to nominal
                    if column_type == 'numeric' and sensitive:
                        item['type'] = 'nominal'  # Change type from numeric to nominal
                    
                    if sensitive:
                        # Mask sensitive data using Caesar Cipher
                        df[column_name] = df[column_name].apply(lambda x: caesar_cipher_mask(str(x), shift=3))
                        masked_data[column_name] = df[column_name].head(1).to_list()  # Display first row for masking

                # Generate synthetic data
                synthetic_data = generate_synthetic_data(parsed_json, num_records)

                # Prepare column statistics for display
                column_stats = {}
                for item in parsed_json:
                    column_name = item['column_name']
                    column_stats[column_name] = {
                        'type': item['type'],
                        'sensitive': item['sensitive'],
                        'sample_values': str(df[column_name].head(5).to_list())  # Sample values from the column
                    }
                    # Calculating the statistics for each column type
                    if item['type'] == 'numeric':
                        column_stats[column_name].update({
                            'mean': df[column_name].mean(),
                            'median': df[column_name].median(),
                            'std_dev': df[column_name].std(),
                            'range': (df[column_name].min(), df[column_name].max())
                        })
                    elif item['type'] == 'categorical':
                        column_stats[column_name].update({
                            'mode': df[column_name].mode()[0],
                            'frequency_count': df[column_name].value_counts().to_dict()
                        })
                    elif item['type'] == 'ordinal':
                        column_stats[column_name].update({
                            'mode': df[column_name].mode()[0],
                            'frequency_count': df[column_name].value_counts().to_dict()
                        })
                    elif item['type'] == 'nominal':
                        column_stats[column_name].update({
                            'mode': df[column_name].mode()[0],
                            'frequency_count': df[column_name].value_counts().to_dict()
                        })

                # Convert all non-serializable types to native Python types
                parsed_json = convert_to_native_types(parsed_json)
                column_stats = convert_to_native_types(column_stats)
                masked_data = convert_to_native_types(masked_data)

                return render_template('index.html', 
                                       synthetic_data=synthetic_data.strip("```csv\n"), 
                                       parsed_json=parsed_json, 
                                       column_stats=column_stats,
                                       masked_data=masked_data)

            except json.JSONDecodeError as e:
                return f"Error decoding JSON: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 8000)))