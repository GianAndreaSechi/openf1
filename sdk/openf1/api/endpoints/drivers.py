from openf1.api.handler import ApiHandler
from openf1.models.driver import Driver
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class DriversEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_drivers(self, **kwargs) -> List[Driver]:
        """
        Retrieves driver data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("drivers", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [Driver(**row) for index, row in df.iterrows()]
        return []
