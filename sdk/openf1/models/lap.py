from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class Lap(BaseModel):
    """
    Represents a single lap completed by a driver.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        lap_number (int): The lap number.
        date_start (datetime, optional): The timestamp when the lap started.
        duration_sector_1 (float, optional): The duration of sector 1 in seconds.
        duration_sector_2 (float, optional): The duration of sector 2 in seconds.
        duration_sector_3 (float, optional): The duration of sector 3 in seconds.
        i1_speed (int, optional): The speed at the first intermediate in km/h.
        i2_speed (int, optional): The speed at the second intermediate in km/h.
        is_pit_out_lap (bool): Whether this was a pit-out lap.
        lap_duration (float, optional): The total duration of the lap in seconds.
        segments_sector_1 (list[int], optional): The status of the segments in sector 1.
        segments_sector_2 (list[int], optional): The status of the segments in sector 2.
        segments_sector_3 (list[int], optional): The status of the segments in sector 3.
        st_speed (int, optional): The speed at the start/finish line in km/h.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    lap_number: int
    date_start: Optional[datetime] = None
    duration_sector_1: Optional[float] = None
    duration_sector_2: Optional[float] = None
    duration_sector_3: Optional[float] = None
    i1_speed: Optional[int] = None
    i2_speed: Optional[int] = None
    is_pit_out_lap: bool = False
    lap_duration: Optional[float] = None
    segments_sector_1: Optional[List[Optional[int]]] = None
    segments_sector_2: Optional[List[Optional[int]]] = None
    segments_sector_3: Optional[List[Optional[int]]] = None
    st_speed: Optional[int] = None