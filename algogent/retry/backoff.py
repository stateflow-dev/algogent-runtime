"""
ALGOgent Runtime SDK
backoff.py

Adaptive Exponential Backoff
"""

from __future__ import annotations

import random


class ExponentialBackoff:
    """
    Exponential backoff with jitter.
    """

    def __init__(
        self,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        jitter: bool = True,
    ):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter

    def calculate(
        self,
        attempt: int,
    ) -> float:

        delay = self.base_delay * (2 ** (attempt - 1))

        delay = min(delay, self.max_delay)

        if self.jitter:
            delay += random.uniform(
                0,
                delay * 0.25,
            )

        return round(delay, 3)