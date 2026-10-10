from app.schemas.tool import (
    CalculatorRequest,
    CalculatorResponse,
)
from app.schemas.tool import TextRequest, TextResponse
from app.schemas.tool import ToolInfoResponse

from app.tools.calculator import calculate
from app.tools.text_processor import process_text


def execute_calculation(
    request: CalculatorRequest,
) -> CalculatorResponse:

    result = calculate(
        a=request.a,
        b=request.b,
        operation=request.operation,
    )

    return CalculatorResponse(
        a=request.a,
        b=request.b,
        operation=request.operation,
        result=result,
    )

def execute_text_operation(
    request: TextRequest,
) -> TextResponse:

    result = process_text(
        text=request.text,
        operation=request.operation,
    )

    return TextResponse(
        operation=request.operation,
        result=result,
    )

def get_tool_information(
    tool_id: str,
) -> ToolInfoResponse:

    tools = {
        "calculator": ToolInfoResponse(
            tool_id="calculator",
            name="Calculator",
            description="Performs basic mathematical operations.",
            operations=[
                "add",
                "subtract",
                "multiply",
                "divide",
            ],
        ),
        "text": ToolInfoResponse(
            tool_id="text",
            name="Text Processor",
            description="Performs basic text-processing operations.",
            operations=[
                "uppercase",
                "lowercase",
                "word_count",
            ],
        ),
    }

    tool = tools.get(tool_id)

    if tool is None:
        raise ValueError(f"Tool not found: {tool_id}")

    return tool