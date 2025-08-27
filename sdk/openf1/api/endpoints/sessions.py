import json
from openf1.api.handler import ApiHandler
from openf1.models.session import Session
from typing import List, Dict, Any
from ._base import BaseEndpoint

class SessionsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_sessions(self, **kwargs) -> str:
        """
        Retrieves session data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("sessions", params=processed_params)
        
        if data_list:
            session_models = [Session(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in session_models])
        return "[]"
