"""
ALGOgent Runtime SDK
runtime.py

Main Runtime Orchestrator
"""

from __future__ import annotations

import time
import traceback
from typing import Any, Callable, Awaitable

from .result import RuntimeResult
from .exceptions import RuntimeExecutionError


class Runtime:
    """
    Main entry point for ALGOgent Runtime SDK.
    """

    def __init__(
        self,
        name: str = "default-runtime",
        debug: bool = False,
    ):
        self.name = name
        self.debug = debug

    async def run(
        self,
        task: Callable[..., Awaitable[Any]],
        *args,
        **kwargs,
    ) -> RuntimeResult:
        """
        Execute async task and return RuntimeResult.
        """

        start_time = time.perf_counter()

        try:
            result = await task(*args, **kwargs)

            execution_time = (
                time.perf_counter() - start_time
            )

            return RuntimeResult(
                success=True,
                data=result,
                execution_time=execution_time,
                confidence=1.0,
                retry_count=0,
                error=None,
            )

        except Exception as exc:

            execution_time = (
                time.perf_counter() - start_time
            )

            if self.debug:
                traceback.print_exc()

            raise RuntimeExecutionError(
                message=str(exc),
                execution_time=execution_time,
            ) from exc