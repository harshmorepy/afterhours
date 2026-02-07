from datetime import datetime
from typing import Dict

from .schemas import VisitResponse, VisitStatus

# Temporary in-memory store (later → database)
VISITS: Dict[str, VisitResponse] = {}


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
