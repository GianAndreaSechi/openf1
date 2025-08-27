from pydantic import BaseModel
from typing import Optional

class SessionDTO(BaseModel):
    circuit_key: Optional[int] = None
    circuit_short_name: Optional[str] = None
    country_code: Optional[str] = None
    country_key: Optional[int] = None
    country_name: Optional[str] = None
    date_end: Optional[str] = None
    date_start: Optional[str] = None
    gmt_offset: Optional[str] = None
    location: Optional[str] = None
    meeting_key: Optional[int] = None
    session_key: Optional[int] = None
    session_name: Optional[str] = None
    session_type: Optional[str] = None
    year: Optional[int] = None
