from pydantic import BaseModel
from typing import Optional

class OvertakeDTO(BaseModel):
    date: Optional[str] = None
    meeting_key: Optional[int] = None
    overtaken_driver_number: Optional[int] = None
    overtaking_driver_number: Optional[int] = None
    position: Optional[int] = None
    session_key: Optional[int] = None
