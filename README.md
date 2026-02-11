# Smart Trade API

Minimal FastAPI project for processing trade-related CSVs and returning simple reports.

Structure:


Run locally:

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
# Smart Trade API

A compact FastAPI service for processing trade CSVs and producing concise reports.

## Features

- Parse trade CSV inputs and generate summary reports
- Lightweight FastAPI endpoints for integration with other tools
- Example input/output files under `data/`

## Project Layout

- `app/` — FastAPI application and routers
- `data/` — example input/output CSVs
- `tests/` — unit and integration tests

## Quick Start

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
uvicorn app.main:app --reload
```

API will be available at http://127.0.0.1:8000.

## Testing

Run tests with:

```powershell
pytest
```

## Contributing

Open issues or PRs to suggest improvements or add features.

## Contact

Include your GitHub profile or email for follow-up.
