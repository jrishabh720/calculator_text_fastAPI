from pydantic import BaseModel, Field
from typing import Literal

class ToolInfoResponse(BaseModel):
    tool_id: str
    name: str
    description: str
    operations: list[str]

class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10000)

    operation: Literal[
        "uppercase",
        "lowercase",
        "word_count",
    ]


class TextResponse(BaseModel):
    operation: str
    result: str | int

class CalculatorRequest(BaseModel):
    a: float
    b: float

    operation: Literal[
        "add",
        "subtract",
        "multiply",
        "divide",
    ]


class CalculatorResponse(BaseModel):
    a: float
    b: float
    operation: str
    result: float