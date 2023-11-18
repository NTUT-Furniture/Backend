import mysql.connector
import json

def read_default(COLUMNS: str, TABLES: str, CONDITION: str):
    try:
        with open('../core/dbInfo.json') as json_file:
            config = json.load(json_file)
            # config['raise_on_warnings'] = bool(config['raise_on_warnings'])
            # print(config)
            with mysql.connector.connect(**config) as cnx:
                cursor = cnx.cursor()
                # cursor.execute(f"SHOW COLUMNS FROM {TABLES}")

                sql = f"SELECT {COLUMNS} FROM {TABLES}"
                if CONDITION:
                    print(CONDITION)
                    sql += f" WHERE {CONDITION}"
                print(sql)
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
#     print (row)