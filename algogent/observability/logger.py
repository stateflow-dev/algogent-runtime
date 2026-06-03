"""
ALGOgent Runtime SDK
logger.py

Structured Runtime Logger
"""

from __future__ import annotations

from datetime import datetime


class RuntimeLogger:

    def __init__(
        self,
        enabled: bool = True,
    ):
        self.enabled = enabled

    def _log(
        self,
        component: str,
        message: str,
    ) -> None:

        if not self.enabled:
            return

        now = datetime.now().strftime(
            "%H:%M:%S"
        )

        print(
            f"[{now}]"
            f"[{component}] "
            f"{message}"
        )

    def runtime(
        self,
        message: str,
    ):

        self._log(
            "RUNTIME",
            message,
        )

    def retry(
        self,
        message: str,
    ):

        self._log(
            "RETRY",
            message,
        )

    def state(
        self,
        message: str,
    ):

        self._log(
            "STATE",
            message,
        )

    def checkpoint(
        self,
        message: str,
    ):

        self._log(
            "CHECKPOINT",
            message,
        )

    def confidence(
        self,
        message: str,
    ):

        self._log(
            "CONFIDENCE",
            message,
        )

    def event(
        self,
        message: str,
    ):

        self._log(
            "EVENT",
            message,
        )

    def warning(
        self,
        message: str,
    ):

        self._log(
            "WARNING",
            message,
        )

    def error(
        self,
        message: str,
    ):

        self._log(
            "ERROR",
            message,
        )