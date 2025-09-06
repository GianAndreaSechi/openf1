from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.overtake import Overtake
from typing import List

class OvertakesEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_overtakes(self, **kwargs) -> List[Overtake]:
        """
        Retrieves overtake data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("overtakes", params=processed_params)
        
        if data_list:
            return [Overtake(**item) for item in data_list]
        return []
