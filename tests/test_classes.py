import unittest
from typing import Any, List, Optional, Type
from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from src.classes import Category, CatIter, LawnGrass, Product, Smartphone


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
        with pytest.raises(ValueError):
            product = Product("Книга", "Интересная книга", 19.99, 0)
            product

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

        self.assertEqual(len(category.products_list), 2)
        self.assertIsInstance(category.products_list[0], Product)
        self.assertEqual(category.products_list[1].name, "Мышь")

    def test_add_product_to_category(self) -> None:
        """Тест добавления продукта в категорию"""
        category = Category("Одежда", "Модная одежда")
        product = Product("Футболка", "Хлопковая футболка", 29.99, 50)

        category.add_product(product)
        self.assertEqual(len(category.products_list), 1)
        self.assertEqual(category.products_list[0].name, "Футболка")

    def test_category_with_none_products(self) -> None:
        """Тест создания категории с products=None (должен создаваться пустой список)"""
        category = Category("Мебель", "Домашняя мебель", None)
        self.assertEqual(len(category.products), 0)


@pytest.mark.parametrize(
    "name, description, price, quantity, expected_error",
    [
        # Корректные данные (без ошибки)
        ("Ноутбук", "Мощный ноутбук", 999.99, 5, None),
        ("Книга", "Интересная книга", 19.99, 0, ValueError),  # Количество = 0 недопустимо
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
    assert len(category.products_list) == 1
    assert category.products_list[0] == sample_product


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
    empty_category.add_product(sample_product)
    assert len(empty_category.products_list) == 1
    assert empty_category.products_list[0] == sample_product


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


def test_getter_products_list(sample_product: Product, another_product: Product) -> None:
    """Тест получения списка товаров"""
    cat1 = Category("тест", "тестирование", [sample_product, another_product])
    assert len(cat1.products_list) == 2
    assert cat1.products_list[0] == sample_product
    assert cat1.products_list[1] == another_product


def test_add_product(sample_product: Product, another_product: Product) -> None:
    """Тест добавления товара в категорию"""
    cat1 = Category("тест", "тестирование", [sample_product])
    assert len(cat1.products_list) == 1
    cat1.add_product(another_product)
    assert len(cat1.products_list) == 2
    assert cat1.products_list[1] == another_product


def test_getter_products(sample_category: Category) -> None:
    """Тест получения строки из списка товаров"""
    assert sample_category.products == "Телефон, 599.99 руб. Остаток: 10 шт.\n"


@pytest.mark.parametrize(
    "product, expected",
    [
        (
            {"name": "FreeBuds 5", "description": "Безпроводные наушники", "price": 5099.45, "quantity": 5},
            "Безпроводные наушники",
        ),
        ({}, ValueError),
        (None, ValueError),
        ([], ValueError),
    ],
)
def test_new_product(product: dict[str, Any], expected: Any) -> None:
    """Тест создания нового товара"""
    if expected != ValueError:
        product1 = Product.new_product(product)
        if product1 is not None:
            assert product1.description == expected
    else:
        with pytest.raises(expected):
            Product.new_product(product)


@pytest.mark.parametrize(
    "new_price, final_price", [("Тысяча", 599.99), (-1000, 599.99), (0, 599.99), (1000.00, 1000.00)]
)
def test_price_setter(sample_product: Product, new_price: Any, final_price: float) -> None:
    """Тест сеттера цены, тестирование возврата правильной цены при установке валидных и невалидных цен"""
    sample_product.price = new_price
    assert sample_product.price == final_price


@pytest.mark.parametrize(
    "new_price, message",
    [
        (0, "Цена не должна быть нулевая или отрицательная"),
        ("qwerty", "Неверный формат ввода"),
        (-1000, "Цена не должна быть нулевая или отрицательная"),
    ],
)
def test_price_setter_invalid_price(
    capsys: pytest.CaptureFixture[str], sample_product: Product, new_price: float, message: str
) -> None:
    """Тест сеттера цены, тестирование вывода сообщения при установке невалидных цен"""
    sample_product.price = new_price
    assert capsys.readouterr().out.strip().split("\n")[-1] == message


@pytest.mark.parametrize(
    "new_price, conformation, final_price", [(5000, "y", 5000), (500, "y", 500), (400, "n", 599.99)]
)
def test_price_setter_lower_price(
    sample_product: Product, new_price: float, conformation: str, final_price: float
) -> None:
    """Тест сеттера цены, тестирование подтверждения установки цены ниже существующей"""
    with patch("builtins.input", return_value=conformation):
        sample_product.price = new_price
        assert sample_product.price == final_price


@pytest.mark.parametrize(
    "new_product, price_expected, quantity_expected",
    [
        ({"name": "Ноутбук", "description": "Игровой", "price": 10, "quantity": 20}, 999.99, 25),
        ({"name": "Ноутбук", "description": "Игровой", "price": 10000, "quantity": 1}, 10000.00, 6),
    ],
)
def test_new_product_in_list(
    list_of_products: list[Product], new_product: dict[Any, Any], price_expected: float, quantity_expected: int
) -> None:
    """Тест добавления в список продукта с таким же именем"""
    product_list = list_of_products
    product3 = Product.new_product(new_product, product_list)
    if product3 is not None:
        assert product3.quantity == quantity_expected
        assert product3.price == price_expected


@pytest.mark.parametrize(
    "new_product, price_expected, quantity_expected",
    [
        ({"name": "Ноутбук", "description": "Игровой", "price": 10, "quantity": 20}, 10, 20),
        ({"name": "Ноутбук", "description": "Игровой", "price": 10000, "quantity": 1}, 10000.00, 1),
    ],
)
def test_new_product_in_list_empty(new_product: dict[Any, Any], price_expected: float, quantity_expected: int) -> None:
    """Тест на добавление продукта в пустой список"""
    product_list1 = None
    product1 = Product.new_product(new_product, product_list1)
    if product1 is not None:
        assert product1.quantity == quantity_expected
        assert product1.price == price_expected
    product_list2: list = []
    product2 = Product.new_product(new_product, product_list2)
    if product2 is not None:
        assert product2.quantity == quantity_expected
        assert product2.price == price_expected


@pytest.mark.parametrize(
    "product, expected_str",
    [
        (
            {"name": "Ноутбук", "description": "Игровой", "price": 10, "quantity": 20},
            "Ноутбук, 10.0 руб. Остаток: 20 шт.",
        ),
        (
            {"name": "FreeBuds 5", "description": "Безпроводные наушники", "price": 5099.45, "quantity": 5},
            "FreeBuds 5, 5099.45 руб. Остаток: 5 шт.",
        ),
    ],
)
def test_str_view_of_product(product: dict, expected_str: str) -> None:
    """Тест строкового отображения продукта"""
    prd = Product.new_product(product)
    assert str(prd) == expected_str


@pytest.mark.parametrize(
    "category, expected_str",
    [
        (
            Category(
                "Electronics",
                "Electronic devices",
                [Product("Телефон", "Смартфон", 599.99, 10), Product("Ноутбук", "Игровой", 999.99, 5)],
            ),
            "Electronics, количество продуктов: 15 шт.",
        )
    ],
)
def test_str_view_of_category(category: dict, expected_str: str) -> None:
    """Тест строкового отображения категории"""
    cat = category
    assert str(cat) == expected_str


def test_count_items_in_category(sample_category: Category) -> None:
    """Тест на объединение одинаковых товаров при добавлении в категорию"""
    cat = sample_category
    assert cat.quantity_of_items_in_category == 10
    new_prod1 = Product("Телефон", "Смартфон", 799.99, 20)
    cat.add_product(new_prod1)
    assert len(cat.products_list) == 1
    assert cat.quantity_of_items_in_category == 30
    assert cat.products_list[0].price == 799.99
    new_prod2 = Product.new_product(
        {"name": "FreeBuds 5", "description": "Безпроводные наушники", "price": 5099.45, "quantity": 5}
    )
    cat.add_product(new_prod2)
    assert len(cat.products_list) == 2
    assert cat.quantity_of_items_in_category == 35
    assert cat.products_list[1].price == 5099.45


def test_sum_of_whole_cost_of_two_products(list_of_products2: List[Product]) -> None:
    """Тест суммирования продуктов"""
    assert list_of_products2[0] + list_of_products2[1] == 2580000
    assert list_of_products2[1] + list_of_products2[2] == 2114000
    assert list_of_products2[2] + list_of_products2[0] == 1334000


def test_iterator_with_1_product(sample_category: Category) -> None:
    """Тест итератора на категории с одним товаром"""
    iter_1 = CatIter(sample_category)
    assert iter_1.index == 0
    assert str(next(iter_1)) == str(Product("Телефон", "Смартфон", 599.99, 10))
    assert iter_1.index == 1
    with pytest.raises(StopIteration):
        next(iter_1)


def test_iterator_with_2_products(sample_category: Category, another_product: Product) -> None:
    """Тест итератора после добавления в категорию нового товара"""
    cat = sample_category
    cat.add_product(another_product)
    iter_1 = CatIter(sample_category)
    next(iter_1)
    assert str(next(iter_1)) == str(another_product)
    with pytest.raises(StopIteration):
        next(iter_1)


def test_smartphone_creation(smartphone1: Smartphone) -> None:
    smartphone = smartphone1
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.memory == 256
    assert smartphone.model == "S23 Ultra"
    assert smartphone.color == "Серый"


def test_lowngrass_creation(lawn_grass1: LawnGrass) -> None:
    lawn_grass = lawn_grass1
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_addition(
    lawn_grass1: LawnGrass, smartphone1: Smartphone, lawn_grass2: LawnGrass, smartphone2: Smartphone
) -> None:
    smartphone_1 = smartphone1
    lawn_grass_1 = lawn_grass1
    smartphone_2 = smartphone2
    lawn_grass_2 = lawn_grass2
    with pytest.raises(TypeError):
        assert smartphone_1 + lawn_grass_2
    with pytest.raises(TypeError):
        assert lawn_grass_1 + smartphone_2
    assert smartphone_1 + smartphone_2 == 2580000
    assert lawn_grass_1 + lawn_grass_2 == 16750


def test_add_to_category(
    lawn_grass1: LawnGrass, smartphone1: Smartphone, lawn_grass2: LawnGrass, smartphone2: Smartphone
) -> None:
    smartphone_1 = smartphone1
    lawn_grass_1 = lawn_grass1
    smartphone_2 = smartphone2
    lawn_grass_2 = lawn_grass2
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone_1])
    assert category_smartphones.quantity_of_items_in_category == 5
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [lawn_grass_1])
    category_smartphones.add_product(smartphone_2)
    assert category_smartphones.quantity_of_items_in_category == 13
    category_grass.add_product(lawn_grass_2)
    assert category_grass.quantity_of_items_in_category == 35
    with pytest.raises(TypeError):
        category_grass.add_product("Not a product")


def test_middle_price_of_category(smartphone1: Smartphone, smartphone2: Smartphone, empty_category: Category) -> None:
    category1 = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    assert round(category1.middle_price(), 2) == 198461.54
    assert empty_category.middle_price() == 0


def test_new_product_zero_quantity(capsys: CaptureFixture) -> None:
    product1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 170000,
            "quantity": 0,
        }
    )
    assert product1 is None
    captured = capsys.readouterr()
    output = captured.out.splitlines()
    assert output[-2].strip() == "Нельзя создать продукт с нулевым количеством"
    assert output[-1].strip() == "Обработка операции создания продукта завершена"


def test_new_product_messages(capsys: CaptureFixture) -> None:
    product1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 170000,
            "quantity": 5,
        }
    )
    assert product1 is not None
    captured = capsys.readouterr()
    output = captured.out.splitlines()
    assert output[-2].strip() == "Продукт успешно создан"
    assert output[-1].strip() == "Обработка операции создания продукта завершена"
    list1 = [product1]
    product2 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 120000,
            "quantity": 2,
        },
        list1,
    )
    if product2 is not None:
        assert product2.price == 170000
    captured = capsys.readouterr()
    output = captured.out.splitlines()
    assert output[-2].strip() == "Продукт уже находится в списке товаров, данные по продукту обновлены"
    assert output[-1].strip() == "Обработка операции создания продукта завершена"
