import mysql.connector
import pandas as pd

def create_connection():
    conn = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'amir1234',
        database = 'car_price'
    )
    return conn

def get_data(query):
    conn = create_connection()
    data = pd.read_sql(query,conn)
    conn.close()
    return data

# For Example
# if __name__ == '__main__':
#     cars_data = get_data('SELECT * FROM cars')
#     print(cars_data.head())