import uuid

from fastapi import APIRouter, Depends, status, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.account import CreateAccountForm, ReturnCreateAccount, UpdateAccountForm, ReturnAccount
from model.general import ErrorModel, SuccessModel
from model.image_io import ImageIOSuccessModel, ImageIOFailModel
from utils import image_io
from utils.db_process import get_all_result, execute_query, dict_delete_none, dict_to_sql_command

router = APIRouter(
    tags=["account"],
)

@router.post("/create", tags=["account"], responses={
    status.HTTP_200_OK: {"model": ReturnCreateAccount},
    status.HTTP_404_NOT_FOUND: {"model": ErrorModel}
})
async def create_account(
        account_form: CreateAccountForm = Depends(CreateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    id = uuid.uuid4()
    sql = """
        INSERT INTO `Account`
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, DEFAULT, DEFAULT
        );
    """
    result = execute_query(sql, (str(id),) + tuple(account_form.values()))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({"msg": "success", "data": id})
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({"msg": "fail"})
    )

@router.put("/update", tags=["account"], responses={
    status.HTTP_200_OK: {"model": SuccessModel},
    status.HTTP_404_NOT_FOUND: {"model": ErrorModel}
})
async def update_account(
        account_form: UpdateAccountForm = Depends(UpdateAccountForm.as_form)
):
    account_form = account_form.model_dump()
    account_form = dict_delete_none(account_form)
    sql_set_text, sql_set_values = dict_to_sql_command(account_form)
    sql = f"""UPDATE `Account` SET {sql_set_text} WHERE account_uuid = %s;"""
    result = execute_query(sql, (sql_set_values + (account_form["account_uuid"],)))
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({"msg": "success"})
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({"msg": "fail"})
    )

@router.get("/get", tags=["account"], responses={
    status.HTTP_200_OK: {"model": ReturnAccount},
    status.HTTP_404_NOT_FOUND: {"model": ErrorModel}
})
async def get_account(
        account_uuid: str = None
):
    sql = """
        SELECT
            account_uuid,
            name,
            image_url,
            email,
            phone,
            birthday,
            address,
            is_active,
            update_time
        FROM `Account`
    """
    if account_uuid is not None:
        sql += " WHERE account_uuid = %s;"
        result = get_all_result(sql, (account_uuid,))
    else:
        sql += ";"
        result = get_all_result(sql)
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({"msg": "success", "data": result})
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({"msg": "fail"})
    )

@router.post("/{id}/upload_image",
             description="Upload image(jpeg/png) for product, max_size = 10MB",
             responses={
                 status.HTTP_200_OK: {"model": ImageIOSuccessModel},
                 status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel},
             },
             tags=["account", "img_upload"]
             )
async def upload_image(id: str, file: UploadFile):
    script = """
    SELECT EXISTS(SELECT 1 FROM Account WHERE account_uuid = '%d') AS UUID_Exists;
    """
    result = execute_query(script, (id,))
    if result:
        return await image_io.save_file(file, image_io.ImgSourceEnum.avatar, id)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": "No such account" + id})
    )

@router.get("/{id}/get_image/{file_name}",
            description="Get image(jpeg/png) for product",
            responses={
                status.HTTP_200_OK: {"model": ImageIOSuccessModel},
                status.HTTP_400_BAD_REQUEST: {"model": ImageIOFailModel},
            },
            tags=["account", "img_get"]
            )
async def get_image(id: str, file_name: str):
    result = await image_io.get_file(image_io.ImgSourceEnum.avatar, id, file_name)
    if result:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({"msg": "success", "data": result})
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"msg": "fail"})
    )
