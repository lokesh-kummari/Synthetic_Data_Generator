# Synthetic Dataset Generator


**Synthetic Dataset Generator** is a platform that allows you to generate synthetic datasets for machine learning model training while ensuring privacy. The tool analyzes the uploaded dataset, categorizes the data, applies necessary masking techniques for sensitive information, and generates synthetic data with preserved statistical properties.

This project is not about traditional dataset generation but focuses on **generating data with privacy**. This ensures that sensitive information (such as names, contact details, or IDs) is masked while still maintaining the overall structure and statistical consistency of the data.

## Features

- **Data Categorization**: Automatically categorizes the data into numeric, categorical, ordinal, and nominal types.
- **Sensitive Data Masking**: Ensures privacy by applying encryption techniques (e.g., Caesar Cipher) to sensitive columns such as names, email addresses, phone numbers, and unique identifiers.
- **Synthetic Data Generation**: Based on the statistical characteristics of the data (e.g., mean, skewness, kurtosis, and proportions), synthetic data is generated.
- **Privacy Preserved**: The generated synthetic data maintains the same distribution while masking sensitive information.

## Technology Stack

| Technology   | Description                                                             | Logo                                                              |
|--------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Python**   | Core language used for backend development                              | ![Python](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg) |
| **Flask**    | Web framework for building the web application                          | ![Flask](https://upload.wikimedia.org/wikipedia/commons/9/99/Flask_logo.svg) |
| **Jupyter**  | Interactive notebooks for generating and testing synthetic data models  | ![Jupyter](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Jupyter_logo.svg/1280px-Jupyter_logo.svg.png) |
| **Vertex AI**| Google Cloud AI for dataset analysis and predictions                    | No Logo (Google Cloud)                                            |
| **Pandas**   | Data manipulation and analysis library                                  | No Logo (Pandas)                                                   |
| **HTML/CSS/JS**| Frontend technologies for rendering the user interface               | No Logo (Standard web technologies)                               |

## How It Works

1. **Upload Dataset**: The user uploads a CSV dataset through the web interface.
2. **Analyze Columns**: The tool analyzes the dataset and classifies each column (numeric, categorical, ordinal, nominal). It also detects sensitive data.
3. **Mask Sensitive Data**: Sensitive information is masked using encryption techniques (e.g., Caesar Cipher).
4. **Generate Synthetic Data**: Synthetic data is generated based on the statistical properties of the original dataset, ensuring the privacy of sensitive data.
5. **Download Generated Data**: The synthetic data is presented to the user, ready for use in training machine learning models.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Synthetic_Data_Generator.git
