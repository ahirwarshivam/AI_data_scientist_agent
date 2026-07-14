# 🤖 AI Data Scientist Agent

> An LLM-powered autonomous Data Scientist that transforms raw datasets into actionable insights by automating data cleaning, exploratory data analysis (EDA), feature engineering, machine learning, visualization, and AI-generated reports.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📌 Overview

AI Data Scientist Agent is an intelligent application that automates the complete machine learning workflow using Large Language Models (LLMs) and traditional machine learning techniques.

Instead of manually performing every step of a data science project, users simply upload a dataset, and the agent automatically:

- Cleans the data
- Performs Exploratory Data Analysis (EDA)
- Engineers useful features
- Selects appropriate machine learning models
- Trains and evaluates models
- Generates interactive visualizations
- Produces AI-powered analytical reports

The project combines the reasoning capabilities of Large Language Models with the predictive power of traditional Machine Learning.

---

# 🎯 Problem Statement

Data analysis and machine learning involve multiple repetitive tasks including:

- Data cleaning
- Missing value handling
- Feature engineering
- Model selection
- Hyperparameter tuning
- Visualization
- Report generation

These tasks require significant manual effort and technical expertise.

The AI Data Scientist Agent automates this complete workflow, enabling users to obtain meaningful insights with minimal manual intervention.

---

# 🚀 Features

## 📂 Dataset Upload

- Upload CSV datasets
- Automatic dataset preview
- Dataset information
- Data type detection

---

## 🧹 Automated Data Cleaning

- Missing value detection
- Missing value imputation
- Duplicate removal
- Data type correction
- Outlier detection
- Null value visualization

---

## 📊 Exploratory Data Analysis

Automatically generates:

- Dataset Summary
- Statistical Description
- Correlation Matrix
- Heatmaps
- Histograms
- Boxplots
- Scatter Plots
- Distribution Analysis
- Class Distribution

---

## ⚙️ Feature Engineering

- Label Encoding
- One Hot Encoding
- Feature Scaling
- Standardization
- Normalization
- Feature Selection

---

## 🤖 Machine Learning

Automatically identifies problem type:

- Regression
- Classification

Supported Models

Regression

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Classification

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- KNN

---

## 📈 Model Evaluation

Regression Metrics

- MAE
- MSE
- RMSE
- R² Score

Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix

---

## 🎯 Hyperparameter Tuning

Supports

- Grid Search
- Random Search

---

## 📊 Interactive Visualizations

Interactive dashboards built using Plotly.

Includes

- Correlation Heatmap
- Missing Value Chart
- Feature Importance
- Confusion Matrix
- ROC Curve
- Model Comparison
- Distribution Plots

---

## 🧠 AI-Powered Insights

Using OpenAI APIs and LangChain, the application can:

- Explain dataset characteristics
- Interpret visualizations
- Recommend preprocessing steps
- Suggest appropriate ML algorithms
- Explain model performance
- Generate business insights
- Create analytical reports

---

## 📄 Automated Report Generation

Generate professional reports including:

- Dataset Summary
- Key Findings
- Feature Importance
- Model Performance
- Business Recommendations

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM

## Data Analysis

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib

## LLM Framework

- LangChain

## AI Model

- OpenAI GPT

## Web Framework

- Streamlit

---

# 🏗️ Project Architecture

```text
                   User
                     │
                     ▼
              Upload Dataset
                     │
                     ▼
             Data Validation
                     │
                     ▼
              Data Cleaning
                     │
                     ▼
                   EDA
                     │
                     ▼
          Feature Engineering
                     │
                     ▼
             Model Selection
                     │
                     ▼
             Model Training
                     │
                     ▼
           Hyperparameter Tuning
                     │
                     ▼
             Model Evaluation
                     │
                     ▼
            AI Report Generation
                     │
                     ▼
              Interactive Dashboard
```

---

# 📂 Project Structure

```text
AI-DataScientist-Agent/

│── app.py
│── requirements.txt
│── README.md
│
├── data/
│
├── models/
│
├── reports/
│
├── pages/
│   ├── Upload.py
│   ├── Cleaning.py
│   ├── EDA.py
│   ├── Modeling.py
│   ├── Prediction.py
│   └── Report.py
│
├── utils/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── model.py
│   └── llm.py
│
└── assets/
```

---

# Installation

Clone Repository

```bash
git clone https://github.com/yourusername/AI-DataScientist-Agent.git
```

Move into project

```bash
cd AI-DataScientist-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# Requirements

```
Python >=3.10

streamlit
pandas
numpy
plotly
matplotlib
scikit-learn
xgboost
lightgbm
langchain
openai
shap
```

---

# Workflow

1. Upload Dataset
2. Clean Data
3. Perform EDA
4. Feature Engineering
5. Select Model
6. Train Model
7. Evaluate Model
8. Generate AI Report
9. Download Results

---

# Demo

(Add screenshots or GIFs here)

Example

```
assets/dashboard.png

assets/report.png

assets/model.png
```

---

# Future Improvements

- AutoML Integration
- Multi-Agent Workflow
- Voice Assistant
- RAG-based Dataset Q&A
- MLflow Experiment Tracking
- Docker Support
- Cloud Deployment
- Hugging Face Integration
- Explainable AI Dashboard
- PDF Report Export

---

# Contribution

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

**Shivam Ahirwar**

GitHub: https://github.com/ahirwarshivam

LinkedIn: # 🤖 AI Data Scientist Agent

> An LLM-powered autonomous Data Scientist that transforms raw datasets into actionable insights by automating data cleaning, exploratory data analysis (EDA), feature engineering, machine learning, visualization, and AI-generated reports.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# Overview

AI Data Scientist Agent is an intelligent application that automates the complete machine learning workflow using Large Language Models (LLMs) and traditional machine learning techniques.

Instead of manually performing every step of a data science project, users simply upload a dataset, and the agent automatically:

- Cleans the data
- Performs Exploratory Data Analysis (EDA)
- Engineers useful features
- Selects appropriate machine learning models
- Trains and evaluates models
- Generates interactive visualizations
- Produces AI-powered analytical reports

The project combines the reasoning capabilities of Large Language Models with the predictive power of traditional Machine Learning.

---

# Problem Statement

Data analysis and machine learning involve multiple repetitive tasks including:

- Data cleaning
- Missing value handling
- Feature engineering
- Model selection
- Hyperparameter tuning
- Visualization
- Report generation

These tasks require significant manual effort and technical expertise.

The AI Data Scientist Agent automates this complete workflow, enabling users to obtain meaningful insights with minimal manual intervention.

---

# Features

## Dataset Upload

- Upload CSV datasets
- Automatic dataset preview
- Dataset information
- Data type detection

---

## Automated Data Cleaning

- Missing value detection
- Missing value imputation
- Duplicate removal
- Data type correction
- Outlier detection
- Null value visualization

---

## Exploratory Data Analysis

Automatically generates:

- Dataset Summary
- Statistical Description
- Correlation Matrix
- Heatmaps
- Histograms
- Boxplots
- Scatter Plots
- Distribution Analysis
- Class Distribution

---

## Feature Engineering

- Label Encoding
- One Hot Encoding
- Feature Scaling
- Standardization
- Normalization
- Feature Selection

---

## Machine Learning

Automatically identifies problem type:

- Regression
- Classification

Supported Models

Regression

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Classification

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- KNN

---

##  Model Evaluation

Regression Metrics

- MAE
- MSE
- RMSE
- R² Score

Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix

---

## Hyperparameter Tuning

Supports

- Grid Search
- Random Search

---

## Interactive Visualizations

Interactive dashboards built using Plotly.

Includes

- Correlation Heatmap
- Missing Value Chart
- Feature Importance
- Confusion Matrix
- ROC Curve
- Model Comparison
- Distribution Plots

---

## AI-Powered Insights

Using OpenAI APIs and LangChain, the application can:

- Explain dataset characteristics
- Interpret visualizations
- Recommend preprocessing steps
- Suggest appropriate ML algorithms
- Explain model performance
- Generate business insights
- Create analytical reports

---

## Automated Report Generation

Generate professional reports including:

- Dataset Summary
- Key Findings
- Feature Importance
- Model Performance
- Business Recommendations

---

# Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM

## Data Analysis

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib

## LLM Framework

- LangChain

## AI Model

- OpenAI GPT

## Web Framework

- Streamlit

---

# Project Architecture

```text
                   User
                     │
                     ▼
              Upload Dataset
                     │
                     ▼
             Data Validation
                     │
                     ▼
              Data Cleaning
                     │
                     ▼
                   EDA
                     │
                     ▼
          Feature Engineering
                     │
                     ▼
             Model Selection
                     │
                     ▼
             Model Training
                     │
                     ▼
           Hyperparameter Tuning
                     │
                     ▼
             Model Evaluation
                     │
                     ▼
            AI Report Generation
                     │
                     ▼
              Interactive Dashboard
```

---

# Project Structure

```text
AI-DataScientist-Agent/

│── app.py
│── requirements.txt
│── README.md
│
├── data/
│
├── models/
│
├── reports/
│
├── pages/
│   ├── Upload.py
│   ├── Cleaning.py
│   ├── EDA.py
│   ├── Modeling.py
│   ├── Prediction.py
│   └── Report.py
│
├── utils/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── model.py
│   └── llm.py
│
└── assets/
```

---

# Installation

Clone Repository

```bash
git clone https://github.com/yourusername/AI-DataScientist-Agent.git
```

Move into project

```bash
cd AI-DataScientist-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# Requirements

```
Python >=3.10

streamlit
pandas
numpy
plotly
matplotlib
scikit-learn
xgboost
lightgbm
langchain
openai
shap
```

---

# Workflow

1. Upload Dataset
2. Clean Data
3. Perform EDA
4. Feature Engineering
5. Select Model
6. Train Model
7. Evaluate Model
8. Generate AI Report
9. Download Results

---

# Demo

(Add screenshots or GIFs here)

Example

```
assets/dashboard.png

assets/report.png

assets/model.png
```

---

# Future Improvements

- AutoML Integration
- Multi-Agent Workflow
- Voice Assistant
- RAG-based Dataset Q&A
- MLflow Experiment Tracking
- Docker Support
- Cloud Deployment
- Hugging Face Integration
- Explainable AI Dashboard
- PDF Report Export

---

# Contribution

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

**Shivam Ahirwar**

Machine Learning | Generative AI | Data Science

GitHub: https://github.com/yourusername

LinkedIn: https://www.linkedin.com/in/shivam-ahirwar-425293311
