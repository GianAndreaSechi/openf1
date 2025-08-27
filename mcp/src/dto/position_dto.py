from pydantic import BaseModel
from typing import Optional

class PositionDTO(BaseModel):
    date: Optional[str] = None
    driver_number: Optional[int] = None
    meeting_key: Optional[int] = None
    position: Optional[int] = None
    session_key: Optional[int] = None
