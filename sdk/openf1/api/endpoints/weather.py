from openf1.api.handler import ApiHandler
from openf1.models.weather import Weather
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class WeatherEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_weather(self, **kwargs) -> List[Weather]:
        """
        Retrieves weather data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("weather", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [Weather(**row) for index, row in df.iterrows()]
        return []
