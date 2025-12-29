import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'amir1234', # Your PassWord
    database = 'car_price'
)
cur = conn.cursor()
# The CSV file created here is only for uploading to GitHub,
# the original CSV file is in the following path:
df = pd.read_csv(r'C:\Program Files\MySQL\MySQL Server 8.0\Uploads\cars_data.csv')

for _ , row in df.iterrows():
    cur.execute("""
                INSERT INTO cars
                (brand,model,year,mileage,gear_type,full_type,price)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
                """,tuple(row))
conn.commit()
conn.close()