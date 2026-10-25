from fastapi import APIRouter, Depends

from app.auth import get_current_user

router = APIRouter()


@router.get("/protected-resource")
def protected_resource(username: str = Depends(get_current_user)):
    return {"message": f"Hello, {username}. This is protected data."}
