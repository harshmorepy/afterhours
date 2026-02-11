from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import uuid

from .schemas import VisitCreate, VisitResponse, VisitStatus
from . import service

router = APIRouter(prefix="/visits", tags=["Visits"])


# =========================
# CREATE VISIT
# =========================
@router.post("/", response_model=VisitResponse)
def start_visit(data: VisitCreate):
    visit = VisitResponse(
        visit_id=str(uuid.uuid4()),
        person_name=data.person_name,
        space=data.space,
        vibe=data.vibe,

        status=VisitStatus.PENDING,
        started_at=datetime.utcnow(),

        checked_in_at=None,
        activated_at=None,
        checked_out_at=None,
        cancelled_at=None
    )
    return service.create_visit(visit)


# =========================
# VISIT LIFECYCLE ACTIONS
# =========================
@router.patch("/{visit_id}/check-in", response_model=VisitResponse)
def check_in(visit_id: str):
    try:
        return service.check_in_visit(visit_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{visit_id}/activate", response_model=VisitResponse)
def activate(visit_id: str):
    try:
        return service.activate_visit(visit_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{visit_id}/check-out", response_model=VisitResponse)
def check_out(visit_id: str):
    try:
        return service.check_out_visit(visit_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{visit_id}/cancel", response_model=VisitResponse)
def cancel(visit_id: str):
    try:
        return service.cancel_visit(visit_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/active", response_model=list[VisitResponse])
def active_visits():
    return service.get_active_visits()


@router.get("/occupancy")
def occupancy():
    return JSONResponse(
        content={
            "current_occupancy": service.get_occupancy_count()
        },
        media_type="application/json; charset=utf-8"
    )

@router.get("/summary")
def summary():
    return JSONResponse(
        content=service.get_visit_summary(),
        media_type="application/json; charset=utf-8"
    )





# =========================
# HEALTH / ROOT ENDPOINT
# =========================
@router.get("/")
def get_visits():
    return JSONResponse(
        content={"message": "visits endpoint is live 🎉"},
        media_type="application/json; charset=utf-8"
    )


    