from pytest import CaptureFixture

# from src.main import main_16_1
# from src.main import main_16_2
from src.main import main_17_1


def test_main_output(capsys: CaptureFixture) -> None:
    main_17_1()

    captured = capsys.readouterr()
    output = captured.out.splitlines()
    expected_strings: list[str] = [
        "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством",
        "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)",
        "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)",
        "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)",
        "111629.63",
        "0",
    ]

    assert expected_strings[0] == output[0].strip()
    assert expected_strings[1] == output[1].strip()
    assert expected_strings[2] == output[2].strip()
    assert expected_strings[3] == output[3].strip()
    assert expected_strings[4] == output[4].strip()
    assert expected_strings[5] == output[5].strip()


# def test_main_output(capsys: CaptureFixture) -> None:
#     main_16_2()
#
#     captured = capsys.readouterr()
#     output = captured.out
#     expected_strings: list[str] = [
#         "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)",
#         "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)",
#         "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)",
#         "Samsung Galaxy S23 Ultra",
#         "256GB, Серый цвет, 200MP камера",
#         "180000.0",
#         "5",
#         "Iphone 15",
#         "512GB, Gray space",
#         "210000.0",
#         "8",
#         "Xiaomi Redmi Note 11",
#         "1024GB, Синий",
#         "31000.0",
#         "14",
#         "True",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         "146",
#         "1",
#         "3",
#         'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)',
#         "Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#         "42",
#         '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.',
#         "",
#         "2",
#         "4",
#     ]
#
#     for expected in expected_strings:
#         assert expected in output, f"Ожидаемая строка '{expected}' не найдена в выводе"


# def test_main_output(capsys: CaptureFixture) -> None:
#     main_16_1()
#
#     captured = capsys.readouterr()
#     output = captured.out
#     expected_strings: list[str] = [
#         "Samsung Galaxy S23 Ultra",
#         "256GB, Серый цвет, 200MP камера",
#         "180000.0",
#         "5",
#         "95.5",
#         "S23 Ultra",
#         "256",
#         "Серый",
#         "Iphone 15",
#         "512GB, Gray space",
#         "210000.0",
#         "8",
#         "98.2",
#         "15",
#         "512",
#         "Gray space",
#         "Xiaomi Redmi Note 11",
#         "1024GB, Синий",
#         "31000.0",
#         "14",
#         "90.3",
#         "Note 11",
#         "1024",
#         "Синий",
#         "Газонная трава",
#         "Элитная трава для газона",
#         "500.0",
#         "20",
#         "Россия",
#         "7 дней",
#         "Зеленый",
#         "Газонная трава 2",
#         "Выносливая трава",
#         "450.0",
#         "15",
#         "США",
#         "5 дней",
#         "Темно-зеленый",
#         "2580000.0",
#         "16750.0",
#         "Возникла ошибка TypeError при попытке сложения",
#         "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
#         "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
#         "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
#         "5",
#         "Возникла ошибка TypeError при добавлении не продукта",
#     ]
#
#     for expected in expected_strings:
#         assert expected in output, f"Ожидаемая строка '{expected}' не найдена в выводе"
