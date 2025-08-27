import json
from openf1.api.handler import ApiHandler
from openf1.models.interval import Interval
from typing import List, Dict, Any
from ._base import BaseEndpoint

class IntervalsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_intervals(self, **kwargs) -> str:
        """
        Retrieves interval data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("intervals", params=processed_params)
        
        if data_list:
            interval_models = [Interval(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in interval_models])
        return "[]"
