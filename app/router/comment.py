import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import app.utils.auth as auth
from app.model.account import CreateAccountForm, UpdateAccountForm, Account, AccountList
from app.model.comment import CreateCommentForm, UpdateCommentForm, Comment, CommentList, CommentNoSigned, CommentListNoSigned
from app.model.auth import Token
from app.model.general import ErrorModel
from app.router.login import login_for_access_token
from app.utils.db_process import execute_query, dict_to_sql_command, dict_delete_none, get_all_results

router = APIRouter(
    tags=["comment"],
)

@router.get(
    "/", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": CommentList
        },
    },
)
async def get_comments(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        product_uuid: str
):
    """
    usage example:
    email@gmail.com 123

    product_uuid: 094527b3-f8f1-4dfc-82cb-066a48d29caa
    """
    sql = """
        SELECT 
            C.comment_uuid,
            C.account_uuid,
            A.name,
            C.text,
            C.likes,
            C.dislikes,
            C.update_time
        FROM Comment AS C
        LEFT JOIN Account AS A
        ON C.account_uuid = A.account_uuid
        WHERE C.product_uuid = %s
        ORDER BY C.update_time DESC
    """
    result = get_all_results(sql, (product_uuid,))
    [result[i].update({'is_mine': 1 if result[i]['account_uuid'] == account.account_uuid else 0}) for i in
     range(len(result))]

    if result:
        return CommentList(comments=[Comment(**comment) for comment in result])
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comments found")


@router.post(
    "/", tags=["post"], responses={
        status.HTTP_200_OK: {
            "model": CreateCommentForm
        },
    },
)
async def create_comment(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        comment_form: CreateCommentForm = Depends(CreateCommentForm.as_form)
):
    """
    usage example:
    email.gmail.com 123
    product_uuid: 094527b3-f8f1-4dfc-82cb-066a48d29caa
    """
    comment_form = comment_form.model_dump()
    sql = """
        INSERT INTO Comment 
        VALUES (
            %s, %s, %s, %s, DEFAULT, DEFAULT, DEFAULT
        )
    """

    result = execute_query(sql, (str(uuid.uuid4()), comment_form['product_uuid'], account.account_uuid, comment_form['text'],))
    if result:
        return CreateCommentForm(**comment_form)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Create comment failed")

@router.put(
    "/", tags=["update"], responses={
        status.HTTP_200_OK: {
            "model": UpdateCommentForm
        },
    },
)
async def update_comment(
        account: Annotated[
            Account,
            Depends(auth.get_current_active_user)],
        comment_form: UpdateCommentForm = Depends(UpdateCommentForm.as_form)
):
    """
    usage example:
    t110590028@gmail.com 123
    comment_uuid: 0dbc5975-9f28-11ee-9df2-0242ac140002
    """
    comment_form = comment_form.model_dump()
    sql_text, sql_text_value = dict_to_sql_command(dict_delete_none(comment_form), 'comment_uuid', prefix='C')
    sql = f"""
        UPDATE Comment As C
        SET {sql_text}
        WHERE comment_uuid = %s AND account_uuid = %s
    """
    print(sql)
    result = execute_query(sql, sql_text_value + (comment_form['comment_uuid'], account.account_uuid,))
    if result:
        return UpdateCommentForm(**comment_form)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Update comment failed")



@router.get(
    "/guest", tags=["get"], responses={
        status.HTTP_200_OK: {
            "model": CommentListNoSigned
        },
    },
)
async def get_comments_guest(
        product_uuid: str
):
    """
    usage example:
    email@gmail.com 123

    product_uuid: 094527b3-f8f1-4dfc-82cb-066a48d29caa
    """
    sql = """
        SELECT 
            C.comment_uuid,
            C.account_uuid,
            A.name,
            C.text,
            C.likes,
            C.dislikes,
            C.update_time
        FROM Comment AS C
        LEFT JOIN Account AS A
        ON C.account_uuid = A.account_uuid
        WHERE C.product_uuid = %s
        ORDER BY C.update_time DESC
    """
    result = get_all_results(sql, (product_uuid,))

    if result:
        return CommentListNoSigned(comments=[CommentNoSigned(**comment) for comment in result])
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comments found")

