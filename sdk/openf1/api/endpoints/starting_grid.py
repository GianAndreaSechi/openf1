from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.starting_grid import StartingGrid
from typing import List

class StartingGridEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_starting_grid(self, **kwargs) -> List[StartingGrid]:
        """
        Retrieves starting grid data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("starting_grid", params=processed_params)
        
        if data_list:
            return [StartingGrid(**item) for item in data_list]
        return []