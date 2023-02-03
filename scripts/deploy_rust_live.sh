#!/bin/bash

rm -f $HOME/.aws/credentials
ln -s $HOME/.aws/credentials-linode $HOME/.aws/credentials

cd /var/www/my24service/docker/

./update.sh
