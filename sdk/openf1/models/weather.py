from pydantic import BaseModel
from datetime import datetime

class Weather(BaseModel):
    """
    Represents weather data at a specific point in time.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        date (datetime): The timestamp of the weather measurement.
        air_temperature (float): The air temperature in Celsius.
        humidity (float): The humidity in percentage.
        pressure (float): The pressure in millibars.
        rainfall (int): The rainfall in millimeters.
        track_temperature (float): The track temperature in Celsius.
        wind_direction (int): The wind direction in degrees.
        wind_speed (float): The wind speed in km/h.
    """
    meeting_key: int
    session_key: int
    date: datetime
    air_temperature: float
    humidity: float
    pressure: float
    rainfall: int
    track_temperature: float
    wind_direction: int
    wind_speed: float