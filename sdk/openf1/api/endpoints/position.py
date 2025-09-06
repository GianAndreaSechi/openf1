from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.position import Position
from typing import List

class PositionEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_position(self, **kwargs) -> List[Position]:
        """
        Retrieves position data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("position", params=processed_params)
        
        if data_list:
            return [Position(**item) for item in data_list]
        return []
