import mysql.connector
import json

def get_db_connection():
    with open('../core/dbInfo.json') as json_file:
        config = json.load(json_file)
        return mysql.connector.connect(**config)

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