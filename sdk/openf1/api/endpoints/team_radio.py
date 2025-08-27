import json
from openf1.api.handler import ApiHandler
from openf1.models.team_radio import TeamRadio
from typing import List, Dict, Any
from ._base import BaseEndpoint

class TeamRadioEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_team_radio(self, **kwargs) -> str:
        """
        Retrieves team radio data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("team_radio", params=processed_params)
        
        if data_list:
            team_radio_models = [TeamRadio(**item) for item in data_list]
            return json.dumps([model.model_dump() for model in team_radio_models])
        return "[]"
