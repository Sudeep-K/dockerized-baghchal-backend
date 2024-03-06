#!/bin/sh
watchmedo auto-restart --directory=multiple_queues_app --pattern=*.py --recursive -- celery -A baghchal worker "$@" --loglevel=info