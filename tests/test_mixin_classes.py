from pytest import CaptureFixture

from src.classes import Product


def test_mixin_print_work(capsys: CaptureFixture) -> None:
    """Тест работы класса MixinPrint"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product1
    captured = capsys.readouterr()
    output = captured.out
    assert output.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
