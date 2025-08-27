import json
from openf1.api.handler import ApiHandler
from openf1.models.pit import Pit
from typing import List, Dict, Any
from ._base import BaseEndpoint

class PitEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_pit(self, **kwargs) -> str:
        """
        Retrieves pit data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("pit", params=processed_params)
        
        if data_list:
            pit_models = [Pit(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in pit_models])
        return "[]"
