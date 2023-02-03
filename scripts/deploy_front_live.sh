#!/bin/bash

rm -f $HOME/.aws/credentials
ln -s $HOME/.aws/credentials-linode $HOME/.aws/credentials

cd deploy/deploy
../venv/bin/python manage.py deploy_front_live
