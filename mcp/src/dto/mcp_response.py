from pydantic import BaseModel
from typing import List, Dict, Any

class McpResponse(BaseModel):
    message: str
    data: List[Dict[str, Any]]

    def to_dict(self) -> dict:
        return {
            "message": self.message, 
            "data": self.data
            }