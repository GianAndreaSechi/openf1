import json
from openf1.api.handler import ApiHandler
from openf1.models.meeting import Meeting
from typing import List, Dict, Any
from ._base import BaseEndpoint

class MeetingsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_meetings(self, **kwargs) -> str:
        """
        Retrieves meeting data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("meetings", params=processed_params)
        
        if data_list:
            meeting_models = [Meeting(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in meeting_models])
        return "[]"
