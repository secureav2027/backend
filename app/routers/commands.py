from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app import command_store
from app.auth import get_current_user

router = APIRouter()


class NewCommand(BaseModel):
    command: str


class CommandResult(BaseModel):
    status: str
    result: Optional[str] = None


@router.post("/commands")
def create_command(payload: NewCommand, username: str = Depends(get_current_user)):
    return command_store.add_command(payload.command)


@router.get("/commands/pending")
def get_pending_commands(username: str = Depends(get_current_user)):
    return command_store.pop_pending()


@router.post("/commands/{command_id}/result")
def report_result(
    command_id: int, payload: CommandResult, username: str = Depends(get_current_user)
):
    entry = command_store.set_result(command_id, payload.status, payload.result)
    if entry is None:
        raise HTTPException(status_code=404, detail="Command not found")
    return entry


@router.get("/commands")
def list_commands(username: str = Depends(get_current_user)):
    return command_store.list_all()
