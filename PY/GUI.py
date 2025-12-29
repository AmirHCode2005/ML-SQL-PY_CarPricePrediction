from PySide6.QtWidgets import (
    QWidget , QLabel , QComboBox,
    QLineEdit , QRadioButton , QPushButton,
    QVBoxLayout , QHBoxLayout , QButtonGroup,
    QMessageBox
)
from PySide6.QtCore import Qt

class CarPriceGUI(QWidget):
    def __init__(self,car_list,predict_function):
        super().__init__()
        
        self.predict_function = predict_function
        self.setWindowTitle('Car Price Predict')
        self.setMinimumWidth(420)
        
        # ===== Header =====
        self.header_lable = QLabel('Welcome To Car Price Predictor')
        self.header_lable.setAlignment(Qt.AlignCenter)
        
        # ===== Car Selector =====
        self.car_label = QLabel('Select Car')
        self.car_combo = QComboBox()
        self.car_combo.addItems(car_list)
        
        # ===== Inputs =====
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText('Production Year (e.g. 1399)')
        
        self.mileage_input = QLineEdit()
        self.mileage_input.setPlaceholderText('Mileage (KM)')
        
        # ===== Gea Type =====
        self.gear_lable = QLabel('Gear Type')
        self.manual_radio = QRadioButton('Manual')
        self.auto_radio = QRadioButton('Auto')
        self.manual_radio.setChecked(True)
        
        self.gear_grop = QButtonGroup(self)
        self.gear_grop.addButton(self.manual_radio)
        self.gear_grop.addButton(self.auto_radio)
        
        self.gear_layout = QHBoxLayout()
        self.gear_layout.addWidget(self.manual_radio)
        self.gear_layout.addWidget(self.auto_radio)
        
        # ===== Full Type =====
        self.full_lable = QLabel('Full Type')
        self.petrol_radio = QRadioButton('Petrol')
        self.dual_radio = QRadioButton('Dual_Full')
        self.petrol_radio.setChecked(True)
        
        self.full_grop = QButtonGroup(self)
        self.full_grop.addButton(self.petrol_radio)
        self.full_grop.addButton(self.dual_radio)
        
        self.full_layout = QHBoxLayout()
        self.full_layout.addWidget(self.petrol_radio)
        self.full_layout.addWidget(self.dual_radio)
        
        # ===== Button =====
        self.predict_button = QPushButton('Predict Price')
        self.predict_button.clicked.connect(self.handle_predict)
        
        # ===== Main Layout =====
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.header_lable)
        self.main_layout.addWidget(self.car_label)
        self.main_layout.addWidget(self.car_combo)
        self.main_layout.addWidget(QLabel('Year'))
        self.main_layout.addWidget(self.year_input)
        self.main_layout.addWidget(QLabel('Mileage'))
        self.main_layout.addWidget(self.mileage_input)
        self.main_layout.addWidget(self.gear_lable)
        self.main_layout.addLayout(self.gear_layout)
        self.main_layout.addWidget(self.full_lable)
        self.main_layout.addLayout(self.full_layout)
        self.main_layout.addWidget(self.predict_button)
        
        self.setLayout(self.main_layout)
        
        self.apply_styles()
        
    # ================= Style =================
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #e5e7eb;
                font-size: 14px;
            }
            QLabel {
                margin-top: 8px;
            }
            QPushButton {
                background-color: #38bdf8;
                color: #020617;
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0ea5e9;
            }
            QLineEdit, QComboBox {
                background-color: #020617;
                border: 1px solid #334155;
                padding: 6px;
                border-radius: 6px;
            }
        """)
    # ================ Handle Predict Button ===============
    def handle_predict(self):
        car_name = self.car_combo.currentText()
        year_text = self.year_input.text().strip()
        mileage_text = self.mileage_input.text().strip()
        gear = 'Manual' if self.manual_radio.isChecked() else 'Auto'
        full = 'Petrol' if self.petrol_radio.isChecked() else 'Dual_Full'
        
        if not year_text.isdigit():
            QMessageBox.warning(self,'Error','Year must be a Number')
            return
        
        if not mileage_text.isdigit():
            QMessageBox(self,'Error','Mileage must be a Number')
            return
        
        year = int(year_text)
        mileage = int(mileage_text)
        
        try:
            price = self.predict_function(
                car_name , year , mileage , gear , full
            )
            QMessageBox.information(self,'Prediction Result',f'Estimated Price\n {price*10:,.0f} Rial')
        except:
            QMessageBox.critical(self,'System Eror','Something went wrong while predicting the price')