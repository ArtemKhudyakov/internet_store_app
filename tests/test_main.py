from pytest import CaptureFixture

from src.main import main_16_1


def test_main_output(capsys: CaptureFixture) -> None:
    main_16_1()

    captured = capsys.readouterr()
    output = captured.out
    expected_strings: list[str] = [
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        "180000.0",
        "5",
        "95.5",
        "S23 Ultra",
        "256",
        "Серый",
        "Iphone 15",
        "512GB, Gray space",
        "210000.0",
        "8",
        "98.2",
        "15",
        "512",
        "Gray space",
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        "31000.0",
        "14",
        "90.3",
        "Note 11",
        "1024",
        "Синий",
        "Газонная трава",
        "Элитная трава для газона",
        "500.0",
        "20",
        "Россия",
        "7 дней",
        "Зеленый",
        "Газонная трава 2",
        "Выносливая трава",
        "450.0",
        "15",
        "США",
        "5 дней",
        "Темно-зеленый",
        "2580000.0",
        "16750.0",
        "Возникла ошибка TypeError при попытке сложения",
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
        "5",
        "Возникла ошибка TypeError при добавлении не продукта",
    ]

    for expected in expected_strings:
        assert expected in output, f"Ожидаемая строка '{expected}' не найдена в выводе"
