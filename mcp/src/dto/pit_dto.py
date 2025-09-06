from pydantic import BaseModel
from typing import Optional

class PitDTO(BaseModel):
    date: Optional[str] = None
    driver_number: Optional[int] = None
    lap_number: Optional[int] = None
    meeting_key: Optional[int] = None
    pit_duration: Optional[float] = None
    session_key: Optional[int] = None
