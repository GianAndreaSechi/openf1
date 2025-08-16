from openf1.api.handler import ApiHandler
from openf1.api.endpoints.car_data import CarDataEndpoint
from openf1.api.endpoints.drivers import DriversEndpoint
from openf1.api.endpoints.intervals import IntervalsEndpoint
from openf1.api.endpoints.laps import LapsEndpoint
from openf1.api.endpoints.location import LocationEndpoint
from openf1.api.endpoints.meetings import MeetingsEndpoint
from openf1.api.endpoints.overtakes import OvertakesEndpoint
from openf1.api.endpoints.pit import PitEndpoint
from openf1.api.endpoints.position import PositionEndpoint
from openf1.api.endpoints.race_control import RaceControlEndpoint
from openf1.api.endpoints.sessions import SessionsEndpoint
from openf1.api.endpoints.stints import StintsEndpoint
from openf1.api.endpoints.team_radio import TeamRadioEndpoint
from openf1.api.endpoints.weather import WeatherEndpoint
from openf1.api.endpoints.session_result import SessionResultEndpoint
from openf1.api.endpoints.starting_grid import StartingGridEndpoint

class OpenF1Client:
    def __init__(self):
        self.api_handler = ApiHandler()
        self.car_data = CarDataEndpoint(self.api_handler)
        self.drivers = DriversEndpoint(self.api_handler)
        self.intervals = IntervalsEndpoint(self.api_handler)
        self.laps = LapsEndpoint(self.api_handler)
        self.location = LocationEndpoint(self.api_handler)
        self.meetings = MeetingsEndpoint(self.api_handler)
        self.overtakes = OvertakesEndpoint(self.api_handler)
        self.pit = PitEndpoint(self.api_handler)
        self.position = PositionEndpoint(self.api_handler)
        self.race_control = RaceControlEndpoint(self.api_handler)
        self.sessions = SessionsEndpoint(self.api_handler)
        self.stints = StintsEndpoint(self.api_handler)
        self.team_radio = TeamRadioEndpoint(self.api_handler)
        self.weather = WeatherEndpoint(self.api_handler)
        self.session_result = SessionResultEndpoint(self.api_handler)
        self.starting_grid = StartingGridEndpoint(self.api_handler)