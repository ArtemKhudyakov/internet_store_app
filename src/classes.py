from typing import Any, Iterator, List, Optional

from src.base_classes import BaseProduct
from src.exceptions import ZeroQuantityProductError
from src.mixin_classes import MixinPrint


class Product(BaseProduct, MixinPrint):
    # name: str
    # description: str
    # price: float
    # quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:

        self.name = name
        self.description = description

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.__price = float(price)

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть целым не отрицательным числом")
        elif quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(other) is Product:
            summa = self.__price * self.quantity + other.__price * other.quantity
            return summa
        else:
            raise TypeError("Неверный тип данных")

    @classmethod
    def new_product(cls, data: dict, products_list: Optional[List["Product"]] = None) -> "Product":
        if not isinstance(data, dict):
            raise ValueError("Неверный формат")
        elif data == {} or data is None:
            raise ValueError("Продукт не может быть пустым")
        else:

            try:
                if not data["quantity"]:
                    raise ZeroQuantityProductError("Нельзя создать продукт с нулевым количеством")
            except ZeroQuantityProductError as zqpe:
                print(zqpe)
            else:
                product = Product(**data)
                if products_list is None:
                    print("Продукт успешно создан")
                    return product
                else:
                    for prd in products_list:
                        if prd.name.lower() == product.name.lower():
                            prd.quantity += product.quantity
                            if product.price > prd.price:
                                prd.price = product.price
                            print("Продукт уже находится в списке товаров, данные по продукту обновлены")
                            return prd
                    print("Продукт успешно создан")
                    return product
            finally:
                print("Обработка операции создания продукта завершена")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if not isinstance(new_price, (int, float)):
            print("Неверный формат ввода")
            return
        elif new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if new_price < self.__price:
                conformation = (
                    input(
                        """Подтвердите понижение цены! y - да
                           n - нет
                           ----->"""
                    )
                ).lower()
                if conformation == "y":
                    self.__price = new_price
                else:
                    return
            else:
                self.__price = new_price


class Category:
    # name: str
    # description: str
    # products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)
        self.quantity_of_items_in_category = sum([product.quantity for product in self.__products])

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.quantity_of_items_in_category} шт."

    def __repr__(self) -> str:
        return f"Category(name='{self.name}', products={len(self.products_list)})"

    @property
    def products_list(self) -> List[Product]:
        return self.__products

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product: Product | Any) -> None:
        if isinstance(product, Product) or issubclass(product.__class__, Product):
            name_list = [prd.name for prd in self.__products]
            if product.name in name_list:
                for prd in self.__products:
                    if prd.name == product.name:
                        prd.quantity += product.quantity
                        self.quantity_of_items_in_category += product.quantity
                        if product.price > prd.price:
                            prd.price = product.price
            else:
                self.__products.append(product)
                Category.product_count += 1
                self.quantity_of_items_in_category += product.quantity
        else:
            raise TypeError("Неверный тип данных")

    def middle_price(self)->float:
        mid_price = 0
        try:
            sum_prise_of_all_products_in_category = sum(
                product.price * product.quantity for product in self.__products
            )
            mid_price = sum_prise_of_all_products_in_category / self.quantity_of_items_in_category
        except ZeroDivisionError:
            mid_price = 0
        finally:
            return round(mid_price, 2)


class CatIter:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Product") -> float:
        if type(other) is Smartphone:
            summa = self.price * self.quantity + other.price * other.quantity
            return summa
        else:
            raise TypeError("Неверный тип данных")


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> float:
        if type(other) is LawnGrass:
            summa = self.price * self.quantity + other.price * other.quantity
            return summa
        else:
            raise TypeError("Неверный тип данных")
