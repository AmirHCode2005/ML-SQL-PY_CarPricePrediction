# 🚗 Car Price Prediction Using Machine Learning  

## 📘 Overview
This project is an **end-to-end Machine Learning system** for predicting **car prices** based on technical and usage features.  
It covers the complete ML pipeline — from data preprocessing and model selection to hyperparameter tuning and a functional **GUI application**.

The task is a **Regression problem**, aiming to predict a **continuous numeric value (car price)**.

## 🧠 Project Highlights
- **Problem Type:** Regression  
- **Language:** Python 🐍  
- **Libraries:**  
  - Pandas, NumPy  
  - Scikit-learn  
  - PyQt (GUI)  

- **Models Implemented:**  
  - Linear Regression  
  - Ridge & Lasso  
  - ElasticNet  
  - KNN  
  - Decision Tree  
  - Gradient Boosting (Ensemble)

## ⚙️ Workflow

### 🔹 Data Preparation
- Cleaning and preprocessing raw car data  
- Encoding categorical features (car name, gear type, fuel type)  
- Feature scaling using **StandardScaler**

### 🔹 Model Evaluation
- Spot-checking multiple baseline models  
- Comparing performance using **R²** and **MAE**  
- Selecting the best-performing models for tuning

### 🔹 Hyperparameter Tuning
- GridSearchCV applied to:
  - **ElasticNet**
  - **Gradient Boosting Regressor**
- Improving model stability and generalization

### 🔹 Final Model
- **ElasticNet** selected as the final prediction model  
- Integrated into a **GUI application** for real-time price prediction

## 🖥️ GUI Application
The graphical interface allows users to:
- Select car brand & model from a dropdown  
- Enter:
  - Production year  
  - Mileage  
  - Gear type (Manual / Auto)  
  - Fuel type  
- Click **Predict** to receive an estimated price  
- Input validation and error handling via MessageBox

## 📊 Evaluation Metrics
- **R² Score** – explains model variance  
- **MAE (Mean Absolute Error)** – average prediction error in price units  

⚠️ Prediction accuracy improves for higher price ranges, while lower-priced cars may have larger relative errors.

## 📬 Contact
📧 Email: amirhossin6825@gmail.com  
💬 Telegram: [@AmirHossin6825](https://t.me/AmirHossin6825)
