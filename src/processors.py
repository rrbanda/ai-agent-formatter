import markdown
from typing import Dict, Union

def format_as_table(data: Dict) -> Dict:
    """Convert JSON to Table Format."""
    return {
        "ui_type": "table",
        "content": [{"key": k, "value": v} for k, v in data.items()]
    }

def format_as_card(data: str) -> Dict:
    """Convert Markdown to Card Format."""
    lines = [line.strip() for line in data.split("\n") if line.strip()]
    return {
        "ui_type": "card",
        "title": lines[0].replace("# ", "") if lines[0].startswith("#") else "Information",
        "content": lines[1:]
    }
