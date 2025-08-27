class McpResponse:
    def __init__(self, message: str = None, data: dict = None):
        self.message = message
        self.data = data

    def to_dict(self) -> dict:
        return {
            "message": self.message, 
            "data": self.data}