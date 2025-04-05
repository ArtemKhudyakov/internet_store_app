from typing import Any, Dict, List

from src.classes import Category, Product
from src.data_reader import read_json


def create_objects(file_name: str = "products.json") -> List[Category]:
    data: List[Dict[str, Any]] = read_json(file_name)
    categories: List[Category] = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    objects = create_objects("products.json")
    print(objects)
    print(objects[0].name)
    print(objects[0].description)
    print(objects[0].products)

    print(objects[1].name)
    print(objects[1].description)
    print(objects[1].products)
    for product in objects[0].products:
        print(
            f"\nНаименование: {product.name}\nОписание: {product.description}"
            f"\nЦена: {product.price}\nВ наличии: {product.quantity}"
        )

    for product in objects[1].products:
        print(
            f"\nНаименование: {product.name}\nОписание: {product.description}"
            f"\nЦена: {product.price}\nВ наличии: {product.quantity}"
        )

    print(objects[0].product_count)
    print(objects[1].product_count)

    print(objects[0].category_count)
    print(objects[1].category_count)
