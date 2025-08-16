from openf1.api.handler import ApiHandler
from openf1.models.starting_grid import StartingGrid
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class StartingGridEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_starting_grid(self, **kwargs) -> List[StartingGrid]:
        """
        Retrieves starting grid data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("starting_grid", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [StartingGrid(**row) for index, row in df.iterrows()]
        return []