from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..models.auth import UserCreate, Token, User
from ..services.auth import AuthService, get_current_user, get_db
from ..database import Session

router = APIRouter(
    prefix='/auth',
)


@router.post('/sign-up', response_model=Token)
def sign_up(
        user_data: UserCreate,
        auth_service: AuthService = Depends(),
        db: Session = Depends(get_db)
):
    return auth_service.register_new_user(user_data, db)


@router.post('/sign-in', response_model=Token)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
        db: Session = Depends(get_db)
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
        db
    )


@router.get('/user/', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user