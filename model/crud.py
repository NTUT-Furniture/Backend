import mysql.connector
import json

def read_default(COLUMNS: str, TABLES: str, CONDITION: str):
    with open('../core/dbInfo.json') as json_file:
        config = json.load(json_file)
        # config['raise_on_warnings'] = bool(config['raise_on_warnings'])
        print(config)
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        sql = "SELECT " + COLUMNS + " FROM " + TABLES
        if CONDITION:
        	sql += " WHERE " + CONDITION
        query = (sql)
        cursor.execute(query)
        for column in cursor:
            print(column)
    cnx.close()

read_default("email, credit_card", "Account", "")