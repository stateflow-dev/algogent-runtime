"""
ALGOgent Runtime SDK
event_bus.py

Async Event Bus
"""

from __future__ import annotations

import asyncio
from collections import defaultdict
from typing import Callable, Awaitable, Any


EventHandler = Callable[
    [dict],
    Awaitable[None]
]


class EventBus:
    """
    Lightweight async event bus.
    """

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
    ):
        """
        Decorator style subscription.
        """

        def decorator(
            func: EventHandler,
        ):

            self._subscribers[
                event_name
            ].append(func)

            return func

        return decorator

    async def emit(
        self,
        event_name: str,
        payload: dict | None = None,
    ) -> None:

        payload = payload or {}

        handlers = self._subscribers.get(
            event_name,
            []
        )

        if not handlers:
            return

        await asyncio.gather(
            *[
                handler(payload)
                for handler in handlers
            ]
        )

    def listener_count(
        self,
        event_name: str,
    ) -> int:

        return len(
            self._subscribers.get(
                event_name,
                []
            )
        )

    def registered_events(
        self,
    ) -> list[str]:

        return list(
            self._subscribers.keys()
        )