from abc import ABC
import re

class BaseEndpoint(ABC):
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def _process_kwargs(self, **kwargs):
        """
        Processes keyword arguments to handle special operators.
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
        return processed_params
