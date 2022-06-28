#!/bin/bash

cd deploy/deploy
../venv/bin/python manage.py deploy_rust_dev

sudo supervisorctl restart all
