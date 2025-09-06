from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.pit import Pit
from typing import List

class PitEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_pit(self, **kwargs) -> List[Pit]:
        """
        Retrieves pit data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("pit", params=processed_params)
        
        if data_list:
            return [Pit(**item) for item in data_list]
        return []
