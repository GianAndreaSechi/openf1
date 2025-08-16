from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Driver(BaseModel):
    """
    Represents a driver.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int, optional): The number of the driver.
        broadcast_name (str, optional): The broadcast name of the driver.
        full_name (str, optional): The full name of the driver.
        name_acronym (str, optional): The acronym of the driver's name.
        team_name (str, optional): The name of the driver's team.
        team_colour (str, optional): The color of the driver's team.
        first_name (str, optional): The first name of the driver.
        last_name (str, optional): The last name of the driver.
        headshot_url (str, optional): The URL of the driver's headshot.
        country_code (str, optional): The country code of the driver.
    """
    meeting_key: int
    session_key: int
    driver_number: Optional[int] = None
    broadcast_name: Optional[str] = None
    full_name: Optional[str] = None
    name_acronym: Optional[str] = None
    team_name: Optional[str] = None
    team_colour: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    headshot_url: Optional[str] = None
    country_code: Optional[str] = None