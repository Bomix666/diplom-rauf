#!/bin/bash
# Скрипт для запуска проекта и тестовых данных на Mac
set -e

if [ "$1" = "testdata" ]; then
  echo "Добавление тестовых данных..."
  python3 manage.py shell < scripts/testdata.py
  exit 0
fi

python3 manage.py runserver 0.0.0.0:8000
