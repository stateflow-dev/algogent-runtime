from algogent.observability.logger import RuntimeLogger

logger = RuntimeLogger()

logger.runtime(
    "Runtime started"
)

logger.retry(
    "Retry #1"
)

logger.state(
    "State saved"
)