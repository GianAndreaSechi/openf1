from pydantic import BaseModel
from datetime import datetime

class Overtake(BaseModel):
    """
    Represents an overtake event.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        overtaking_driver_number (int): The number of the driver who is overtaking.
        overtaken_driver_number (int): The number of the driver who is being overtaken.
        date (datetime): The timestamp of the overtake.
        position (int): The position where the overtake happened.
    """
    meeting_key: int
    session_key: int
    overtaking_driver_number: int
    overtaken_driver_number: int
    date: datetime
    position: int