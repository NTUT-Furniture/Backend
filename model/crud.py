import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

pool_config = {
    "pool_name": "pool",
    "pool_size": 5,
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE")
}

cnx_pool = pooling.MySQLConnectionPool(**pool_config)

def read_default(COLUMNS: str, TABLES: str, CONDITION: str = ""):
    try:
        connection = cnx_pool.get_connection()
        cursor = connection.cursor()

        sql = f"SELECT {COLUMNS} FROM {TABLES}"
        if CONDITION:
            sql += f" WHERE {CONDITION}"
        cursor.execute(sql)
        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_default(TABLES: str, SET_VALUES: dict, CONDITION: str = ""):
    try:
        connection = cnx_pool.get_connection()
        cursor = connection.cursor()
        
        set_sql = ", ".join([f"{column} = %s" for column in SET_VALUES.keys()])
        sql = f"UPDATE {TABLES} SET {set_sql}"
        if CONDITION:
            sql += f" WHERE {CONDITION}"
        values = tuple(SET_VALUES.values())

        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
