from typing import Any, Dict, Optional, Sequence, Type

from pydantic import BaseModel, create_model
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.exceptions import WebSocketException as WebSocketException  # noqa: F401


class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)


RequestErrorModel: Type[BaseModel] = create_model("Request")
WebSocketErrorModel: Type[BaseModel] = create_model("WebSocket")


class FastAPIError(RuntimeError):
    """
    A generic, FastAPI-specific error.
    """


class RequestValidationError(Exception):
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None:
        self.body = body
        self._errors = errors

    def errors(self) -> Sequence[Any]:
        return self._errors


class WebSocketRequestValidationError(Exception):
    def __init__(self, errors: Sequence[Any]) -> None:
        self._errors = errors

    def errors(self) -> Sequence[Any]:
        return self._errors


class ResponseValidationError(Exception):
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None:
        self.body = body
        self._errors = errors

    def errors(self) -> Sequence[Any]:
        return self._errors
