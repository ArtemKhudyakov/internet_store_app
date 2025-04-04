import unittest
from typing import Any, List, Optional, Type

import pytest

from src.classes import Category, Product


class TestProduct(unittest.TestCase):
    def test_product_creation(self) -> None:
        """Тест создания объекта Product и проверки атрибутов"""
        product = Product("Телефон", "Смартфон", 599.99, 10)

        self.assertEqual(product.name, "Телефон")
        self.assertEqual(product.description, "Смартфон")
        self.assertEqual(product.price, 599.99)
        self.assertEqual(product.quantity, 10)

    def test_product_zero_quantity(self) -> None:
        """Тест создания продукта с нулевым количеством"""
        product = Product("Книга", "Интересная книга", 19.99, 0)
        self.assertEqual(product.quantity, 0)

    def test_product_negative_price(self) -> None:
        """Тест создания продукта с отрицательной ценой (должна вызывать ошибку)"""
        with self.assertRaises(ValueError):
            Product("Товар", "Описание", -100.0, 5)


class TestCategory(unittest.TestCase):
    def test_category_creation(self) -> None:
        """Тест создания категории с пустым списком продуктов"""
        category = Category("Электроника", "Гаджеты и устройства")

        self.assertEqual(category.name, "Электроника")
        self.assertEqual(category.description, "Гаджеты и устройства")
        self.assertEqual(len(category.products), 0)

    def test_category_with_products(self) -> None:
        """Тест создания категории с предопределенным списком продуктов"""
        products = [Product("Ноутбук", "Мощный ноутбук", 999.99, 5), Product("Мышь", "Беспроводная мышь", 49.99, 20)]
        category = Category("Компьютеры", "Компьютерная техника", products)

        self.assertEqual(len(category.products), 2)
        self.assertIsInstance(category.products[0], Product)
        self.assertEqual(category.products[1].name, "Мышь")

    def test_add_product_to_category(self) -> None:
        """Тест добавления продукта в категорию"""
        category = Category("Одежда", "Модная одежда")
        product = Product("Футболка", "Хлопковая футболка", 29.99, 50)

        category.products.append(product)
        self.assertEqual(len(category.products), 1)
        self.assertEqual(category.products[0].name, "Футболка")

    def test_category_with_none_products(self) -> None:
        """Тест создания категории с products=None (должен создаваться пустой список)"""
        category = Category("Мебель", "Домашняя мебель", None)
        self.assertEqual(len(category.products), 0)


@pytest.mark.parametrize(
    "name, description, price, quantity, expected_error",
    [
        # Корректные данные (без ошибки)
        ("Ноутбук", "Мощный ноутбук", 999.99, 5, None),
        ("Книга", "Интересная книга", 19.99, 0, None),  # Количество = 0 допустимо
        # Неправильная цена (должен вызывать `ValueError`)
        ("Товар", "Описание", -100.0, 5, ValueError),
        ("Товар", "Описание", "сто", 5, ValueError),  # Строка вместо числа
        # Неправильное количество (должен вызывать `ValueError`)
        ("Товар", "Описание", 100.0, -5, ValueError),
        ("Товар", "Описание", 100.0, 5.5, ValueError),  # `float` вместо `int`
    ],
)
def test_product_validation(
    name: str,
    description: str,
    price: Any,
    quantity: Any,
    expected_error: Optional[Type[Exception]],
) -> None:
    """Тестирует валидацию в классе `Product`."""
    if expected_error:
        with pytest.raises(expected_error):
            Product(name, description, price, quantity)
    else:
        product = Product(name, description, price, quantity)
        assert product.name == name
        assert product.description == description
        assert product.price == float(price)
        assert product.quantity == quantity


def test_category_initialization(sample_product: Product) -> None:
    """Тест инициализации категории с продуктами."""
    category = Category("Электроника", "Гаджеты", [sample_product])
    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert len(category.products) == 1
    assert category.products[0] == sample_product


def test_empty_category(empty_category: Category) -> None:
    """Тест пустой категории."""
    assert empty_category.name == "Книги"
    assert empty_category.description == "Литература"
    assert len(empty_category.products) == 0


def test_add_product_to_category(
    empty_category: Category,
    sample_product: Product,
) -> None:
    """Тест добавления продукта в категорию."""
    empty_category.products.append(sample_product)
    assert len(empty_category.products) == 1
    assert empty_category.products[0] == sample_product


def test_category_with_none_products() -> None:
    """Тест создания категории с `products=None`."""
    category = Category("Мебель", "Домашняя мебель", None)
    assert len(category.products) == 0


# Тесты для `__repr__`
def test_product_repr(sample_product: Product) -> None:
    """Тест строкового представления `Product`."""
    assert repr(sample_product) == "Product(name='Телефон', price=599.99, quantity=10)"


def test_category_repr(sample_category: Category) -> None:
    """Тест строкового представления `Category`."""
    assert repr(sample_category) == "Category(name='Электроника', products=1)"


@pytest.mark.parametrize(
    "products_list, expected_products_count",
    [
        ([], 0),  # Пустой список товаров
        (["p1"], 1),  # 1 товар
        (["p1", "p2", "p3"], 3),  # 3 товара
    ],
)
def test_category_products_counter(
    sample_product: Product,
    products_list: List[str],
    expected_products_count: int,
) -> None:
    """
    Тест подсчёта общего количества товаров (products_count).
    Передаём mock-товары (просто строки для упрощения).
    """
    # Подменяем фиктивные товары на реальные (для репрезентативности)
    real_products = [sample_product] * len(products_list)

    category = Category("Тест", "Тестовая категория", real_products)
    assert category.name == "Тест"
    assert Category.product_count == expected_products_count


# Тест для categories_count
def test_categories_counter(empty_category: Category) -> None:
    """Тест подсчёта количества категорий."""
    assert Category.category_count == 1  # empty_category создана

    # Создаём ещё одну
    Category("Электроника", "Гаджеты")
    assert Category.category_count == 2


# Комплексный тест
def test_multiple_categories_and_products(sample_product: Product, another_product: Product) -> None:
    """Тест: несколько категорий с товарами."""
    # Создаём 2 категории с товарами
    cat1 = Category("Электроника", "Гаджеты", [sample_product, another_product])
    cat2 = Category("Одежда", "Модная одежда", [sample_product])

    assert cat1.description == "Гаджеты"
    assert cat2.name == "Одежда"
    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 + 1 товар
