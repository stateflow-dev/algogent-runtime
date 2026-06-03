"""
ALGOgent Runtime SDK
retry_engine.py

Smart Retry Engine
"""

from __future__ import annotations

import asyncio
from typing import Any, Callable, Awaitable

from .backoff import ExponentialBackoff
from ..core.exceptions import RetryExhaustedError


class RetryEngine:
    """
    Smart retry executor.
    """

    def __init__(
        self,
        max_attempts: int = 3,
        base_delay: float = 1.0,
    ):
        self.max_attempts = max_attempts
        self.backoff = ExponentialBackoff(
            base_delay=base_delay
        )

    async def execute(
        self,
        func: Callable[..., Awaitable[Any]],
        *args,
        **kwargs,
    ) -> tuple[Any, int]:

        last_exception = None

        for attempt in range(1, self.max_attempts + 1):

            try:
                result = await func(*args, **kwargs)

                return result, attempt - 1

            except Exception as exc:

                last_exception = exc

                if attempt >= self.max_attempts:
                    break

                delay = self.backoff.calculate(attempt)

                await asyncio.sleep(delay)

        raise RetryExhaustedError(
            f"Retry limit reached ({self.max_attempts})"
        ) from last_exception