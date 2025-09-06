from pydantic import BaseModel
from typing import Optional

class WeatherDTO(BaseModel):
    air_temperature: Optional[float] = None
    date: Optional[str] = None
    humidity: Optional[int] = None
    meeting_key: Optional[int] = None
    pressure: Optional[float] = None
    rainfall: Optional[int] = None
    session_key: Optional[int] = None
    track_temperature: Optional[float] = None
    wind_direction: Optional[int] = None
    wind_speed: Optional[float] = None
