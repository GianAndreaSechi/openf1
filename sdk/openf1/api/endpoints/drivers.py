from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.driver import Driver
from typing import List

class DriversEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_drivers(self, **kwargs) -> List[Driver]:
        """
        Retrieves driver data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("drivers", params=processed_params)
        
        if data_list:
            return [Driver(**item) for item in data_list]
        return []
