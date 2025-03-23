# 🔐 **Synthetic Dataset Generator** 


### AI-based Synthetic Dataset Generator

**Use Case**:  
Build a platform that generates synthetic but realistic datasets for machine learning model training while maintaining privacy. This is particularly helpful for industries or sectors that face challenges in obtaining large datasets due to privacy concerns. The platform ensures that the synthetic datasets maintain statistical properties of the original data, while protecting sensitive information and providing valuable data for model training.

This tool is designed to bridge the gap between privacy constraints and the need for large, high-quality datasets in fields like healthcare, finance, and more.

---

## ⚠️ **Important Note**

This application is designed to generate **synthetic datasets** while maintaining **privacy**. We ensure the generated datasets preserve the statistical properties of the original data while masking any **sensitive information** such as names, phone numbers, and unique identifiers.

Please go through the code and description of the **synthetic data generation process** in this repository: [GitHub Repository](https://github.com/lokesh-kummari/Synthetic_Data_Generator)

## 🌟 **Brief**

In today’s world, **data privacy** is a key concern, especially when working with sensitive data. Our AI-driven solution generates **synthetic datasets** that preserve **privacy** and **statistical consistency**. By analyzing the original dataset's statistical characteristics, we use LLM's to  generate synthetic data that mimics the original dataset without exposing sensitive information. 

This solution provides a **secure**, **privacy-preserving** alternative for working with datasets, ensuring that **data-driven decisions** can still be made without compromising **user privacy**. 

## 🛠️ **Technology Stack**

| **Frontend**   | **Backend**   | **ML Library**   | **LLMs**        | **Database**   | **Deployment**  | **Version Control** |
|----------------|---------------|------------------|-----------------|----------------|-----------------|---------------------|
| 🌐 **HTML5**   | 🐍 **FastAPI** | 📊 **Scikit-Learn** | 🤖 **Gemini 1.5 Pro** | -              | 🌐 **Render**          | 🐙 **GitHub**       |
| 🎨 **CSS3**    | 🖥️ **Python (Flask)** | 📈 **Pandas, Numpy** | -               | -              | 🧑‍💻 **Render**  | 🔧 **GitHub**       |
| 💻 **JavaScript** |               |                  |                 |                |                 |                     |

## 🔑 **Key Features**

- **🔒 Privacy-Preserving Data Generation**: Generate synthetic data while maintaining **privacy**.
- **📊 Statistical Consistency**: Ensure that generated datasets preserve key **statistical properties** of the original data.
- **🔐 Sensitive Data Masking**: Mask sensitive information like **names**, **phone numbers**, and **unique identifiers** using techniques like **Caesar Cipher**.
- **🛡️ Data Security**: Generate **secure**, privacy-preserving synthetic datasets suitable for testing and training **machine learning models**.

---

For more information on how to use this application, please refer to the detailed instructions in the repository.

## 🚀 Process Flow

The **Synthetic Dataset Generator** follows a well-structured process to generate synthetic datasets for machine learning, ensuring privacy at every step. Below is a detailed overview of how the platform works:

### 1. **Upload a CSV File**
   - **What Happens**: The first step is uploading your original dataset in CSV format. This is done through the user interface where you are prompted to select the file from your system. Once the file is selected, the system will verify that the file is a CSV file and save it for further processing.
   - **Why It's Important**: The uploaded dataset serves as the basis for generating synthetic data. The system needs to analyze your data in order to generate new data that closely resembles the original dataset while maintaining its statistical properties.

### 2. **Data Categorization**
   - **What Happens**: After the file is uploaded, the system will examine the dataset to categorize the columns. It identifies the type of each column (e.g., Numeric, Categorical, Nominal, or Ordinal). For example, numeric columns may contain integers or floats, categorical columns may contain predefined categories (like "Male" or "Female"), and ordinal columns may represent ranked data.
   - **Why It's Important**: Categorizing the columns is essential because different types of data require different methods of handling during the data generation process. For instance, numeric columns are handled differently than categorical columns when generating synthetic data, so proper categorization ensures accurate results.

### 3. **Sensitive Data Masking**
   - **What Happens**: The system scans through your dataset to detect sensitive information such as personal identifiers (names, phone numbers, emails, etc.). If any such sensitive data is found, it is automatically masked to prevent privacy breaches. For example, a name might be encrypted, or a phone number might be altered using an encoding technique.
   - **Why It's Important**: Masking sensitive data ensures that no private or personally identifiable information is exposed in the generated synthetic dataset. It is a key step for maintaining privacy and adhering to data protection regulations (such as GDPR or HIPAA), ensuring that the synthetic data is safe to use.

### 4. **Synthetic Data Generation**
   - **What Happens**: Once the dataset has been categorized and sensitive information is masked, the system proceeds to generate synthetic data. The synthetic data is created by preserving the statistical properties of the original dataset (e.g., mean, standard deviation, and correlations between columns). This is done by using advanced machine learning models that understand the distribution of the original data and create new data points that follow the same distribution.
   - **Why It's Important**: Synthetic data generation allows for the creation of new datasets that mimic the characteristics of the original data. This is particularly useful when the original data is too sensitive to share or use directly, but synthetic data can serve as a good substitute for training machine learning models or performing analysis without violating privacy concerns.

### 5. **Download Synthetic Data (CSV Format)**
   - **What Happens**: After the synthetic data is generated, the platform provides an option to download the generated dataset in CSV format. A download button is made available on the user interface, allowing users to save the newly generated data to their local system.
   - **Why It's Important**: The ability to download the synthetic data is the final step in the process. After the synthetic data has been generated, users can use it in their machine learning projects or any other data-related tasks. This downloadable CSV file allows users to easily integrate the synthetic dataset into their workflow.

### 6. **Optional Decryption (For Authorized Users)**
   - **What Happens**: In case sensitive data was masked during the process, authorized users have the option to decrypt the sensitive information. This step can be performed through a secure decryption portal if users have the necessary permissions to access the original data.
   - **Why It's Important**: This optional step ensures that if authorized personnel need access to the original sensitive data, they can decrypt it securely. It offers flexibility for scenarios where the original data might be required for analysis or other purposes, but still ensures data security during the data generation process.

---


## 💡 **Example Workflow**

## 🔒 **How It Works**

1. **Upload**: Upload a CSV file containing the original data.
2. **Analyze**: The application categorizes columns and determines privacy-sensitive data.
3. **Data masking** is also performed on sensitive columns.
4. **Generate**: Synthetic data is generated based on statistical properties while ensuring privacy. 
5. **Download**: Download the synthetic data for further use in machine learning models.


---

## 🛡️**How Will It Be Able to Solve the Problem?**

### 🔒**Optimized Data Generation:**
The **Synthetic Dataset Generator** optimizes data generation by using statistical methods to generate synthetic data that closely mimics the **original dataset**. This allows organizations to perform analyses, develop models, and conduct research while ensuring **data privacy**. Our system maintains the **mean**, **standard deviation**, and other key characteristics of the original dataset, ensuring the synthetic data is statistically accurate while removing sensitive information such as personal details, financial records, and more.

### 📅 **Improved Data Utilization:**
By generating **synthetic datasets**, users can proceed with machine learning experiments without worrying about data privacy. The synthetic data retains the same **statistical patterns** and relationships found in the original dataset, enabling users to train their models effectively. This approach facilitates improved use of data for **research, analysis, and model training** while adhering to privacy guidelines and regulations.

### ⚠️ **Privacy Protection:**
The synthetic data generation process ensures that **sensitive data** is masked through various encryption techniques. This protects individuals' privacy and ensures that the generated datasets do not expose any personally identifiable information (PII). Our system is designed to prevent data misuse and help organizations comply with privacy regulations such as **GDPR** and **CCPA**, making it a **compliant and secure solution** for generating data.

### 🔄 **Increased Flexibility:**
By using our solution, organizations can generate **synthetic datasets** that can be used for multiple purposes, including training, testing, and validation. These datasets can be customized according to specific requirements, providing flexibility and enabling organizations to explore different scenarios and applications without the need for **sensitive data**.

---

## 🌟 **Unique Selling Points (USP) of the Solution**

### 🔄 **Continuous Privacy Support:**
Our **AI-driven solution** continuously offers **privacy-preserving synthetic data** by generating datasets that mimic the statistical properties of original data without exposing sensitive information. This ongoing support ensures that businesses and researchers can access **privacy-safe data** for analysis, training, and development without concerns about privacy violations.

### 🌍 **Sustainability:**
By ensuring that sensitive data is never exposed, our solution promotes **data privacy sustainability**. This protects both individuals' personal data and the organizations' compliance with data protection laws, fostering trust and responsible data usage.

### 📈 **Increased Resilience in Data Analysis:**
Our platform increases resilience by providing synthetic datasets that mimic real-world data while maintaining privacy. This enables users to continue their work on real-world projects, validate models, and perform testing without worrying about data breaches. The ability to generate privacy-safe synthetic data adds robustness to the data handling process.

### 💰 **Cost-Effective Solution:**
Organizations can save costs associated with acquiring and managing sensitive data. By using synthetic data, businesses and research organizations can conduct analyses, build machine learning models, and optimize algorithms without the financial burden of securing sensitive real-world datasets. This **cost-effective solution** makes data access and research more affordable and scalable.

---

## 🎥 Project Video Demonstration

Here is a demonstration video of the project:



https://github.com/user-attachments/assets/a830bd38-1481-4ebf-9219-324cfb06f444



## Conclusion

The **Synthetic Data Generator** is a powerful tool designed to help users generate realistic synthetic datasets while ensuring that sensitive information is effectively masked. By leveraging advanced machine learning techniques and generative models, this solution not only enhances privacy but also ensures that the generated data maintains statistical consistency with the original dataset. With a user-friendly interface and automated data categorization and masking, the tool allows users to seamlessly generate privacy-preserving synthetic data, making it ideal for machine learning model training and data analysis purposes. This project promotes a balance between data utility and privacy, empowering users to make informed decisions based on synthetic data without compromising sensitive information.




🔗 **Related Links**:
- [GitHub Repository](https://github.com/lokesh-kummari/Synthetic_Data_Generator)
- [Documentation](https://link-to-your-docs.com)
