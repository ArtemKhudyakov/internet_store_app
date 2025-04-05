from typing import Any, Dict, List
from unittest.mock import patch

import pytest

from src.classes import Category, Product
from src.utils import create_objects


def test_create_objects_success(test_data_valid: List[Dict[str, Any]]) -> None:
    """Тест успешного создания объектов из JSON."""

    with patch("src.utils.read_json", return_value=test_data_valid):
        result = create_objects("test.json")

        assert len(result) == 1
        assert isinstance(result[0], Category)
        assert isinstance(result[0].products[0], Product)
        assert result[0].name == "Тест"
        assert result[0].products[0].name == "Товар"


def test_create_objects_empty_file() -> None:
    """Тест с пустым файлом."""
    with patch("src.utils.read_json", return_value=[]):
        result = create_objects("empty.json")
        assert result == []


def test_create_objects_invalid_data(test_data_invalid: List[Dict[str, Any]]) -> None:
    """Тест с некорректными данными."""
    test_data = [{"name": "Некорректная категория", "description": "Описание", "products": [{"invalid": "data"}]}]

    with patch("src.utils.read_json", return_value=test_data):
        with pytest.raises(TypeError):
            create_objects("invalid.json")


def test_create_objects_multiple_categories(test_data_multiple_categories: List[Dict[str, Any]]) -> None:
    """Тест с несколькими категориями."""

    with patch("src.utils.read_json", return_value=test_data_multiple_categories):
        result = create_objects("multiple.json")

        assert len(result) == 2
        assert result[0].name == "Категория 1"
        assert result[1].name == "Категория 2"
        assert len(result[0].products) == 1
        assert result[0].products[0].name == "Товар 1"
