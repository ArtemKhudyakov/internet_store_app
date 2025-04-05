import json
from pathlib import Path
from typing import Any, Dict, List


def read_json(file_name: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей."""
    current_file_path = Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    json_path = project_root_path / "data" / file_name

    with open(json_path, "r", encoding="UTF-8") as f:
        data: List[Dict[str, Any]] = json.load(f)
    return data


if __name__ == "__main__":
    print(read_json("products.json"))
