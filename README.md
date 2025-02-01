

# **AI-Agent Formatter**
AI-Agent Formatter is a **post-processing component** that takes the output from an AI agent and formats it into a **structured, UI-friendly format**. It supports:
- **JSON Output → Table View**
- **Markdown Output → Card Layout**

This can be used as a **standalone application** or **integrated into other AI-powered applications**.

---

## **🚀 Features**
- **Formats JSON as a table** for easy visualization.
- **Formats Markdown as a card** for better readability.
- **Works as a separate post-processing component** that can be integrated anywhere.
- **Tested independently** before integration with AI agents.

---

## **📂 Folder Structure**
```
ai-agent-formatter/
│── src/
│   ├── processors.py  # JSON & Markdown formatters
│   ├── __init__.py
│
│── tests/
│   ├── test_processors.py  # Unit tests for processors
│   ├── __init__.py
│
│── requirements.txt  # Dependencies
│── README.md  # Documentation
│── .gitignore  # Ignore unnecessary files
│── pyproject.toml  # Python package configuration
│── setup.py  # Optional package setup
```

---

## **🛠️ Installation**
### **1️⃣ Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **2️⃣ Install Dependencies**
```sh
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## **▶️ Running the Application**
Since this is a **post-processing component**, you can **run it as a standalone script** before integrating with other AI agents.

```sh
python src/processors.py
```

---

## **✅ Running Tests**
Before integrating with AI agents, ensure everything works **independently**.

### **Option 1: Run Tests with `PYTHONPATH` (Recommended)**
If pytest cannot find `src/`, explicitly set `PYTHONPATH`:
```sh
PYTHONPATH=$(pwd) pytest tests/test_processors.py  # macOS/Linux
```
For Windows (PowerShell):
```powershell
$env:PYTHONPATH = (Get-Location).Path; pytest tests/test_processors.py
```

### **Option 2: Run Tests Normally**
```sh
pytest tests/
```

---

## **🖥️ Example Usage**
### **1️⃣ Formatting JSON as a Table**
Example JSON output:
```json
{
  "time_seconds": 9.62,
  "explanation": "The leopard's speed was converted from km/h to m/s and calculated using distance/speed."
}
```
Formatted as a **table**:
```
+---------------+------------------------------------------------+
| time_seconds  | 9.62                                           |
| explanation   | The leopard's speed was converted ...         |
+---------------+------------------------------------------------+
```

---

### **2️⃣ Formatting Markdown as a Card**
Example Markdown output:
```md
## Task: Compute Time
- **Speed**: 58 km/h
- **Distance**: 155 meters
- **Formula**: Time = Distance / Speed
```
Formatted as a **card** (UI layout):
```
+-----------------------------------+
|   🏆 Compute Time                 |
|-----------------------------------|
| - Speed: 58 km/h                  |
| - Distance: 155 meters             |
| - Formula: Time = Distance / Speed |
+-----------------------------------+
```

---

## **🔗 Next Steps**
- **Test the application independently** to ensure correct formatting.
- **Integrate it with AI-Agent Response Handling.**
- **Build a UI Component** (React, Vue, or Streamlit) that consumes the formatted output.

---

