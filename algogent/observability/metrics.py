"""
ALGOgent Runtime SDK
metrics.py

Runtime Metrics Collector
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RuntimeMetrics:

    total_runs: int = 0

    successful_runs: int = 0

    failed_runs: int = 0

    total_retries: int = 0

    total_execution_time: float = 0.0

    def record_success(
        self,
        execution_time: float,
        retries: int = 0,
    ):

        self.total_runs += 1
        self.successful_runs += 1

        self.total_execution_time += execution_time
        self.total_retries += retries

    def record_failure(
        self,
        execution_time: float,
        retries: int = 0,
    ):

        self.total_runs += 1
        self.failed_runs += 1

        self.total_execution_time += execution_time
        self.total_retries += retries

    @property
    def success_rate(self) -> float:

        if self.total_runs == 0:
            return 0.0

        return round(
            (
                self.successful_runs
                / self.total_runs
            )
            * 100,
            2,
        )

    @property
    def average_execution_time(
        self,
    ) -> float:

        if self.total_runs == 0:
            return 0.0

        return round(
            self.total_execution_time
            / self.total_runs,
            4,
        )

    def summary(
        self,
    ) -> dict:

        return {
            "total_runs": self.total_runs,
            "successful_runs": self.successful_runs,
            "failed_runs": self.failed_runs,
            "success_rate": self.success_rate,
            "total_retries": self.total_retries,
            "avg_execution_time": self.average_execution_time,
        }