import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from src.data_reader import read_json


def test_read_json_success(tmp_path: Path) -> None:
    """Тест успешного чтения JSON-файла."""
    # Создаем временный файл с тестовыми данными
    test_data = [{"name": "Тестовый товар"}]
    test_file = tmp_path / "test_products.json"
    test_file.write_text(json.dumps(test_data), encoding="utf-8")

    # Мокаем только open, чтобы не зависеть от реальной файловой системы
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))) as mocked_open:
        result = read_json("test_products.json")

    assert result == test_data
    mocked_open.assert_called_once()


def test_read_json_file_not_found() -> None:
    """Тест обработки отсутствующего файла."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_json("nonexistent.json")


def test_read_json_invalid_json(tmp_path: Path) -> None:
    """Тест обработки невалидного JSON."""
    test_file = tmp_path / "invalid.json"
    test_file.write_text("{invalid json}", encoding="utf-8")

    with patch("builtins.open", mock_open(read_data="{invalid json}")):
        with pytest.raises(json.JSONDecodeError):
            read_json("invalid.json")


def test_read_json_empty_file(tmp_path: Path) -> None:
    """Тест чтения пустого файла."""
    test_file = tmp_path / "empty.json"
    test_file.write_text("", encoding="utf-8")

    with patch("builtins.open", mock_open(read_data="")):
        with pytest.raises(json.JSONDecodeError):
            read_json("empty.json")
