"""
ALGOgent Runtime SDK
checkpoint.py

Checkpoint Engine
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from ..core.exceptions import CheckpointError


class CheckpointManager:
    """
    Runtime checkpoint manager.
    """

    def __init__(
        self,
        checkpoint_dir: str = ".algogent_checkpoints",
    ):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    async def create(
        self,
        state: dict[str, Any],
        metadata: dict[str, Any] | None = None,
    ) -> str:

        try:

            checkpoint_id = str(uuid.uuid4())

            payload = {
                "checkpoint_id": checkpoint_id,
                "created_at": datetime.utcnow().isoformat(),
                "metadata": metadata or {},
                "state": state,
            }

            file_path = (
                self.checkpoint_dir /
                f"{checkpoint_id}.json"
            )

            with open(
                file_path,
                "w",
                encoding="utf-8",
            ) as fp:
                json.dump(
                    payload,
                    fp,
                    indent=2,
                    ensure_ascii=False,
                )

            return checkpoint_id

        except Exception as exc:
            raise CheckpointError(
                f"Failed to create checkpoint: {exc}"
            ) from exc

    async def restore(
        self,
        checkpoint_id: str,
    ) -> dict[str, Any]:

        try:

            file_path = (
                self.checkpoint_dir /
                f"{checkpoint_id}.json"
            )

            if not file_path.exists():
                raise CheckpointError(
                    f"Checkpoint not found: {checkpoint_id}"
                )

            with open(
                file_path,
                "r",
                encoding="utf-8",
            ) as fp:

                data = json.load(fp)

            return data["state"]

        except Exception as exc:
            raise CheckpointError(
                f"Failed to restore checkpoint: {exc}"
            ) from exc

    async def latest(self) -> dict[str, Any] | None:

        files = sorted(
            self.checkpoint_dir.glob("*.json"),
            key=lambda x: x.stat().st_mtime,
            reverse=True,
        )

        if not files:
            return None

        with open(
            files[0],
            "r",
            encoding="utf-8",
        ) as fp:

            return json.load(fp)