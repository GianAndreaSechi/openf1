from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union

class Interval(BaseModel):
    """
    Represents the interval between two drivers at a specific point in time.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        date (datetime): The timestamp of the interval measurement.
        gap_to_leader (str or float, optional): The gap to the leader.
        interval (str or float, optional): The interval to the driver ahead.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    date: datetime
    gap_to_leader: Optional[Union[str, float]] = None
    interval: Optional[Union[str, float]] = None
