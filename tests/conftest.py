from typing import Any, Dict, List

import pytest

from src.classes import Category, Product


@pytest.fixture
def sample_product() -> Product:
    """Фикстура: создаёт тестовый продукт."""
    return Product("Телефон", "Смартфон", 599.99, 10)


@pytest.fixture
def empty_category() -> Category:
    """Фикстура: создаёт пустую категорию."""
    return Category("Книги", "Литература")


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    """Фикстура: создает тестовую категорию с одним продуктом"""
    return Category("Электроника", "Гаджеты", [sample_product])


@pytest.fixture
def another_product() -> Product:
    """Фикстура: ещё один тестовый продукт."""
    return Product("Ноутбук", "Игровой", 999.99, 5)


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Фикстура: сбрасывает счётчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def test_data_valid() -> List[Dict[str, Any]]:
    test_data_valid = [
        {
            "name": "Тест",
            "description": "Описание",
            "products": [{"name": "Товар", "description": "Описание", "price": 100, "quantity": 5}],
        }
    ]
    return test_data_valid


@pytest.fixture
def test_data_invalid() -> List[Dict[str, Any]]:
    test_data_invalid = [
        {"name": "Некорректная категория", "description": "Описание", "products": [{"invalid": "data"}]}
    ]
    return test_data_invalid


@pytest.fixture
def test_data_multiple_categories() -> List[Dict[str, Any]]:
    test_data_multiple_categories = [
        {
            "name": "Категория 1",
            "description": "Описание 1",
            "products": [{"name": "Товар 1", "description": "Описание товара 1", "price": 100, "quantity": 1}],
        },
        {
            "name": "Категория 2",
            "description": "Описание 2",
            "products": [{"name": "Товар 2", "description": "Описание товара 2", "price": 200, "quantity": 2}],
        },
    ]
    return test_data_multiple_categories
