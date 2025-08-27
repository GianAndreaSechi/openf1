import json
from openf1.api.handler import ApiHandler
from openf1.models.car_data import CarData
from typing import List, Dict, Any
from ._base import BaseEndpoint

class CarDataEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_car_data(self, **kwargs) -> str:
        """
        Retrieves car data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("car_data", params=processed_params)
        
        if data_list:
            car_data_models = [CarData(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in car_data_models])
        return "[]"
