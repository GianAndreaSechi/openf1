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

    def to_dict(self) -> dict:
        return {
            "broadcast_name": self.broadcast_name,
            "country_code": self.country_code,
            "driver_number": self.driver_number,
            "first_name": self.first_name,
            "full_name": self.full_name,
            "headshot_url": self.headshot_url,
            "last_name": self.last_name,
            "meeting_key": self.meeting_key,
            "name_acronym": self.name_acronym,
            "session_key": self.session_key,
            "team_colour": self.team_colour,
            "team_name": self.team_name,
        }
