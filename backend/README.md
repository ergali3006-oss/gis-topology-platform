# Backend quick run

## Рекомендуемый запуск (без Docker, в Codespaces)

```bash
./scripts/start_backend.sh
```

Скрипт автоматически ставит зависимости и запускает API на `http://localhost:8000`.

## Альтернатива (вручную)

```bash
python -m pip install -r backend/requirements.txt
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Не запускайте `python backend/app/main.py` напрямую — это ASGI-приложение для запуска через Uvicorn.
