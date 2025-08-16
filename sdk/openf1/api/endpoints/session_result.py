from openf1.api.handler import ApiHandler
from openf1.models.session_result import SessionResult
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class SessionResultEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_session_result(self, **kwargs) -> List[SessionResult]:
        """
        Retrieves session result data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("session_result", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [SessionResult(**row) for index, row in df.iterrows()]
        return []