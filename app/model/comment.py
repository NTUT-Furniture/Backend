from datetime import datetime, date
from typing import List

from pydantic import BaseModel

from app.utils.as_form import as_form

class Comment(BaseModel):
    comment_uuid: str
    account_uuid: str
    name: str
    text: str
    likes: int
    dislikes: int
    update_time: str
    is_mine: int

class CommentNoSigned(BaseModel):
    comment_uuid: str
    account_uuid: str
    name: str
    text: str
    likes: int
    dislikes: int
    update_time: str
class CommentList(BaseModel):
    comments: List[Comment]

class CommentListNoSigned(BaseModel):
    comments: List[CommentNoSigned]

@as_form
class CreateCommentForm(BaseModel):
    product_uuid: str
    text: str

@as_form
class UpdateCommentForm(BaseModel):
    comment_uuid: str
    text: str | None = None

@as_form
class CreateLikeForm(BaseModel):
    comment_uuid: str
    if_hates: int

@as_form
class DeleteLikeForm(BaseModel):
    comment_uuid: str
