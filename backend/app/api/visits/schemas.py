from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class VisitStatus(str, Enum):
    PENDING = "PENDING"
    CHECKED_IN = "CHECKED_IN"
    ACTIVE = "ACTIVE"
    CHECKED_OUT = "CHECKED_OUT"
    CANCELLED = "CANCELLED"


class VisitCreate(BaseModel):
    person_name: str
    space: str
    vibe: Optional[str] = None


class VisitResponse(BaseModel):
    visit_id: str
    person_name: str
    space: str
    vibe: Optional[str] = None

    status: VisitStatus
    started_at: datetime

    checked_in_at: Optional[datetime] = None
    activated_at: Optional[datetime] = None
    checked_out_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None

