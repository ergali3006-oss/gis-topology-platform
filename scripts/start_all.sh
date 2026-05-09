#!/usr/bin/env bash
set -euo pipefail

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is required. In Codespaces, enable Docker-in-Docker or use GitHub Codespaces with Docker support."
  exit 1
fi

exec docker compose up --build
