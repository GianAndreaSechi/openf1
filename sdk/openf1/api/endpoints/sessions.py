from openf1.api.handler import ApiHandler
from openf1.models.session import Session
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class SessionsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_sessions(self, **kwargs) -> List[Session]:
        """
        Retrieves session data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("sessions", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [Session(**row) for index, row in df.iterrows()]
        return []
