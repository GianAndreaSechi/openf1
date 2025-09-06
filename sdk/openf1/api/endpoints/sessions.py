from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.session import Session
from typing import List

class SessionsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_sessions(self, **kwargs) -> List[Session]:
        """
        Retrieves session data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("sessions", params=processed_params)
        
        if data_list:
            return [Session(**item) for item in data_list]
        return []
