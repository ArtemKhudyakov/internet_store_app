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
