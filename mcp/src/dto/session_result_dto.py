from pydantic import BaseModel
from typing import Optional

class SessionResultDTO(BaseModel):
    dnf: Optional[bool] = None
    dns: Optional[bool] = None
    dsq: Optional[bool] = None
    driver_number: Optional[int] = None
    duration: Optional[float] = None
    gap_to_leader: Optional[float] = None
    number_of_laps: Optional[int] = None
    meeting_key: Optional[int] = None
    position: Optional[int] = None
    session_key: Optional[int] = None
