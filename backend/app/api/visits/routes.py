from fastapi import APIRouter
from fastapi.responses import JSONResponse 
from datetime import datetime
import uuid

from .schemas import VisitCreate, VisitResponse

router = APIRouter(prefix="/visits", tags=["Visits"])


@router.post("/", response_model=VisitResponse)
def start_visit(data: VisitCreate):
    return VisitResponse(
        visit_id=str(uuid.uuid4()),
        person_name=data.person_name,
        space=data.space,
        vibe=data.vibe,
        started_at=datetime.utcnow()
    )



@router.get("/")
def get_visits():
    return JSONResponse(
        content={"message": "visits endpoint is live 🎉"},
        media_type="application/json; charset=utf-8"
    )

    