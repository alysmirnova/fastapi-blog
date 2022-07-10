from ..database import Session
from .. import tables
from ..models.posts import PostUpdate, PostCreate
from typing import Optional
from fastapi import HTTPException, status
from ..tables import Post


class PostService:
    def __init__(self):
        self.session = Session()

    def _get(self, user_id: int, post_id: int):
        post = (
            self.session.query(Post).filter_by(id=post_id, user_id=user_id).first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get(self, user_id: int, post_id: int):
        return self._get(user_id, post_id)

    def get_list(self, user_id: Optional[int] = None):
        query = self.session.query(tables.Post)
        if user_id:
            query = query.filter_by(user_id=user_id)
        posts = query.all()
        return posts

    def create(self, user_id: int, post: PostCreate):
        new_post = tables.Post(**post.dict(), user_id=user_id)
        self.session.add(new_post)
        self.session.commit()
        return new_post

    def update(self, user_id: int, post_id: int, new_post: PostUpdate):
        post = self._get(user_id, post_id)
        for field, value in new_post:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delete(self, user_id: int, post_id: int):
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()

    def __del__(self):
        self.session.close()