from pydantic import BaseModel
from typing import Optional

class StartingGridDTO(BaseModel):
    driver_number: Optional[int] = None
    lap_duration: Optional[float] = None
    meeting_key: Optional[int] = None
    position: Optional[int] = None
    session_key: Optional[int] = None
