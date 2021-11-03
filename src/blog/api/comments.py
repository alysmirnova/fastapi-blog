from fastapi import APIRouter
from ..models.comments import CommentUpdate, CommentCreate, Comment
from ..services.comments import CommentService
from fastapi import Depends, Response, status
from typing import List

router = APIRouter(
    prefix='/comments',
)


@router.get('/{comment_id}', response_model=Comment)
def get_comment(
    comment_id: int,
    service: CommentService = Depends()
):
    return service.get(comment_id)


@router.get('/', response_model=List[Comment])
def get_comments(
    post_id: int,
    service: CommentService = Depends()
):
    return service.get_list(post_id)


@router.post('/', response_model=Comment)
def create_comment(
    new_comment: CommentCreate,
    service: CommentService = Depends()
):
    return service.create(new_comment)


@router.put('/{comment_id}', response_model=Comment)
def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    service: CommentService = Depends()
):
    return service.update(
        comment_id,
        comment,
    )


@router.delete('/{comment_id}')
def delete_comment(
    comment_id: int,
    service: CommentService = Depends()
):
    service.delete(comment_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)