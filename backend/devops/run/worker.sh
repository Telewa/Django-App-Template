#!/usr/bin/env bash
celery -A configuration worker -Q celery,quick_asks --loglevel=INFO -E
