import sys
from importlib.abc import Loader
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from pathlib import Path
from typing import cast


def run_main_and_capture_output() -> str:
    """Запускает main.py и возвращает его вывод."""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        # Получаем путь к main.py
        test_dir = Path(__file__).parent
        main_path = test_dir.parent / "src" / "main.py"

        # Современный способ загрузки модуля с проверками типов
        spec = spec_from_file_location("main", str(main_path))
        if spec is None:
            raise ImportError(f"Не удалось создать спецификацию для файла {main_path}")

        module = module_from_spec(spec)
        sys.modules["main"] = module

        # Явно указываем тип для loader
        loader = cast(Loader, spec.loader)
        if loader is None:
            raise ImportError(f"Не удалось получить загрузчик для {main_path}")

        loader.exec_module(module)

        # Если main-блок обернут в функцию main()
        if hasattr(module, "main"):
            module.main()  # type: ignore

        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout


def test_main_output() -> None:
    """Тестирует вывод main.py."""
    output = run_main_and_capture_output()

    # Проверяем основные моменты вывода
    required_strings = [
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        "180000",
        "5",
        "Iphone 15",
        "512GB, Gray space",
        "210000",
        "8",
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        "31000",
        "14",
        "Смартфоны",
        "Телевизоры",
        '55" QLED 4K',
        "123000",
        "7",
    ]

    for s in required_strings:
        assert s in output, f"Строка '{s}' не найдена в выводе"


def test_main_logic() -> None:
    """Тестирует логику main.py."""
    from src.classes import Category

    # Сбросим счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    run_main_and_capture_output()

    assert Category.category_count == 2
    assert Category.product_count == 4
