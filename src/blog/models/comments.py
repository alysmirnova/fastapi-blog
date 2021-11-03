from pydantic import BaseModel


class BaseComment(BaseModel):
    user_id: int
    post_id: int
    text: str


class Comment(BaseComment):
    id: int

    class Config:
        orm_mode = True


class CommentCreate(BaseComment):
    pass


class CommentUpdate(BaseComment):
    pass