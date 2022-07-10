from pydantic import BaseModel


class BaseComment(BaseModel):
    post_id: int
    text: str


class Comment(BaseComment):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class CommentCreate(BaseComment):
    pass


class CommentUpdate(BaseModel):
    text: str