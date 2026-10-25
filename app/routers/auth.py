from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.auth import authenticate_user, create_access_token

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    token = create_access_token(credentials.username)
    return TokenResponse(access_token=token)
