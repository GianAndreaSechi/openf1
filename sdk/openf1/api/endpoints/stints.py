from openf1.api.handler import ApiHandler
from openf1.models.stint import Stint
from typing import List
import re
import pandas as pd

class StintsEndpoint:
    def __init__(self, api_handler: ApiHandler):
        self.api_handler = api_handler

    def get_stints(self, **kwargs) -> List[Stint]:
        """
        Retrieves stint data.
        """
        processed_params = {}
        for key, value in kwargs.items():
            if isinstance(value, str) and any(op in value for op in ['>=', '<=', '>', '<']):
                operator_match = re.search(r'(>=|<=|>|<)', value)
                if operator_match:
                    operator = operator_match.group(1)
                    numeric_value = value.replace(operator, '')
                    processed_params[f"{key}{operator}{numeric_value}"] = ''
                else:
                    processed_params[key] = value
            else:
                processed_params[key] = value
        
        df = self.api_handler.get("stints", params=processed_params)
        
        if not df.empty:
            # Replace NaN with None for Pydantic compatibility
            df = df.where(pd.notnull(df), None)
            return [Stint(**row) for index, row in df.iterrows()]
        return []
