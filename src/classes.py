from typing import Any, Iterator, List, Optional

from src.base_classes import BaseEntity, BaseProduct
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
    def new_product(cls, data: dict, products_list: Optional[List["Product"]] = None) -> Optional["Product"]:
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
                return None
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


class Category(BaseEntity):
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

    def middle_price(self) -> float:
        mid_price = 0.0
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


class Order(BaseEntity):
    """Класс заказа с одним товаром и фиксированным продуктом"""

    _next_order_number = 1

    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")

        self._order_number = Order._next_order_number
        Order._next_order_number += 1

        self._product = product
        self._quantity = quantity
        self._total_price = product.price * quantity
        self._confirmed = False

    def __repr__(self) -> str:
        status = "подтвержден" if self._confirmed else "не подтвержден"
        return (
            f"Order(order_number={self._order_number}, "
            f"product={self._product.name}, "
            f"quantity={self._quantity}, status={status})"
        )

    def __str__(self) -> str:
        status = "подтвержден" if self._confirmed else "не подтвержден"
        return (
            f"Заказ #{self._order_number} {status}: {self._product.name}, "
            f"{self._quantity} шт. × {self._product.price} руб. = "
            f"{self._total_price:.2f} руб."
        )

    def add_product(self, additional_quantity: int) -> None:
        """Увеличивает количество товара в заказе"""
        if self._confirmed:
            raise ValueError("Нельзя изменить подтвержденный заказ")
        try:
            if additional_quantity < 0:
                raise ValueError("Добавляемое количество должно быть положительным")
            if additional_quantity == 0:
                raise ZeroQuantityProductError("Добавляемое количество товара в заказ должно быть больше ноля")
        except ValueError as ve:
            print(ve)
            additional_quantity = 0
        except ZeroQuantityProductError as zqpe:
            print(zqpe)
            additional_quantity = 0
        finally:
            self._quantity += additional_quantity
            self._total_price = self._product.price * self._quantity
            print("Операция добавления товара в заказ завершена")

    def confirm(self) -> None:
        """Подтверждение заказа - уменьшает количество товара в категории"""
        if self._confirmed:
            raise ValueError("Заказ уже подтвержден")

        if self._product.quantity < self._quantity:
            raise ValueError(
                f"Недостаточно товара '{self._product.name}' на складе. Доступно: {self._product.quantity}, "
                f"требуется: {self._quantity}"
            )

        self._product.quantity -= self._quantity
        self._confirmed = True

    def cancel(self) -> None:
        """Отмена заказа"""
        if self._confirmed:
            self._product.quantity += self._quantity

        self._confirmed = False
        self._quantity = 0
        self._total_price = 0

    @property
    def order_number(self) -> int:
        return self._order_number

    @property
    def product(self) -> str:
        return f"Продукт: {self._product.name}, цена: {self._product.price} руб. В заказе: {self._quantity} шт."

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def total_price(self) -> float:
        return self._total_price

    @property
    def is_confirmed(self) -> bool:
        return self._confirmed


# if __name__ == "__main__":
#
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1)
#     order1 = Order(product1, 2)
#
#
#     order1.add_product(2)
#
#     print(order1)
#     order1.confirm()
#     print(product1)
#
#     print (order1.order_number)
#     print(order1.product)
#     print(order1.total_price)
#     print(order1.quantity)
#     print(order1.is_confirmed)
