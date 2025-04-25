from typing import Optional

class ZeroQuantityProductError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)
