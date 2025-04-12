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


@pytest.fixture
def list_of_products(sample_product: Product, another_product: Product) -> List[Product]:
    list_of_products = [sample_product, another_product]
    return list_of_products


@pytest.fixture
def list_of_products2() -> List[Product]:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    list_of_products = [product1, product2, product3]
    return list_of_products
