from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RaceControl(BaseModel):
    """
    Represents a race control message.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        date (datetime, optional): The timestamp of the message.
        driver_number (int, optional): The number of the driver involved.
        lap_number (int, optional): The lap number when the message was issued.
        category (str, optional): The category of the message.
        flag (str, optional): The flag shown.
        scope (str, optional): The scope of the message.
        sector (int, optional): The sector where the message is relevant.
        message (str, optional): The content of the message.
    """
    meeting_key: int
    session_key: int
    date: Optional[datetime] = None
    driver_number: Optional[int] = None
    lap_number: Optional[int] = None
    category: Optional[str] = None
    flag: Optional[str] = None
    scope: Optional[str] = None
    sector: Optional[int] = None
    message: Optional[str] = None