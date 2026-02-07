# Smart Trade API

Minimal FastAPI project for processing trade-related CSVs and returning simple reports.

Structure:

- `app/` - FastAPI app and routers
- `data/` - sample input/output files
- `tests/` - basic unit tests

Run locally:

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
