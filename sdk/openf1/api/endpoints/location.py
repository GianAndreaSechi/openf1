from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.location import Location
from typing import List

class LocationEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_location(self, **kwargs) -> List[Location]:
        """
        Retrieves location data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("location", params=processed_params)
        
        if data_list:
            return [Location(**item) for item in data_list]
        return []
