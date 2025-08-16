from pydantic import BaseModel
from typing import Optional, List, Union

class SessionResult(BaseModel):
    """
    Represents the result of a session for a driver.

    Attributes:
        meeting_key (int): The key of the meeting.
        session_key (int): The key of the session.
        driver_number (int): The number of the driver.
        position (int, optional): The final position of the driver.
        number_of_laps (int, optional): The number of laps completed by the driver.
        points (float, optional): The points scored by the driver.
        dnf (bool): Whether the driver did not finish the session.
        dns (bool): Whether the driver did not start the session.
        dsq (bool): Whether the driver was disqualified from the session.
        duration (float or list[float], optional): The total duration of the driver's session.
            For races, this is a single float value. For qualifying sessions, this is a list of floats
            representing the duration of each qualifying part (Q1, Q2, Q3).
        gap_to_leader (str, float, or list[float], optional): The time gap to the leader.
            For races, this can be a float (in seconds) or a string (e.g., "+1 Lap").
            For qualifying sessions, this is a list of floats representing the gap to the leader in each part.
    """
    meeting_key: int
    session_key: int
    driver_number: int
    position: Optional[int] = None
    number_of_laps: Optional[int] = None
    points: Optional[float] = None
    dnf: bool = False
    dns: bool = False
    dsq: bool = False
    duration: Optional[Union[float, List[Optional[float]]]] = None
    gap_to_leader: Optional[Union[str, float, List[Optional[float]]]] = None