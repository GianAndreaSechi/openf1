from openf1.api.handler import ApiHandler
from openf1.models.interval import Interval
from typing import List
import pandas as pd
from ._base import BaseEndpoint

class IntervalsEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_intervals(self, **kwargs) -> List[Interval]:
        """
        Retrieves interval data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        df = self.api_handler.get("intervals", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [Interval(**row) for index, row in df.iterrows()]
        return []
