from pydantic import BaseModel
from typing import Optional, List

class LapDTO(BaseModel):
    date_start: Optional[str] = None
    driver_number: Optional[int] = None
    duration_sector_1: Optional[float] = None
    duration_sector_2: Optional[float] = None
    duration_sector_3: Optional[float] = None
    i1_speed: Optional[int] = None
    i2_speed: Optional[int] = None
    is_pit_out_lap: Optional[bool] = None
    lap_duration: Optional[float] = None
    lap_number: Optional[int] = None
    meeting_key: Optional[int] = None
    segments_sector_1: Optional[List[int]] = None
    segments_sector_2: Optional[List[int]] = None
    segments_sector_3: Optional[List[int]] = None
    session_key: Optional[int] = None
    st_speed: Optional[int] = None
