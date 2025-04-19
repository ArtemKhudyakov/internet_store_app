class MixinPrint:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(self.info())

    def info(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
