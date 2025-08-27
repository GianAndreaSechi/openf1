import json
from openf1.api.handler import ApiHandler
from openf1.models.weather import Weather
from typing import List, Dict, Any
from ._base import BaseEndpoint

class WeatherEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_weather(self, **kwargs) -> str:
        """
        Retrieves weather data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("weather", params=processed_params)
        
        if data_list:
            weather_models = [Weather(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in weather_models])
        return "[]"
