from pydantic import BaseModel
from typing import Optional

class StintDTO(BaseModel):
    compound: Optional[str] = None
    driver_number: Optional[int] = None
    lap_end: Optional[int] = None
    lap_start: Optional[int] = None
    meeting_key: Optional[int] = None
    session_key: Optional[int] = None
    stint_number: Optional[int] = None
    tyre_age_at_start: Optional[int] = None
