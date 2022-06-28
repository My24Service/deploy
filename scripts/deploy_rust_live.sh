#!/bin/bash

cd deploy/deploy
../venv/bin/python manage.py deploy_rust_live

sudo supervisorctl restart all
