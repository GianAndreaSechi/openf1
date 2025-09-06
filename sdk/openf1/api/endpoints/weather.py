from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.weather import Weather
from typing import List

class WeatherEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_weather(self, **kwargs) -> List[Weather]:
        """
        Retrieves weather data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("weather", params=processed_params)
        
        if data_list:
            return [Weather(**item) for item in data_list]
        return []
