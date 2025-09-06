from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.meeting import Meeting
from typing import List

class MeetingsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_meetings(self, **kwargs) -> List[Meeting]:
        """
        Retrieves meeting data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("meetings", params=processed_params)
        
        if data_list:
            return [Meeting(**item) for item in data_list]
        return []
