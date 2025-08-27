from pydantic import BaseModel
from typing import Optional

class RaceControlDTO(BaseModel):
    category: Optional[str] = None
    date: Optional[str] = None
    driver_number: Optional[int] = None
    flag: Optional[str] = None
    lap_number: Optional[int] = None
    meeting_key: Optional[int] = None
    message: Optional[str] = None
    scope: Optional[str] = None
    sector: Optional[int] = None
    session_key: Optional[int] = None
