import mysql.connector
import json
import crud

def get_all_column_from_account():
    # with open('../core/dbInfo.json') as json_file:
    #     config = json.load(json_file)
    #     # config['raise_on_warnings'] = bool(config['raise_on_warnings'])
    #     print(config)
    #     cnx = mysql.connector.connect(**config)
    #     cursor = cnx.cursor()
    #     query = ("SELECT * FROM Account")
    #     cursor.execute(query)
    #     for column in cursor:
    #         print(column)
    # cnx.close()
    result = crud.read_default("*", "Account", "")
    return result

def get_excepted_columns_from_account(COLUMNS: str):
    # with open('../core/dbInfo.json') as json_file:
    #     config = json.load(json_file)
    #     # config['raise_on_warnings'] = bool(config['raise_on_warnings'])
    #     print(config)
    #     cnx = mysql.connector.connect(**config)
    #     cursor = cnx.cursor()
    #     sql = "SELECT " + COLUMNS + " FROM Account"
    #     query = (sql)
    #     cursor.execute(query)
    #     for column in cursor:
    #         print(column)
    # cnx.close()
    result = crud.read_default(COLUMNS, "Account", "")
    return result

a = get_all_column_from_account()
print(a)
b = get_excepted_columns_from_account("email")
print(b)