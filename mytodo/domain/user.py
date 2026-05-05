# mytodo/domain/user.py

from datetime import datetime, timezone

from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class User(BaseModel):
    id: str
    username: str
    password: str
    created_at: datetime = Field(default_factory=utc_now)
