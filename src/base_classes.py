from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    # def __init__(self, *args, **kwargs):
    #     pass
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass
