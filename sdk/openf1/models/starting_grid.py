from pydantic import BaseModel
from typing import Optional

class StartingGrid(BaseModel):
    """
    Represents a driver's position on the starting grid.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        position (int, optional): The starting grid position of the driver.
        lap_duration (float, optional): The lap time that determined the grid position.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    position: Optional[int] = None
    lap_duration: Optional[float] = None