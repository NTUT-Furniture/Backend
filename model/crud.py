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

def read_default(COLUMNS: str, TABLES: str, CONDITION: str):
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

# Example usage:
# columns = "*"
# tables = "Account"
# condition = ""
# result = read_default("email, credit_card", "Account", "")
# for row in result:
#     print(row)
# result = read_default(columns, tables, condition)
# print(result)
# for row in result:
#     print(row)