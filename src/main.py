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

