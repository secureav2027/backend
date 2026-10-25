import itertools
from datetime import datetime, timezone
from typing import Optional

_next_id = itertools.count(1)
_commands: dict[int, dict] = {}


def add_command(command: str) -> dict:
    command_id = next(_next_id)
    entry = {
        "id": command_id,
        "command": command,
        "status": "pending",
        "result": None,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _commands[command_id] = entry
    return entry


def pop_pending() -> list[dict]:
    pending = [c for c in _commands.values() if c["status"] == "pending"]
    for c in pending:
        c["status"] = "dispatched"
    return pending


def set_result(command_id: int, status: str, result: Optional[str]) -> Optional[dict]:
    entry = _commands.get(command_id)
    if entry is None:
        return None
    entry["status"] = status
    entry["result"] = result
    return entry


def list_all() -> list[dict]:
    return list(_commands.values())
