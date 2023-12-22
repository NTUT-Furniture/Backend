import os
from typing import Final
from typing import Union, Tuple, Dict, Optional

import mysql.connector
from dotenv import load_dotenv
from fastapi import HTTPException
from mysql.connector import pooling
from starlette import status

load_dotenv()

pool_config: Final = {
    "pool_name": "pool",
    "pool_size": 5,
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}

cnx_pool = pooling.MySQLConnectionPool(**pool_config)

def execute_sql(sql, param: Optional[Tuple] = None, fetch: bool = False) -> Union[Dict, bool]:
    connection = None
    cursor = None
    try:
        connection = cnx_pool.get_connection()
        cursor = connection.cursor()

        count = cursor.execute(sql, param or ())
        if fetch:
            result = cursor.fetchall()
            if result:
                column_names = [desc[0] for desc in cursor.description]
                result = [dict(zip(column_names, row)) for row in result]
                [result_row.update(
                    {"update_time": result_row["update_time"].strftime("%Y-%m-%d %H:%M:%S")}
                    ) if "update_time" in result_row else result_row for result_row in result]
        else:
            result = count != 0
            connection.commit()

    except mysql.connector.Error as e:
        if not fetch and connection is not None:
            connection.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Some error occurred when executing sql command:{e}"  # TODO: Remove sql error on release
        )

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

    return result

def get_all_results(sql: str, param: Optional[Tuple] = None) -> Union[Dict, bool]:
    return execute_sql(sql, param, True)

def execute_query(sql, param: Optional[Tuple] = None) -> bool:
    return execute_sql(sql, param)

def dict_to_sql_command(_dict: Dict, exclude_col=None) -> Tuple[str, tuple]:
    if exclude_col is None:
        exclude_col = []
    sql_command = []
    values = tuple()
    for key, value in list(_dict.items()):
        if key not in exclude_col:
            sql_command.append(f'{key}=%s')
            values += (value,)

    return ",".join(sql_command), values

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

async def if_exists_in_db(table_name, column_name, value) -> bool:
    sql = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {column_name} = %s) AS UUID_Exists;"
    result = get_all_results(sql, (value,))
    assert result[0]["UUID_Exists"] in [0, 1]
    return result[0]["UUID_Exists"] == 1

async def if_one_owns_the_other(
        table_name: str, col1: str, val1: str, col2: str, val2: str
) -> bool:
    sql = f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE  {col1} = %s AND {col2} = %s) AS 'Exists';"
    result = get_all_results(sql, (val1, val2))
    assert result[0]["Exists"] in [0, 1]
    return result[0]["Exists"] == 1

async def get_shop_by_account_uuid(account_uuid: str) -> str:
    sql = """
        SELECT shop_uuid FROM `Shop` WHERE account_uuid = %s LIMIT 1;
    """
    result = get_all_results(sql, (account_uuid,))
    if result:
        return result[0]["shop_uuid"]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Shop under account: {account_uuid} is not found"
    )
