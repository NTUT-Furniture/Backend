import crud
import datetime

def get_all_column_from_account():
    result = crud.read_default("*", "`Account`", "")
    return result

def get_excepted_columns_from_account(COLUMNS: str, CONDITIONS: str):
    result = crud.read_default(COLUMNS, "`Account`", CONDITIONS)
    return result

def update_excepted_value_from_account(SET_VALUES: dict, CONDITIONS: str):
    crud.update_default("`Account`", SET_VALUES, CONDITIONS)

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

def update_account_setting(ID: str, NAME: str, EMAIL: str, PHONE: str, CITY: str, DISTRICT: str, STREET: str, ALLEY: int, FLOOR: int, BIRTHDAY: datetime):
    CONDITION = f"account_uuid='{ID}'"
    SET_VALUES = {
        "name": NAME,
        "email": EMAIL,
        "phone": PHONE,
        "city": CITY,
        "district": DISTRICT,
        "street": STREET,
        "alley": ALLEY,
        "floor": FLOOR,
        "birthday": BIRTHDAY
    }
    update_excepted_value_from_account(SET_VALUES, CONDITION)

a = get_all_column_from_account()
print('all')
print(a)
print('setting info')
print(get_account_avator("assdfd"))
print('account setting before')
print(get_account_setting("assdfd"))
print(get_user_name('assdfd'))
update_account_setting('assdfd', 'account name', 'awgwrg@gmail.com', '02348123312', 'asd', 'asdef', 'esbea', 1, 1, datetime.datetime(2014, 2, 14, 0, 0))
print('modify name')
print(get_account_setting("assdfd"))