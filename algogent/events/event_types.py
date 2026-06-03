"""
ALGOgent Runtime SDK
event_types.py

Standard Runtime Events
"""


class EventTypes:

    # Runtime

    RUNTIME_STARTED = (
        "runtime_started"
    )

    RUNTIME_STOPPED = (
        "runtime_stopped"
    )

    # Task

    TASK_STARTED = (
        "task_started"
    )

    TASK_SUCCESS = (
        "task_success"
    )

    TASK_FAILED = (
        "task_failed"
    )

    # Retry

    RETRY_STARTED = (
        "retry_started"
    )

    RETRY_ATTEMPT = (
        "retry_attempt"
    )

    RETRY_EXHAUSTED = (
        "retry_exhausted"
    )

    # State

    STATE_SAVED = (
        "state_saved"
    )

    STATE_LOADED = (
        "state_loaded"
    )

    # Checkpoint

    CHECKPOINT_CREATED = (
        "checkpoint_created"
    )

    CHECKPOINT_RESTORED = (
        "checkpoint_restored"
    )

    # Confidence

    CONFIDENCE_UPDATED = (
        "confidence_updated"
    )

    # Recovery

    RECOVERY_STARTED = (
        "recovery_started"
    )

    RECOVERY_COMPLETED = (
        "recovery_completed"
    )