## **🚀 Project: AI Response Post-Processing Service**
This is a **standalone FastAPI service** that **formats AI responses** into **UI-friendly formats**:
- **JSON** → Table Format
- **Markdown** → Card Layout

---

## **📂 Folder Structure**
```plaintext
ai-post-processor/
│── configs/
│   ├── config.yaml          # Configurations (if needed)
│── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI service
│   ├── processors.py        # Processing logic (Table/Card conversion)
│── tests/
│   ├── test_processors.py   # Unit tests for processing logic
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

---

## **📌 1️⃣ requirements.txt**
```plaintext
fastapi
uvicorn
pydantic
markdown
pytest
```

---

## **📌 2️⃣ `src/processors.py` (Processing Logic)**
```python
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
```

---

## **📌 3️⃣ `src/main.py` (FastAPI Service)**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Union
from src.processors import format_as_table, format_as_card

app = FastAPI()

# Input Model
class AIResponse(BaseModel):
    format: str  # "json" or "markdown"
    data: Union[Dict, str]  # JSON object or Markdown text

@app.post("/process")
async def process_output(response: AIResponse):
    """Handles AI response formatting."""
    if response.format == "json":
        return format_as_table(response.data)
    elif response.format == "markdown":
        return format_as_card(response.data)
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")

```

---

## **📌 4️⃣ `tests/test_processors.py` (Unit Tests)**
```python
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
```

---

## **📌 5️⃣ `README.md`**
```markdown
# 🏆 AI Post-Processing Service (FastAPI)

## 🚀 Overview
This FastAPI service formats AI-generated responses into UI-friendly formats.

## 📌 Features
✅ Converts JSON to **Table Format**  
✅ Converts Markdown to **Card Layout**  
✅ Standalone API → Easily Integrate into Any System

## 📂 Folder Structure
```
ai-post-processor/
│── configs/
│   ├── config.yaml
│── src/
│   ├── main.py
│   ├── processors.py
│── tests/
│   ├── test_processors.py
│── requirements.txt
│── README.md
```

## 🛠️ Setup
### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI Server
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload
```

## 🛠️ API Usage
### ✅ Convert JSON to Table
#### **Request:**
```sh
curl -X POST "http://localhost:8001/process" \
-H "Content-Type: application/json" \
-d '{
  "format": "json",
  "data": {"time_seconds": 9.62, "explanation": "Leopard runs fast!"}
}'
```
#### **Response:**
```json
{
  "ui_type": "table",
  "content": [
    {"key": "Time (Seconds)", "value": "9.62"},
    {"key": "Explanation", "value": "Leopard runs fast!"}
  ]
}
```

### ✅ Convert Markdown to Card
#### **Request:**
```sh
curl -X POST "http://localhost:8001/process" \
-H "Content-Type: application/json" \
-d '{
  "format": "markdown",
  "data": "# Leopard Speed\n- 58 km/h\n- Converted to 16.11 m/s\n- Crosses bridge in 9.62 sec"
}'
```
#### **Response:**
```json
{
  "ui_type": "card",
  "title": "Leopard Speed",
  "content": [
    "58 km/h",
    "Converted to 16.11 m/s",
    "Crosses bridge in 9.62 sec"
  ]
}
```
```

---

## **🚀 Next Steps**
✅ **You can now call this service** from your main AI pipeline.  
✅ **Front-end just renders the output** (No extra logic needed).  
✅ **Extendable** → Support for graphs, charts, more formats in future.

Would you like me to integrate this with your AI system now? 🚀