# Heart Disease Classification Project

## 📖 Overview

This project is designed to classify whether a patient has heart disease based on various medical attributes. It uses a machine learning model trained on a dataset containing features such as age, sex, chest pain type, cholesterol levels, and more. The project includes a PostgreSQL database for storing data, a Python-based migration system, and a Dockerized environment for easy deployment.

---

## 🚀 Features

- **Data Storage**: Uses PostgreSQL to store patient data and migration history.
- **Migrations**: SQL-based migrations to manage database schema changes.
- **Dockerized Environment**: Easy setup and deployment using Docker and Docker Compose.
- **Machine Learning**: A trained model to predict heart disease based on patient data.
- **Scalable Architecture**: Designed to handle large datasets and future enhancements.

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Migration Tooling**: Custom Python scripts for SQL migrations
- **Environment Management**: `.env` files for configuration

---

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed.
- Python 3.8+ installed.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/heart-disease-classification.git
   cd heart-disease-classification

Set Up Environment Variables:
Create a .env file in the root directory with the following content:

   ```bash
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=your_database_name
   ... Rest of the configuration
   ```

Build and Run the Docker Container:

```bash
docker-compose up --build
```

### Configure Minio:
Go to localhost:9000 and create the access key and secret key. Paste it into your .env and re-run the docker-compose up --build command.

### Apply Database Migrations:
Run the migration script to set up the database schema and insert sample data:

```bash
python -m scripts.run_migrations
```

## 🧩 Functionalities
1. Database Management
Schema Creation: SQL migrations to create and update the database schema.

Sample Data Insertion: Predefined SQL scripts to insert sample data for testing.

2. Machine Learning
Model Training: Train a machine learning model using Scikit-learn.

Prediction: Use the trained model to predict heart disease based on patient data.

3. Dockerized Environment
Easy Setup: Run the entire project (database, migrations, and scripts) using Docker Compose.

Portability: Deploy the project anywhere Docker is supported.

## 📊 Dataset
The dataset used in this project contains the following features:

| Column Name | Description                                |
|-------------|--------------------------------------------|
| `age`       | Age of the patient                         |
| `sex`       | Gender of the patient (0 = female, 1 = male) |
| `cp`        | Chest pain type (0-3)                      |
| `trestbps`  | Resting blood pressure (mm Hg)             |
| `chol`      | Serum cholesterol (mg/dl)                  |
| `fbs`       | Fasting blood sugar > 120 mg/dl (0 = false, 1 = true) |
| `restecg`   | Resting electrocardiographic results (0-2) |
| `thalach`   | Maximum heart rate achieved                |
| `exang`     | Exercise-induced angina (0 = no, 1 = yes)  |
| `oldpeak`   | ST depression induced by exercise          |
| `slope`     | Slope of the peak exercise ST segment      |
| `ca`        | Number of major vessels colored by fluoroscopy |
| `thal`      | Thalassemia (0-3)                          |
| `target`    | Target variable (0 = no disease, 1 = disease) |