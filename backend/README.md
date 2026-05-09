# Backend quick run

If you run backend directly in Codespaces (without Docker), install dependencies first:

```bash
python -m pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Do **not** run `python backend/app/main.py` directly.
