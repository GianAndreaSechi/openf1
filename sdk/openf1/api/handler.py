import requests
import json
from loguru import logger
from typing import Dict, List, Any

class ApiHandler:
    def __init__(self, base_url: str = "https://api.openf1.org/v1"):
        self.base_url = base_url

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            logger.info(f"Requesting URL: {response.url}")
    
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")
            return []
        except Exception as e:
            logger.error(f"An error occurred during response processing: {e}")
            return []
