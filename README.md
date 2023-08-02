# unit-test-python

how to make use of unit testing of python

## VScode settings

- extentions
  - Ruff
  - Black Formatter
  - Python Test Explorer

## Preparation

```bash
export PIPENV_VENV_IN_PROJECT=1
cd backend
pipenv sync --dev
```

## Memo

If test explorer doesn't work, please delete this setting.

```json
"python.testing.cwd": "backend",
```
