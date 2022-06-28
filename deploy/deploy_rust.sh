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

# set symlink
rm -fr "${MY24_BASEDIR}/live/release/source/my24frontend" && ln -s "${DEPLOY_DIR}" "${MY24_BASEDIR}/live/release/source/my24frontend"
