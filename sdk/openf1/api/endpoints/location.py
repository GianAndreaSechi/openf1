import json
from openf1.api.handler import ApiHandler
from openf1.models.location import Location
from typing import List, Dict, Any
from ._base import BaseEndpoint

class LocationEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_location(self, **kwargs) -> str:
        """
        Retrieves location data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("location", params=processed_params)
        
        if data_list:
            location_models = [Location(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in location_models])
        return "[]"
