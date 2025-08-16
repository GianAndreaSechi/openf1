from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Session(BaseModel):
    """
    Represents a session.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        location (str, optional): The location of the session.
        date_start (datetime, optional): The start date of the session.
        date_end (datetime, optional): The end date of the session.
        session_type (str, optional): The type of the session (e.g., Practice, Qualifying, Race).
        session_name (str, optional): The name of the session.
        country_key (int, optional): The key of the country.
        country_code (str, optional): The code of the country.
        country_name (str, optional): The name of the country.
        circuit_key (int, optional): The key of the circuit.
        circuit_short_name (str, optional): The short name of the circuit.
        gmt_offset (str, optional): The GMT offset of the session.
        year (int, optional): The year of the session.
    """
    meeting_key: int
    session_key: int
    location: Optional[str] = None
    date_start: Optional[datetime] = None
    date_end: Optional[datetime] = None
    session_type: Optional[str] = None
    session_name: Optional[str] = None
    country_key: Optional[int] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    circuit_key: Optional[int] = None
    circuit_short_name: Optional[str] = None
    gmt_offset: Optional[str] = None
    year: Optional[int] = None