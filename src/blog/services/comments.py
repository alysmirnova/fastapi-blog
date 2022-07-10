from ..database import Session
from ..models.comments import CommentCreate, CommentUpdate
from fastapi import HTTPException, status
from ..tables import Comment


class CommentService:
    def __init__(self):
        self.session = Session()

    def _get(self, user_id: int, comment_id: int):
        comment = (
            self.session.query(Comment).filter_by(id=comment_id, user_id=user_id).first()
        )
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return comment

    def get(self, user_id: int, comment_id: int):
        return self._get(user_id, comment_id)

    def get_list(self, post_id: int):
        query = self.session.query(Comment).filter_by(post_id=post_id)
        comments = query.all()
        if not comments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return comments

    def create(self, user_id: int, comment: CommentCreate):
        new_comment = Comment(**comment.dict(), user_id=user_id)
        self.session.add(new_comment)
        self.session.commit()
        return new_comment

    def update(self, user_id: int, comment_id: int, new_comment: CommentUpdate):
        comment = self._get(user_id, comment_id)
        for field, value in new_comment:
            setattr(comment, field, value)
        self.session.commit()
        return comment

    def delete(self, user_id: int, comment_id: int):
        comment = self._get(user_id, comment_id)
        self.session.delete(comment)
        self.session.commit()

    def __del__(self):
        self.session.close()