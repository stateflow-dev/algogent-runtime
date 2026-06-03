"""
ALGOgent Runtime SDK
confidence_engine.py

Confidence Intelligence Engine
"""

from __future__ import annotations

from collections import deque


class ConfidenceEngine:
    """
    Adaptive confidence scoring.
    """

    def __init__(
        self,
        history_size: int = 100,
    ):
        self.history = deque(
            maxlen=history_size
        )

    def calculate(
        self,
        success_rate: float,
        retry_count: int,
        execution_time: float,
    ) -> float:
        """
        Return confidence score (0-1)
        """

        score = 1.0

        # Retry penalty
        score -= retry_count * 0.08

        # Slow execution penalty
        if execution_time > 5:
            score -= 0.10

        if execution_time > 10:
            score -= 0.15

        # Historical reliability
        score *= success_rate

        score = max(
            0.0,
            min(
                score,
                1.0,
            )
        )

        return round(score, 4)

    def record(
        self,
        success: bool,
    ) -> None:

        self.history.append(success)

    def success_rate(
        self,
    ) -> float:

        if not self.history:
            return 1.0

        success_count = sum(
            self.history
        )

        return (
            success_count /
            len(self.history)
        )

    def evaluate(
        self,
        retry_count: int,
        execution_time: float,
    ) -> float:

        rate = self.success_rate()

        return self.calculate(
            success_rate=rate,
            retry_count=retry_count,
            execution_time=execution_time,
        )