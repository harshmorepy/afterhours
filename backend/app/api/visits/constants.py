from enum import Enum

class VisitStatus(str, Enum):
    PENDING = "PENDING"
    CHECKED_IN = "CHECKED_IN"
    ACTIVE = "ACTIVE"
    CHECKED_OUT = "CHECKED_OUT"
    CANCELLED = "CANCELLED"

