"""Custom Application Exceptions"""
from typing import Optional

class AppException(Exception):
    """Base application exception"""
    def __init__(
        self,
        detail: str,
        status_code: int = 500,
        error_code: Optional[str] = None
    ):
        self.detail = detail
        self.status_code = status_code
        self.error_code = error_code or "INTERNAL_ERROR"
        super().__init__(self.detail)

class ValidationException(AppException):
    """Validation error"""
    def __init__(self, detail: str, error_code: str = "VALIDATION_ERROR"):
        super().__init__(detail, status_code=422, error_code=error_code)

class NotFoundException(AppException):
    """Resource not found"""
    def __init__(self, resource: str, error_code: str = "NOT_FOUND"):
        super().__init__(f"{resource} not found", status_code=404, error_code=error_code)

class UnauthorizedException(AppException):
    """Unauthorized access"""
    def __init__(self, detail: str = "Unauthorized", error_code: str = "UNAUTHORIZED"):
        super().__init__(detail, status_code=401, error_code=error_code)

class ForbiddenException(AppException):
    """Forbidden access"""
    def __init__(self, detail: str = "Forbidden", error_code: str = "FORBIDDEN"):
        super().__init__(detail, status_code=403, error_code=error_code)

class ConflictException(AppException):
    """Conflict error"""
    def __init__(self, detail: str, error_code: str = "CONFLICT"):
        super().__init__(detail, status_code=409, error_code=error_code)
