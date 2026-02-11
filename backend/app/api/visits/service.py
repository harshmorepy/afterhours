from datetime import datetime
from typing import Dict

from .schemas import VisitResponse, VisitStatus

# ================================
# In-Memory Store (Temporary DB)
# ================================
VISITS: Dict[str, VisitResponse] = {}


# ================================
# CORE VISIT FUNCTIONS
# ================================

def create_visit(visit: VisitResponse) -> VisitResponse:
    VISITS[visit.visit_id] = visit
    return visit


def get_visit(visit_id: str) -> VisitResponse:
    visit = VISITS.get(visit_id)
    if not visit:
        raise ValueError("Visit not found")
    return visit


def check_in_visit(visit_id: str) -> VisitResponse:
    visit = get_visit(visit_id)

    if visit.status != VisitStatus.PENDING:
        raise ValueError("Only PENDING visits can be checked in")

    visit.status = VisitStatus.CHECKED_IN
    visit.checked_in_at = datetime.utcnow()
    return visit


def activate_visit(visit_id: str) -> VisitResponse:
    visit = get_visit(visit_id)

    if visit.status != VisitStatus.CHECKED_IN:
        raise ValueError("Only CHECKED_IN visits can be activated")

    visit.status = VisitStatus.ACTIVE
    visit.activated_at = datetime.utcnow()
    return visit


def check_out_visit(visit_id: str) -> VisitResponse:
    visit = get_visit(visit_id)

    if visit.status != VisitStatus.ACTIVE:
        raise ValueError("Only ACTIVE visits can be checked out")

    visit.status = VisitStatus.CHECKED_OUT
    visit.checked_out_at = datetime.utcnow()
    return visit


def cancel_visit(visit_id: str) -> VisitResponse:
    visit = get_visit(visit_id)

    if visit.status in [VisitStatus.CHECKED_OUT, VisitStatus.CANCELLED]:
        raise ValueError("Visit already finalized")

    visit.status = VisitStatus.CANCELLED
    visit.cancelled_at = datetime.utcnow()
    return visit


# ================================
# VISIT INTELLIGENCE (Analytics)
# ================================

def get_active_visits():
    return [
        visit
        for visit in VISITS.values()
        if visit.status in [VisitStatus.CHECKED_IN, VisitStatus.ACTIVE]
    ]


def get_occupancy_count():
    return len(get_active_visits())


def get_visit_summary():
    summary = {
        "total_visits": len(VISITS),
        "active": 0,
        "checked_out": 0,
        "cancelled": 0,
        "pending": 0,
        "checked_in": 0,
    }

    for visit in VISITS.values():
        summary[visit.status.value.lower()] += 1

    return summary

