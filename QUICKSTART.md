# ALGOgent Runtime SDK v1 — Quick Start

> Verify your installation by running each module test, then run the full examples.

---

## Prerequisites

- Python 3.10+
- Project cloned and dependencies installed:

```bash
git clone https://github.com/your-username/algogent-runtime.git
cd algogent-runtime
pip install -r requirements.txt
```

---

## Step 1 — Test State Manager

```bash
python -m algogent.test.test_state
```

**Expected Output:**

<img src="assets/carbon_test_state.png" width="500">

---

## Step 2 — Test Checkpoint Engine

```bash
python -m algogent.test.test_checkpoint
```

**Expected Output:**

<img src="assets/carbon_test_checkpoint.png" width="500">

> UUID will differ on each run — that is normal.

---

## Step 3 — Test Confidence Engine

```bash
python -m algogent.test.test_confidence
```

**Expected Output:**

<img src="assets/carbon_test_confidence.png" width="500">

> Output may vary — confidence scores are probabilistic.

---

## Step 4 — Test Event Bus

```bash
python -m algogent.test.test_events
```

**Expected Output:**

<img src="assets/carbon_test_events.png" width="500">

---

## Step 5 — Test Runtime Logger

```bash
python -m algogent.test.test_logger
```

**Expected Output:**

<img src="assets/carbon_test_logger.png" width="500">

---

## Step 6 — Run All Examples

```bash
python -m algogent.examples.ecommerce
python -m algogent.examples.ai_agent
python -m algogent.examples.automation
```

---

## Generated Files

After running the examples, ALGOgent will automatically create:

```text
algogent_state.json          ← runtime state snapshot
.algogent_checkpoints/       ← checkpoint recovery data
```

Add both to `.gitignore`:

```gitignore
__pycache__/
*.pyc
algogent_state.json
.algogent_checkpoints/
.venv/
venv/
.env
```

---

All tests passed? Head over to [README.md](README.md) for full documentation.