from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    text: str


class Post(BasePost):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class PostCreate(BasePost):
    pass


class PostUpdate(BasePost):
    pass