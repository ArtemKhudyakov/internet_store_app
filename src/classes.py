from typing import Iterator, List, Optional


class Product:
    # name: str
    # description: str
    # price: float
    # quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.__price = float(price)

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть целым неотрицательным числом")
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:

        summa = self.__price * self.quantity + other.__price * other.quantity
        return summa

    @classmethod
    def new_product(cls, data: dict, products_list: Optional[List["Product"]] = None) -> "Product":
        if not isinstance(data, dict):
            raise ValueError("Неверный формат")
        elif data == {} or data is None:
            raise ValueError("Продукт не может быть пустым")
        else:
            product = Product(**data)
            if products_list is None:
                return product
            else:
                for prd in products_list:
                    if prd.name.lower() == product.name.lower():
                        prd.quantity += product.quantity
                        if product.price > prd.price:
                            prd.price = product.price
                        return prd
                return product

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

    def add_product(self, product: Product) -> None:
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


# if __name__ == "__main__":
#     category1 = Category("Electronic", "Eectronic devices")
#     product1 = Product("Laptop", "Powerful laptop", 999.99, 5)
#     product2 = Product("Phone", "Smartphone", 699.99, 10)
#     category1.add_product(product1)
#     category1.add_product(product2)
#     print(category1.products)
#     for product in category1.products_list:
#         print(product.name, product.description)
#
#     print(category1.product_count)

# if __name__ == "__main__":
#     new_product = {'name': 'FreeBuds 5', 'description': 'Безпроводные наушники', 'price': 5099.45, 'quantity': 5}
#
#     product3 = Product.new_product(new_product)
#
#     print(product3.name, product3.description, product3.price, product3.quantity)
#
#     try:
#         product4 = Product.new_product(['FreeBuds 5', 'Безпроводные наушники', 5099.45, 5])
#     except Exception as e:
#         print(e)
#     try:
#         print(product4.name, product4.description, product4.price, product4.quantity)
#     except Exception as e:
#         print(e)
#
#     product3.price = 7099.45
#
#     print(product3)
#
#     product3.price = -2332.454
#     print(product3)
#
#     product3.price = 'dfd'
#     print(product3)
#
#     product3.price = 6099.45
#     print(product3)

# product_list = [Product("Телефон", "Смартфон", 599.99, 10),
#                 Product("Ноутбук", "Игровой", 999.99, 5)]
#
#
# product3 = Product.new_product({'name': 'FreeBuds 5', 'description': 'Безпроводные наушники',
#                                                  'price': 5099.45, 'quantity': 5}, product_list)
#
# print(product3.price)
#
# product_list = [Product("Телефон", "Смартфон", 599.99, 10),
#                 Product("Ноутбук", "Игровой", 999.99, 5)]
#
#
# product3 = Product.new_product({'name': "Ноутбук", 'description': "Игровой",
#                                                  'price': 10, 'quantity': 20}, product_list)
#
# print(product3.price, product3.quantity)
#
# for prod in product_list:
#     print(prod)
#
# if __name__ == "__main__":
#     initial_product_list1 = [Product("Телефон", "Смартфон", 599.99, 10), Product("Ноутбук", "Игровой", 999.99, 5)]
#
#     category1 = Category("Electronics", "Electronic devices", products=initial_product_list1)
#
#     product3 = Product.new_product({"name": "Ноутбук", "description": "Игровой", "price": 10, "quantity": 20})
#
#     product4 = Product.new_product(
#         {"name": "FreeBuds 5", "description": "Безпроводные наушники", "price": 5099.45, "quantity": 5}
#     )
#
#     category1.add_product(product3)
#     category1.add_product(product4)
#
#     initial_product_list2 = [
#         Product("Товар 1", "Описание товара 1", 100, 1),
#         Product("Товар 2", "Описание товара 2", 200, 2),
#     ]
#
#     category2 = Category("Тест", "Тестовая категоря", products=initial_product_list2)
#
#     test_product = Product.new_product(
#         {"name": "Товар 3", "description": "Описание товара 3", "price": 300, "quantity": 3}
#     )
#     category2.add_product(test_product)
#
#     for prod in category1.products_list:
#         print(prod)
#
#     print("####")
#
#     print(category1)
#
#     print(category2)
#
#     print("###")
#
#     for prod in CatIter(category1):
#         print(prod)
#
#     print("\nповтор\n")
#     iter_cat1 = CatIter(category1)
#     print(next(iter_cat1))
#     print(next(iter_cat1))
#     print(next(iter_cat1))
#
#     print("###")
#
#     for prod in CatIter(category2):
#         print(prod)
