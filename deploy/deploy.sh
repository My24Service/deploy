#!/bin/bash

. /etc/profile.d/my24-base-dir.sh

FILENAME=$1
RELEASE_NAME=$2

mv $FILENAME $MY24_BASEDIR/live

cd $MY24_BASEDIR/live
tar zxf $FILENAME
#rm $FILENAME

DEPLOY_DIR="${MY24_BASEDIR}/live/${RELEASE_NAME}"

echo "DEPLOY_DIR: $DEPLOY_DIR"

cd $DEPLOY_DIR

# make virtualenv
virtualenv --python=python3 venv

# activate virtualenv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

cd source

# install yarn packages
npm install

# link configs
rm -f settings/__init__.py
rm -f settings/local_settings.py

ln -s ${MY24_BASEDIR}/conf/__init__.py settings/__init__.py
ln -s ${MY24_BASEDIR}/conf/live_settings.py settings/live_settings.py

# migrate models
python manage.py migrate_schemas --noinput

# collect static
python manage.py collectstatic --noinput --clear

# collectstatic_js_reverse
python manage.py collectstatic_js_reverse

# create symlink for media
rm -rf media
ln -s /mnt/my24-media/media media

# copy symlink to frontend
cp -P "${MY24_BASEDIR}/live/release/source/my24frontend" .

# set symlink to release
rm "${MY24_BASEDIR}/live/release" && ln -s "${DEPLOY_DIR}" "${MY24_BASEDIR}/live/release"

# restart supervisor
sudo supervisorctl restart all
