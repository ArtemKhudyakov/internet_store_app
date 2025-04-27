from abc import ABC, abstractmethod
from typing import Any

# # from src.classes import Product
# if TYPE_CHECKING: from src.classes import Product


class BaseProduct(ABC):

    # def __init__(self, *args, **kwargs):
    #     pass
    @abstractmethod
    def __repr__(self) -> str:
        """Выводит информацию об объекте"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Выводит параметры объекта в строковом формате"""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Складывает какие-либо параметры класса. Параметры сложения указываются в конкретном классе"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Метод создания нового объекта класса"""
        pass


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с общими свойствами."""

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def add_product(self, product) -> None:
        """Добавление продукта в сущность"""
        pass
