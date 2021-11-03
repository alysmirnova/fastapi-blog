from fastapi import APIRouter
from .posts import router as post_router
from .comments import router as comment_router
from .auth import router as auth_router

router = APIRouter()
router.include_router(post_router)
router.include_router(comment_router)
router.include_router(auth_router)