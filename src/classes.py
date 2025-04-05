from typing import List, Optional


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = float(price)

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть целым неотрицательным числом")
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Category:
    name: str
    description: str
    products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __repr__(self) -> str:
        return f"Category(name='{self.name}', products={len(self.products)})"


# if __name__ == "__main__":
#     category1 = Category("Electronic", "Eectronic devices")
#     product1 = Product("Laptop", "Powerful laptop", 999.99, 5)
#     product2 = Product("Phone", "Smartphone", 699.99, 10)
#     category1.products.append(product1)
#     category1.products.append(product2)
#     print(category1.products)
#     for product in category1.products:
#         print(product.name, product.description)
