from pydantic import BaseModel
from typing import Optional

class TeamRadioDTO(BaseModel):
    date: Optional[str] = None
    driver_number: Optional[int] = None
    meeting_key: Optional[int] = None
    recording_url: Optional[str] = None
    session_key: Optional[int] = None
