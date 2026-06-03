# Contributing to ALGOgent Runtime SDK

Thank you for your interest in contributing! Here's how to get started.

---

## Getting Started

### 1. Fork & clone the repo

```bash
git clone https://github.com/your-username/algogent-runtime.git
cd algogent-runtime
```

### 2. Create a branch

```bash
git checkout -b feature/your-feature-name
```

Use clear branch names:
- `feature/` → new feature
- `fix/` → bug fix
- `docs/` → documentation update

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Before Submitting

### Run all tests

```bash
python -m algogent.test.test_state
python -m algogent.test.test_checkpoint
python -m algogent.test.test_confidence
python -m algogent.test.test_events
python -m algogent.test.test_logger
```

All tests must pass before opening a Pull Request.

### Code style

- Follow existing code style in each module
- Keep functions focused and single-purpose
- Add docstrings for public functions and classes

---

## Submitting a Pull Request

1. Push your branch to your fork
2. Open a Pull Request against `main`
3. Fill in the PR description — what changed and why
4. Wait for review

---

## Reporting Issues

Open an issue at [github.com/stateflow-dev/algogent-runtime/issues](https://github.com/stateflow-dev/algogent-runtime/issues) with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Python version and OS

---

## Project Structure

See [README.md](README.md) for full project structure and module descriptions.
