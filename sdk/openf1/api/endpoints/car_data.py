from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.car_data import CarData
from typing import List

class CarDataEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_car_data(self, **kwargs) -> List[CarData]:
        """
        Retrieves car data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("car_data", params=processed_params)
        
        if data_list:
            return [CarData(**item) for item in data_list]
        return []
