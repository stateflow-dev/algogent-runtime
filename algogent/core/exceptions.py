"""
ALGOgent Runtime SDK
exceptions.py

Custom Exceptions
"""


class ALGOgentError(Exception):
    """
    Base exception for ALGOgent SDK.
    """

    pass


class RuntimeExecutionError(ALGOgentError):
    """
    Raised when runtime execution fails.
    """

    def __init__(
        self,
        message: str,
        execution_time: float | None = None,
    ):
        super().__init__(message)

        self.message = message
        self.execution_time = execution_time

    def __str__(self) -> str:
        if self.execution_time is None:
            return self.message

        return (
            f"{self.message} "
            f"(execution_time={self.execution_time:.4f}s)"
        )


class RetryExhaustedError(ALGOgentError):
    """
    Raised when retry limit reached.
    """

    pass


class CheckpointError(ALGOgentError):
    """
    Checkpoint operation failed.
    """

    pass


class StateError(ALGOgentError):
    """
    State storage operation failed.
    """

    pass