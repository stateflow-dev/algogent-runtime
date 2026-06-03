"""
ALGOgent Runtime SDK
storage.py

Storage Backend Abstraction
"""

from __future__ import annotations

from pathlib import Path
import json


class JSONStorage:
    """
    Lightweight storage backend.
    """

    def __init__(
        self,
        path: str = "algogent_storage.json",
    ):
        self.path = Path(path)

    async def write(
        self,
        data: dict,
    ) -> bool:

        with open(
            self.path,
            "w",
            encoding="utf-8",
        ) as fp:

            json.dump(
                data,
                fp,
                indent=2,
                ensure_ascii=False,
            )

        return True

    async def read(
        self,
    ) -> dict:

        if not self.path.exists():
            return {}

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as fp:

            return json.load(fp)

    async def exists(
        self,
    ) -> bool:

        return self.path.exists()