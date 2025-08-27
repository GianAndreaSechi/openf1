from pydantic import BaseModel
from typing import Optional

class MeetingDTO(BaseModel):
    circuit_key: Optional[int] = None
    circuit_short_name: Optional[str] = None
    country_code: Optional[str] = None
    country_key: Optional[int] = None
    country_name: Optional[str] = None
    date_start: Optional[str] = None
    gmt_offset: Optional[str] = None
    location: Optional[str] = None
    meeting_key: Optional[int] = None
    meeting_name: Optional[str] = None
    meeting_official_name: Optional[str] = None
    year: Optional[int] = None
