# Запуск платформы

## Вариант 1 (самый простой, без установки программ)

Запуск в браузере через **GitHub Codespaces**:

1. Открой репозиторий на GitHub.
2. Нажми **Code** → **Codespaces** → **Create codespace on work**.
3. В терминале Codespace выполни:

```bash
docker compose up --build
```

4. Открой порты:
   - `3000` — frontend
   - `8000` — backend docs

> Ничего устанавливать локально не нужно: всё запускается в облачном окружении.

---

## Вариант 2 (локально)

```bash
docker compose up --build
```

Адреса:

- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs
- PostGIS: localhost:5432
- Redis: localhost:6379
