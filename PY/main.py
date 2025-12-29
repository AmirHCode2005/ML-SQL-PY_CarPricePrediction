import sys
import joblib
import pandas as pd

from PySide6.QtWidgets import QApplication

from GUI import CarPriceGUI
from db import get_data

# Load Tranied Model
model = joblib.load(r'C:\Users\madrid\Desktop\Python\ML_CarPricePrediction\ML\final_model.pkl')

# Get Car List From Database
quary = """
        SELECT DISTINCT CONCAT(brand , '_' , model) AS car_name
        FROM cars
        ORDER BY car_name
        """
car_df = get_data(quary)
car_list = car_df['car_name'].tolist()

# Prediction Function
def predict_function(car_name,year,mileage,gear,full):
    # Encode categorical values
    gear_values = 1 if gear == 'Auto' else 0
    full_values = 1 if full == 'Dual_Full' else 0
    
    # Prepare dataframe
    input_data = pd.DataFrame([{
        'year' : year,
        'mileage' : mileage,
        'gear_type' : gear_values,
        'full_type' : full_values,
        'car_name' : car_name
    }])
    
    # One-hot encode car_name
    input_data = pd.get_dummies(input_data)
    
    # Align with model features
    model_feature = model.feature_names_in_
    input_data = input_data.reindex(columns=model_feature,fill_value=0)
    
    # Predict
    price = model.predict(input_data)[0]
    return price

# Run Apllication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CarPriceGUI(
        car_list=car_list,
        predict_function=predict_function
    )
    window.show()
    sys.exit(app.exec())