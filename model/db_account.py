import crud

def get_all_column_from_account():
    result = crud.read_default("*", "`Account`", "")
    return result

def get_excepted_columns_from_account(COLUMNS: str, CONDITIONS: str):
    result = crud.read_default(COLUMNS, "`Account`", CONDITIONS)
    return result

def get_account_avator(ID: str):
    CONDITION = f"account_uuid='{ID}'" if ID else ""
    return get_excepted_columns_from_account("image_url", CONDITION)

def get_account_setting(ID: str):
    CONDITION = f"account_uuid='{ID}'" if ID else ""
    COLUMNS = "name, email, phone, city, district, street, alley, floor, birthday"
    return get_excepted_columns_from_account(COLUMNS, CONDITION)

def get_user_name(ID: str):
    CONDITION = f"account_uuid='{ID}'" if ID else ""
    return get_excepted_columns_from_account("name", CONDITION)

a = get_all_column_from_account()
print('all')
print(a)
print('setting info')
print(get_account_avator("assdfd"))
print(get_account_setting("assdfd"))
print(get_user_name('assdfd'))