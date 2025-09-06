from openf1.api.handler import ApiHandler
from ._base import BaseEndpoint
from openf1.models.team_radio import TeamRadio
from typing import List

class TeamRadioEndpoint(BaseEndpoint):
    def __init__(self, api_handler: ApiHandler):
        super().__init__(api_handler)

    def get_team_radio(self, **kwargs) -> List[TeamRadio]:
        """
        Retrieves team radio data.
        """
        processed_params = self._process_kwargs(**kwargs)
        
        data_list = self.api_handler.get("team_radio", params=processed_params)
        
        if data_list:
            return [TeamRadio(**item) for item in data_list]
        return []
