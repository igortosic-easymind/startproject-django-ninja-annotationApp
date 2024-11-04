from ninja import Schema
from typing import Optional
from datetime import datetime


class ProjectCreate(Schema):
    title: str
    description: Optional[str] = None
    is_public: bool = False


class ProjectUpdate(Schema):
    title: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None


class CollaboratorSchema(Schema):
    user_id: int
    role: str


class ProjectOut(Schema):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    owner_id: int
    is_public: bool
