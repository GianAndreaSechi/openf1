from openf1.api.handler import ApiHandler
from openf1.models.team_radio import TeamRadio
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class TeamRadioEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_team_radio(self, **kwargs) -> List[TeamRadio]:
        """
        Retrieves team_radio data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("team_radio", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [TeamRadio(**row) for index, row in df.iterrows()]
        return []
