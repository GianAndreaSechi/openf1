from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Location(BaseModel):
    """
    Represents the location of a driver at a specific point in time.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        date (datetime): The timestamp of the location measurement.
        x (int, optional): The x-coordinate of the driver.
        y (int, optional): The y-coordinate of the driver.
        z (int, optional): The z-coordinate of the driver.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    date: datetime
    x: Optional[int] = None
    y: Optional[int] = None
    z: Optional[int] = None