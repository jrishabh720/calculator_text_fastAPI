from fastapi import APIRouter, HTTPException, status

from app.schemas.tool import (
    CalculatorRequest,
    CalculatorResponse,
)
from app.services.tool_service import execute_calculation

from app.schemas.tool import TextRequest, TextResponse
from app.services.tool_service import execute_text_operation

from app.schemas.tool import ToolInfoResponse
from app.services.tool_service import get_tool_information

from typing import Annotated
from collections.abc import Callable
from fastapi import Depends

from app.core.dependencies import get_calculator_service
from app.schemas.tool import CalculatorRequest, CalculatorResponse

router = APIRouter(
    prefix="/tools",
    tags=["Tools"],
)

@router.get(
    "/{tool_id}",
    response_model=ToolInfoResponse,
)
def get_tool_endpoint(
    tool_id: str,
) -> ToolInfoResponse:

    try:
        return get_tool_information(tool_id)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.post("/calculator", response_model=CalculatorResponse)
def calculate(
    request: CalculatorRequest,
    calculator_service: Annotated[
        Callable[[CalculatorRequest], CalculatorResponse],
        Depends(get_calculator_service),
    ],
):
    try:
        return calculator_service(request)
    except (ValueError, ZeroDivisionError) as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post(
    "/text",
    response_model=TextResponse,
)
def text_endpoint(
    request: TextRequest,
) -> TextResponse:

    try:
        return execute_text_operation(request)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc