from pydantic import BaseModel
from typing import Optional

class DriverDTO(BaseModel):
    broadcast_name: Optional[str] = None
    country_code: Optional[str] = None
    driver_number: Optional[int] = None
    first_name: Optional[str] = None
    full_name: Optional[str] = None
    headshot_url: Optional[str] = None
    last_name: Optional[str] = None
    meeting_key: Optional[int] = None
    name_acronym: Optional[str] = None
    session_key: Optional[int] = None
    team_colour: Optional[str] = None
    team_name: Optional[str] = None
