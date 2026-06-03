from algogent.confidence.confidence_engine import ConfidenceEngine

engine = ConfidenceEngine()

engine.record(True)
engine.record(True)
engine.record(False)

score = engine.evaluate(
    retry_count=1,
    execution_time=2.0
)

print(score)