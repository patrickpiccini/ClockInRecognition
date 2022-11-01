import psycopg2
import os

HOST_DATABSE = "localhost"

class ConnectionDatabase():

    def __init__(self):
        try:
            self.connection  = psycopg2.connect(
                host=HOST_DATABSE,
                port=7000,
                database="baseapplication",
                user="postgres",
                password="postgres")
            self.cursor = self.connection.cursor()
            # start tables
            self.create_tables()
            print('[✓] Connected to Postgres')
        except Exception as error:
            print(f'[X] CONNECTING POSTGRES ERROR: {error}')
    
    def create_tables(self):
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("[✓] You are connected to - ", record)

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                employee_id varchar(5) UNIQUE NOT NULL,
                fullname varchar(50) UNIQUE NOT NULL,
                password varchar(50) UNIQUE NOT NULL,
                age integer NOT NULL,
                photo text UNIQUE NOT NULL,
                created_at TIMESTAMP,
                updated_at TIMESTAMP,
                PRIMARY KEY (employee_id)
            );
            CREATE TABLE IF NOT EXISTS clockin (
                clockin_id SERIAL UNIQUE NOT NULL,
                employee_id varchar(5) NOT NULL,
                item_description varchar(256) NOT NULL,
                fullname varchar(50) NOT NULL,
                date TIMESTAMP,
                hour TIMESTAMP,
                PRIMARY KEY (clockin_id),
                FOREIGN KEY(employee_id) REFERENCES users(employee_id)
            );
            '''
        
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print('[✓] Created tables on DataBase')