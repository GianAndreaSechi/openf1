from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.interval import Interval
from typing import List

class IntervalsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_intervals(self, **kwargs) -> List[Interval]:
        """
        Retrieves interval data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("intervals", params=processed_params)
        
        if data_list:
            return [Interval(**item) for item in data_list]
        return []
