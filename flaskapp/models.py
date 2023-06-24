import os
from dotenv import load_dotenv
import mysql.connector

def connect():
    load_dotenv()
    conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv('PASSWORD'),
        database=os.getenv("DB")
    )

    return conn