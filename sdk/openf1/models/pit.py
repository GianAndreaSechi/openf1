from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Pit(BaseModel):
    """
    Represents a pit stop.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        date (datetime): The timestamp of the pit stop.
        pit_duration (int, optional): The duration of the pit stop in seconds.
        lap_number (int, optional): The lap number when the pit stop occurred.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    date: datetime
    pit_duration: Optional[int] = None
    lap_number: Optional[int] = None