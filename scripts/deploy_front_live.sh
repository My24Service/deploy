#!/bin/bash

source /etc/profile.d/frontend-host.sh

rm -f $HOME/.aws/credentials
ln -s $HOME/.aws/credentials-linode $HOME/.aws/credentials

cd deploy/deploy
../venv/bin/python manage.py deploy_front_live

scp -r /var/www/my24service/live/frontend-release/dist/* $FRONTEND_HOST_PATH
