"""
ALGOgent Runtime SDK
state_manager.py

Runtime State Manager
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core.exceptions import StateError


class StateManager:
    """
    Persistent state storage.
    """

    def __init__(
        self,
        storage_path: str = "algogent_state.json",
    ):
        self.storage_path = Path(storage_path)

    async def save_state(
        self,
        state: dict[str, Any],
    ) -> bool:

        try:

            with open(
                self.storage_path,
                "w",
                encoding="utf-8",
            ) as fp:

                json.dump(
                    state,
                    fp,
                    indent=2,
                    ensure_ascii=False,
                )

            return True

        except Exception as exc:

            raise StateError(
                f"Failed to save state: {exc}"
            ) from exc

    async def load_state(
        self,
    ) -> dict[str, Any]:

        try:

            if not self.storage_path.exists():
                return {}

            with open(
                self.storage_path,
                "r",
                encoding="utf-8",
            ) as fp:

                return json.load(fp)

        except Exception as exc:

            raise StateError(
                f"Failed to load state: {exc}"
            ) from exc

    async def patch_state(
        self,
        patch: dict[str, Any],
    ) -> dict[str, Any]:

        current = await self.load_state()

        current.update(patch)

        await self.save_state(current)

        return current

    async def clear_state(
        self,
    ) -> bool:

        try:

            if self.storage_path.exists():
                self.storage_path.unlink()

            return True

        except Exception as exc:

            raise StateError(
                f"Failed to clear state: {exc}"
            ) from exc