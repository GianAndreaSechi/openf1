import json
from openf1.api.handler import ApiHandler
from openf1.models.starting_grid import StartingGrid
from typing import List, Dict, Any
from ._base import BaseEndpoint

class StartingGridEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_starting_grid(self, **kwargs) -> str:
        """
        Retrieves starting grid data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("starting_grid", params=processed_params)
        
        if data_list:
            starting_grid_models = [StartingGrid(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in starting_grid_models])
        return "[]"