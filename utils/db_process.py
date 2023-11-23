import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv
from typing import Union, Tuple, Dict, List
from typing import Final
import datetime
load_dotenv()

pool_config = {
    "pool_name": "pool",
    "pool_size": 5,
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}
pool_config: Final


cnx_pool = pooling.MySQLConnectionPool(**pool_config)


def get_all_result(sql, param: Union[Tuple, None] = None) -> Dict:
    try:
        connection = cnx_pool.get_connection()
        cursor = connection.cursor()

        if param is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, param)
        result = cursor.fetchall()
        
        cursor.close()
        connection.close()
        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in result]
        return result

    except mysql.connector.Error as e:
        print(e)
        cursor.close()
        connection.close()
        return False

def execute_query(sql, param: Union[Tuple, None] = None) -> bool:
    try:
        connection = cnx_pool.get_connection()
        cursor = connection.cursor()

        if param is None:
            count = cursor.execute(sql)
        else:
            count = cursor.execute(sql, param)
        if count == 0:
            cursor.close()
            connection.close()
            return False
        connection.commit()
        cursor.close()
        connection.close()
        return True

    except mysql.connector.Error as e:
        print(e)
        cursor.close()
        connection.rollback()
        connection.close()
        return False
    
def dict_to_sqltext(_dict: Dict, exclude_col: List[str] = []) -> Tuple[str, tuple]:
    sqltext = []
    values = tuple()
    for key, value in list(_dict.items()):
        if key not in exclude_col:
            sqltext.append(f'{key}=%s')
            values += (value,)

    return ",".join(sqltext), values


def dict_delete_none(_dict: Dict) -> Dict:
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            dict_delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                dict_delete_none(v_i)

    return _dict