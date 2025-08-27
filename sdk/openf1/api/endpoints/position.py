import json
from openf1.api.handler import ApiHandler
from openf1.models.position import Position
from typing import List, Dict, Any
from ._base import BaseEndpoint

class PositionEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_position(self, **kwargs) -> str:
        """
        Retrieves position data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("position", params=processed_params)
        
        if data_list:
            position_models = [Position(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in position_models])
        return "[]"
