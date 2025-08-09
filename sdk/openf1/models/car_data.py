from datetime import datetime
from pydantic import BaseModel

class CarData(BaseModel):
    meeting_key: int
    session_key: int
    driver_number: int
    date: datetime
    rpm: int | None
    speed: int | None
    n_gear: int | None
    throttle: int | None
    brake: int | None
    drs: int | None
