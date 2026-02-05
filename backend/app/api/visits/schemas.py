from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class VisitCreate(BaseModel):
    person_name: str
    space: str
    vibe: Optional[str] = "calm"


class VisitResponse(BaseModel):
    visit_id: str
    person_name: str
    space: str
    vibe: str
    started_at: datetime
