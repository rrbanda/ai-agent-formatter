
from src.processors import format_as_table, format_as_card

def test_format_as_table():
    data = {"time_seconds": 9.62, "explanation": "Leopard runs fast!"}
    result = format_as_table(data)
    assert result["ui_type"] == "table"
    assert len(result["content"]) == 2

def test_format_as_card():
    md_text = "# Title\n- Point 1\n- Point 2"
    result = format_as_card(md_text)
    assert result["ui_type"] == "card"
    assert result["title"] == "Title"
    assert len(result["content"]) == 2
