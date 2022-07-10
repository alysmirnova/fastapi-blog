from fastapi import APIRouter
from ..models.comments import CommentUpdate, CommentCreate, Comment
from ..services.comments import CommentService
from fastapi import Depends, Response, status
from typing import List
from ..models.auth import User
from ..services.auth import get_current_user

router = APIRouter(
    prefix='/comments',
)


@router.get('/{comment_id}', response_model=Comment)
def get_comment(
    comment_id: int,
    user: User = Depends(get_current_user),
    service: CommentService = Depends()
):
    return service.get(user.id, comment_id)


@router.get('/', response_model=List[Comment])
def get_comments(
    post_id: int,
    service: CommentService = Depends()
):
    return service.get_list(post_id)


@router.post('/', response_model=Comment)
def create_comment(
    new_comment: CommentCreate,
    user: User = Depends(get_current_user),
    service: CommentService = Depends()
):
    return service.create(user_id=user.id, comment=new_comment)


@router.put('/{comment_id}', response_model=Comment)
def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    user: User = Depends(get_current_user),
    service: CommentService = Depends()
):
    return service.update(
        user.id,
        comment_id,
        comment,
    )


@router.delete('/{comment_id}')
def delete_comment(
    comment_id: int,
    user: User = Depends(get_current_user),
    service: CommentService = Depends()
):
    service.delete(user.id, comment_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)