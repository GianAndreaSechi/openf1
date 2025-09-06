from pydantic import BaseModel
from typing import Optional

class LocationDTO(BaseModel):
    date: Optional[str] = None
    driver_number: Optional[int] = None
    meeting_key: Optional[int] = None
    session_key: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    z: Optional[int] = None
