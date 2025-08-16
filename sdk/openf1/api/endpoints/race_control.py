from openf1.api.handler import ApiHandler
from openf1.models.race_control import RaceControl
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class RaceControlEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_race_control_messages(self, **kwargs) -> List[RaceControl]:
        """
        Retrieves race_control data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("race_control", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [RaceControl(**row) for index, row in df.iterrows()]
        return []
