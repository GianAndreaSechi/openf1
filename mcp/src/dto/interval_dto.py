from pydantic import BaseModel
from typing import Optional

class IntervalDTO(BaseModel):
    date: Optional[str] = None
    driver_number: Optional[int] = None
    gap_to_leader: Optional[float] = None
    interval: Optional[float] = None
    meeting_key: Optional[int] = None
    session_key: Optional[int] = None
