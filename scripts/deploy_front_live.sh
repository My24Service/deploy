#!/bin/bash

cd deploy/deploy
../venv/bin/python manage.py deploy_front_live

# collect static
cd ${MY24_BASEDIR}/live/release

# activate virtualenv
source venv/bin/activate

cd source

python manage.py collectstatic --noinput
