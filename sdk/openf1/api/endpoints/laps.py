from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.lap import Lap
from typing import List

class LapsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_laps(self, **kwargs) -> List[Lap]:
        """
        Retrieves lap data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("laps", params=processed_params)
        
        if data_list:
            return [Lap(**item) for item in data_list]
        return []
