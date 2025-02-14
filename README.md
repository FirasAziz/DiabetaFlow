# DiabetaFlow: Automating Diabetes Data Processing with AI & Airflow

## Overview
DiabetaFlow is an automated data pipeline designed to process diabetes-related data efficiently. Leveraging Apache Airflow, Python, and MySQL, the pipeline performs ETL (Extract, Transform, Load) operations while integrating machine learning to predict diabetes risk.

This project was developed as part of the **Data Engineering and Analytics coursework at Hashemite University**.

## Features
- **Automated Data Extraction**: Fetches diabetes-related data from an external API.
- **Data Verification**: Ensures extracted data integrity using Airflow sensors.
- **Data Preprocessing**: Cleans and transforms data using Bash and Python scripts.
- **Database Storage**: Loads processed data into a MySQL database.
- **Machine Learning Integration**: Applies predictive models to assess diabetes risk.
- **End-to-End Orchestration**: Utilizes Apache Airflow to manage workflow execution.

## Pipeline Architecture
1. **Data Extraction**: Retrieves data from `http://87.236.232.200:5000/data` in batches of 1,000 records.
2. **Sensor Verification**: Confirms data integrity before proceeding.
3. **Data Transformation**: Cleans and formats data using a Bash script.
4. **Data Loading**: Stores processed data in a MySQL database.
5. **Machine Learning Model**: Predicts diabetes risk using a trained classifier.
6. **Pipeline Orchestration**: Manages execution using an Apache Airflow DAG.

## Technologies Used
- **Python** (Requests, Pandas, Scikit-learn, MySQL Connector, Airflow)
- **Bash Scripting** (jq for JSON processing)
- **MySQL** (Structured storage)
- **Apache Airflow** (Workflow orchestration)

## Installation
### Prerequisites
Ensure the following dependencies are installed:
- Python 3.8+
- Apache Airflow
- MySQL Server
- jq (for Bash JSON processing)

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DiabetaFlow.git
   cd DiabetaFlow
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure MySQL database**:
   - Create a database named `diabetes_db`.
   - Ensure MySQL credentials match those in the configuration file.

5. **Run Airflow DAG**:
   - Start Airflow services:
     ```bash
     airflow db init
     airflow webserver -p 8080 &
     airflow scheduler &
     ```
   - Access the Airflow UI at `http://localhost:8080` and trigger the DAG manually.

## Usage
- Modify `config.py` to set API endpoints and database credentials.
- Run the pipeline using Airflow to automate the data workflow.
- Monitor logs in Airflow to troubleshoot issues.

## Future Enhancements
- Implement real-time data streaming.
- Deploy the pipeline on cloud platforms (AWS, GCP, or Azure).
- Enhance model accuracy with deep learning techniques.


## Contact
For inquiries, reach out via [firasaziz20@gmail.com](mailto:firasaziz20@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/firas-aziz-50012a298).

