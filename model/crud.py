import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_DATABASE")

    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

def read_default(COLUMNS: str, TABLES: str, CONDITION: str):
    try:
        with get_db_connection() as cnx:
            cursor = cnx.cursor()

            sql = f"SELECT {COLUMNS} FROM {TABLES}"
            if CONDITION:
                sql += f" WHERE {CONDITION}"

            cursor.execute(sql)
            result = cursor.fetchall()
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