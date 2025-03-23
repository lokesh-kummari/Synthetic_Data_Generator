# # import vertexai
# # from google.oauth2 import service_account
# # from vertexai.generative_models import GenerativeModel, Part, Content
# # import pandas as pd
# # import json
# # from sklearn.datasets import load_iris


# # PROJECT_ID = "inner-analyst-454416-s9"  # Your project ID
# # LOCATION = "us-central1"  # Your project location

# # credentials = service_account.Credentials.from_service_account_file("keys.json")
# # vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)


# # def identify_column_kind(profiling_report): # Takes profiling_report as input
# #     """Identifies column kinds using Gemini."""

# #     model = GenerativeModel("gemini-1.5-flash-002") # or "gemini-pro"
# #     predictions = []
# #     prompt = f"""
# #         You are a helpful AI assistant that analyzes data column characteristics. You have been given a dataset with the following column characteristics: {json.dumps(profiling_report)}
# #         Based on this information, determine the column's type (numeric, categorical, text, datetime, boolean, or other) and dentify which columns contain  sensitive data  . Sensitive data can include information that could identify an individual, such as   personal identification numbers  ,   contact information  ,   financial information  , or   health-related information  . Columns containing data such as   names  ,   email addresses  ,   phone numbers  ,   SSNs  ,   bank account numbers  , or   medical records   should be marked as sensitive (true/false). Return your answer as a JSON array of objects, where each object has the following format:
        
# #         ```json
# #           {{
# #             "column_name": "column_name",
# #             "type": "your_predicted_type",
# #             "sensitive": your_predicted_sensitivity // true or false
# #           }}
# #         ```
# #         """

# #     response = model.generate_content([Content(parts=[Part.from_text(prompt)], role="user")])

# #     return {"predictions":response.text}




# # # Load the DataFrame and create the profiling report
# # # data = load_iris()
# # # df = pd.DataFrame(data=data.data, columns=data.feature_names)
# # df= pd.read_csv('synthetic_dataset.csv')

# # def profile_data(df):
# #     profile = {}
# #     for column in df.columns:
# #         column_stats = {}
# #         column_stats['dtype'] = str(df[column].dtype)
# #         column_stats['unique_values'] = int(df[column].nunique())
# #         # Convert list of floats to a string representation before JSON serialization
# #         column_stats['sample_values'] = str(df[column].sample(10).tolist()) 
# #         profile[column] = column_stats
# #     return profile

# # profiling_report = profile_data(df)
# # print(profiling_report)

# # # Pass profiling_report to identify_column_kind
# # column_kinds = identify_column_kind(profiling_report)

# # json_string = column_kinds['predictions'].strip("```json\n")  # Remove backticks and newline
# # try:
# #     parsed_json = json.loads(json_string)
# #     print(parsed_json) # Now you have a usable JSON object
# #     # Access the data:
# #     for item in parsed_json:
# #         print(f"Column: {item['column_name']}, Type: {item['type']}, Sensitive: {item['sensitive']}")

# # except json.JSONDecodeError as e:
# #     print(f"Error decoding JSON: {e}")
# #     print(f"Original string that caused the error: {json_string}")
# # print(parsed_json)
# import vertexai
# from google.oauth2 import service_account
# from vertexai.generative_models import GenerativeModel, Part, Content
# import pandas as pd
# import json
# from sklearn.datasets import load_iris
# import numpy as np

# PROJECT_ID = "inner-analyst-454416-s9"  # Your project ID
# LOCATION = "us-central1"  # Your project location

# credentials = service_account.Credentials.from_service_account_file("keys.json")
# vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)


# def identify_column_kind(profiling_report):  # Takes profiling_report as input
#     """Identifies column kinds using Gemini."""
#     model = GenerativeModel("gemini-1.5-flash-002")  # or "gemini-pro"
#     predictions = []
#     prompt = f"""
#         You are a helpful AI assistant that analyzes data column characteristics. You have been given a dataset with the following column characteristics: {json.dumps(profiling_report)}
#         Based on this information, determine the column's type (numeric, categorical, text, datetime, boolean, or other) and identify which columns contain   sensitive data  . Sensitive data can include information that could identify an individual, such as   personal identification numbers  ,   contact information  ,   financial information  , or   health-related information  . Columns containing data such as   names  ,   email addresses  ,   phone numbers  ,   SSNs  ,   bank account numbers  , or   medical records   should be marked as sensitive (true/false). Return your answer as a JSON array of objects, where each object has the following format:
        
#         ```json
#           {{
#             "column_name": "column_name",
#             "type": "your_predicted_type",
#             "sensitive": your_predicted_sensitivity // true or false
#           }}
#         """
#     response = model.generate_content([Content(parts=[Part.from_text(prompt)], role="user")])
#     return {"predictions": response.text}


# # Load the DataFrame and create the profiling report
# df = pd.read_csv('sysn.csv')

# # Function to profile the dataset and compute statistics for different types
# def profile_data(df):
#     profile = {}
#     for column in df.columns:
#         column_stats = {}
#         column_stats['dtype'] = str(df[column].dtype)
#         column_stats['unique_values'] = int(df[column].nunique())
#         # Convert list of floats to a string representation before JSON serialization
#         column_stats['sample_values'] = str(df[column].sample(10).tolist())  # Get 10 sample values
        
#         profile[column] = column_stats
#     return profile

# # Generate the profiling report with basic statistics
# profiling_report = profile_data(df)
# print("Profiling Report:")
# print(json.dumps(profiling_report, indent=4))

# # Pass profiling_report to identify_column_kind
# column_kinds = identify_column_kind(profiling_report)

# # Clean up and parse the response
# json_string = column_kinds['predictions'].strip("```json\n")  # Remove backticks and newline
# try:
#     parsed_json = json.loads(json_string)
#     print("Parsed JSON: ", parsed_json)  # Now you have a usable JSON object

#     # Compute statistics for each column based on its type
#     for item in parsed_json:
#         column_name = item['column_name']
#         column_type = item['type']
#         column_stats = {}
        
#         # Numeric columns
#         if column_type == 'numeric':
#             column_stats['mean'] = df[column_name].mean()
#             column_stats['median'] = df[column_name].median()
#             column_stats['std_dev'] = df[column_name].std()
#             column_stats['range'] = (df[column_name].min(), df[column_name].max())
#             column_stats['skewness'] = df[column_name].skew()
#             column_stats['kurtosis'] = df[column_name].kurt()
        
#         # Categorical columns (nominal)
#         elif column_type == 'categorical':
#             column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
#             column_stats['mode'] = df[column_name].mode()[0]
#             column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()
        
#         # Ordinal columns
#         elif column_type == 'ordinal':
#             column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
#             column_stats['mode'] = df[column_name].mode()[0]
#             column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()
#             column_stats['median'] = df[column_name].median()
#             column_stats['cumulative_frequency'] = df[column_name].value_counts().sort_index().cumsum().to_dict()

#         # Nominal columns
#         elif column_type == 'nominal':
#             column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
#             column_stats['mode'] = df[column_name].mode()[0]
#             column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()

#         # Update parsed_json with the statistics
#         item.update(column_stats)

#     # Print the updated parsed_json with statistics
#     print("Updated Parsed JSON with Statistics:")
#     print(parsed_json)

# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {e}")
#     print(f"Original string that caused the error: {json_string}")

import vertexai
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel, Part, Content
import pandas as pd
import json
import numpy as np

PROJECT_ID = "inner-analyst-454416-s9"  # Your project ID
LOCATION = "us-central1"  # Your project location

credentials = service_account.Credentials.from_service_account_file("keys.json")
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)


def identify_column_kind(profiling_report):  # Takes profiling_report as input
    """Identifies column kinds using Gemini."""
    model = GenerativeModel("gemini-1.5-flash-002")  # or "gemini-pro"
    prompt = f"""
        You are a helpful AI assistant that analyzes data column characteristics. You have been given a dataset with the following column characteristics: {json.dumps(profiling_report)}
        Based on this information, determine the column's type (numeric, categorical, nominal,ordinal) and and identify which columns contain   sensitive data  . Sensitive data can include information that could identify an individual, such as   personal identification numbers  ,   contact information  ,   financial information  , or   health-related information  . Columns that should be marked as sensitive include   names  ,   email addresses  ,   phone numbers  ,   SSNs  ,   bank account numbers  ,   medical records, and other private, confidential, or identifying information like unique ids . sensitive data should be marked as sensitive (true/false). Return your answer as a JSON array of objects, where each object has the following format:
        
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

    # Send the prompt to Gemini and get the response
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


# Load the DataFrame and create the profiling report
df = pd.read_csv("uploads/sysn.csv")

# Function to profile the dataset and compute statistics for different types
def profile_data(df):
    profile = {}
    for column in df.columns:
        column_stats = {}
        column_stats['dtype'] = str(df[column].dtype)
        column_stats['unique_values'] = int(df[column].nunique())
        # Convert list of floats to a string representation before JSON serialization
        column_stats['sample_values'] = str(df[column].sample(10).tolist())  # Get 10 sample values
        
        profile[column] = column_stats
    return profile

# Generate the profiling report with basic statistics
profiling_report = profile_data(df)
print("Profiling Report:")
print(json.dumps(profiling_report, indent=4))

# Pass profiling_report to identify_column_kind
column_kinds = identify_column_kind(profiling_report)

# Clean up and parse the response
json_string = column_kinds['predictions'].strip("```json\n")  # Remove backticks and newline
try:
    parsed_json = json.loads(json_string)
    print("Parsed JSON: ", parsed_json)  # Now you have a usable JSON object

    # Mask sensitive data based on the 'sensitive' field in parsed_json
    for item in parsed_json:
        column_name = item['column_name']
        column_type = item['type']
        sensitive = item['sensitive']

        # Check if numeric column is sensitive and convert to nominal if true
        if column_type == 'numeric' and sensitive:
            item['type'] = 'nominal'  # Change type from numeric to nominal
            print(f"Column '{column_name}' is numeric and sensitive. Changing type to 'nominal'.")
        
        # Mask sensitive data
        if sensitive:  # If column is sensitive, apply Caesar Cipher
            df[column_name] = df[column_name].apply(lambda x: caesar_cipher_mask(str(x), shift=3))

    # Now perform the statistics calculation for each column based on its type
    for item in parsed_json:
        column_name = item['column_name']
        column_type = item['type']
        column_stats = {}

        # For numeric columns, check if the column is numeric before calculating stats
        if column_type == 'numeric' and pd.api.types.is_numeric_dtype(df[column_name]):  # Ensure column is numeric
            column_stats['mean'] = df[column_name].mean()
            column_stats['median'] = df[column_name].median()
            column_stats['std_dev'] = df[column_name].std()
            column_stats['range'] = (df[column_name].min(), df[column_name].max())
            column_stats['skewness'] = df[column_name].skew()
            column_stats['kurtosis'] = df[column_name].kurt()
        
        # For categorical columns (nominal), compute frequency count and mode
        elif column_type == 'categorical':
            column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
            column_stats['mode'] = df[column_name].mode()[0]
            column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()
        
        # For ordinal columns, calculate cumulative frequency and mode
        elif column_type == 'ordinal':
            column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
            column_stats['mode'] = df[column_name].mode()[0]
            column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()
            column_stats['median'] = df[column_name].median()
            column_stats['cumulative_frequency'] = df[column_name].value_counts().sort_index().cumsum().to_dict()

        # For nominal columns, calculate frequency count and mode
        elif column_type == 'nominal':
            column_stats['frequency_count'] = df[column_name].value_counts().to_dict()
            column_stats['mode'] = df[column_name].mode()[0]
            column_stats['proportion'] = df[column_name].value_counts(normalize=True).to_dict()

        # Update parsed_json with the statistics
        item.update(column_stats)

    # Print the updated parsed_json with statistics
    print("Updated Parsed JSON with Statistics:")
    print(parsed_json)

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    print(f"Original string that caused the error: {json_string}")
    
num_records = 20

# Generate synthetic data
synthetic_data = generate_synthetic_data(parsed_json, num_records)

# Print the synthetic data
print(synthetic_data)
