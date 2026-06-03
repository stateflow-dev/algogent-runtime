"""
ALGOgent Runtime SDK
result.py

Standard Runtime Result Object
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class RuntimeResult:
    """
    Standard result returned by Runtime.
    """

    success: bool

    data: Any = None

    execution_time: float = 0.0

    confidence: float = 0.0

    retry_count: int = 0

    error: str | None = None

    @property
    def failed(self) -> bool:
        return not self.success

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "data": self.data,
            "execution_time": self.execution_time,
            "confidence": self.confidence,
            "retry_count": self.retry_count,
            "error": self.error,
        }