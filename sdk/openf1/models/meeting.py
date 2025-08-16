from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Meeting(BaseModel):
    """
    Represents a race meeting.

    Attributes:
        meeting_key (int): The key of the meeting.
        circuit_key (int, optional): The key of the circuit.
        circuit_short_name (str, optional): The short name of the circuit.
        meeting_code (str, optional): The code of the meeting.
        location (str, optional): The location of the meeting.
        country_key (int, optional): The key of the country.
        country_code (str, optional): The code of the country.
        country_name (str, optional): The name of the country.
        meeting_name (str, optional): The name of the meeting.
        meeting_official_name (str, optional): The official name of the meeting.
        gmt_offset (str, optional): The GMT offset of the meeting.
        date_start (datetime, optional): The start date of the meeting.
        year (int, optional): The year of the meeting.
    """
    meeting_key: int
    circuit_key: Optional[int] = None
    circuit_short_name: Optional[str] = None
    meeting_code: Optional[str] = None
    location: Optional[str] = None
    country_key: Optional[int] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    meeting_name: Optional[str] = None
    meeting_official_name: Optional[str] = None
    gmt_offset: Optional[str] = None
    date_start: Optional[datetime] = None
    year: Optional[int] = None