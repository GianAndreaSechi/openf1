from pydantic import BaseModel
from typing import Optional

class Stint(BaseModel):
    """
    Represents a driver's stint on a set of tyres.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        stint_number (int): The number of the stint.
        driver_number (int): The number of the driver.
        lap_start (int): The lap number when the stint started.
        lap_end (int): The lap number when the stint ended.
        compound (str, optional): The tyre compound used in the stint.
        tyre_age_at_start (int, optional): The age of the tyre at the start of the stint.
    """
    meeting_key: int
    session_key: int
    stint_number: int
    driver_number: int
    lap_start: int
    lap_end: int
    compound: Optional[str] = None
    tyre_age_at_start: Optional[int] = None