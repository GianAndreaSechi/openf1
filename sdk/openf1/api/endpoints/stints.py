import json
from openf1.api.handler import ApiHandler
from openf1.models.stint import Stint
from typing import List, Dict, Any
from ._base import BaseEndpoint

class StintsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_stints(self, **kwargs) -> str:
        """
        Retrieves stint data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("stints", params=processed_params)
        
        if data_list:
            stint_models = [Stint(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in stint_models])
        return "[]"
