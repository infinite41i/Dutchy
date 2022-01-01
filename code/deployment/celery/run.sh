#!/bin/sh

# wait for PSQL server to start
while ! curl --max-time 30 http://postgresql-svc:5432/ 2>&1 | grep '52'
do
    echo "Waiting for database..."
    sleep 1
done

# run Celery worker for our project crypto_clothes with Celery configuration stored in _base.celery
celery -A _base worker -Q crypto_clothes,celery --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info --concurrency=5