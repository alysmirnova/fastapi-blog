from fastapi import APIRouter
from ..models.posts import PostUpdate, PostCreate, Post
from ..services.posts import PostService
from fastapi import Depends, Response, status
from typing import List, Optional
from ..models.auth import User
from ..services.auth import get_current_user

router = APIRouter(
    prefix='/posts',
)


#@router.get('/', response_model=List[Post])
#def get_posts(
#        user: User = Depends(get_current_user),
#        service: PostService = Depends(),
#):
#    return service.get_list(user=user)


@router.post('/', response_model=Post)
def create_post(
    new_post: PostCreate,
    user: User = Depends(get_current_user),
    service: PostService = Depends()
):
    return service.create(user_id=user.id, post=new_post)


@router.get('/{post_id}', response_model=Post)
def get_post(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostService = Depends()
):
    return service.get(user.id, post_id)


@router.put('/{post_id}', response_model=Post)
def update_post(
    post_id: int,
    post: PostUpdate,
    user: User = Depends(get_current_user),
    service: PostService = Depends()
):
    return service.update(
        user.id,
        post_id,
        post,
    )


@router.delete('/{post_id}')
def delete_post(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostService = Depends()
):
    service.delete(user.id, post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)