from pydantic import BaseModel
from datetime import datetime

class Position(BaseModel):
    """
    Represents the position of a driver at a specific point in time.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        date (datetime): The timestamp of the position measurement.
        position (int): The position of the driver.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    date: datetime
    position: int