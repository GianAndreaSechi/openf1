from pydantic import BaseModel
from typing import Optional

class CarDataDTO(BaseModel):
    brake: Optional[int] = None
    date: Optional[str] = None
    driver_number: Optional[int] = None
    drs: Optional[int] = None
    meeting_key: Optional[int] = None
    n_gear: Optional[int] = None
    rpm: Optional[int] = None
    session_key: Optional[int] = None
    speed: Optional[int] = None
    throttle: Optional[int] = None
