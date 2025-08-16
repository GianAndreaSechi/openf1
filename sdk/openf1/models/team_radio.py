from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TeamRadio(BaseModel):
    """
    Represents a team radio message.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        recording_url (str): The URL of the radio message recording.
        date (datetime, optional): The timestamp of the radio message.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    recording_url: str
    date: Optional[datetime] = None
