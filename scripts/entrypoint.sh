#!/bin/sh
echo "Running entry point"

echo "Waiting for postgres..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"


if [ "$ENV" = "dev" ]; then
    echo "running migrations"
    python src/gos/manage.py migrate
    python src/gos/manage.py createsuperuser --noinput
fi

exec "$@"