from openf1.api.handler import ApiHandler
from openf1.api.endpoints.car_data import CarDataEndpoint

class OpenF1Client:
    def __init__(self):
        self.api_handler = ApiHandler()
        self.car_data = CarDataEndpoint(self.api_handler)
