from enum import Enum
import logging
import os
import subprocess

import boto3

from django.conf import settings

logger = logging.getLogger(__name__)


class BuildType(Enum):
    DEV = 1
    LIVE = 2


class DeployType(Enum):
    BACKEND = 1
    FRONTEND = 2
    RUST_BACKEND = 1


class DeployBase:
    target = BuildType.DEV
    deploy_type = DeployType.BACKEND

    target_name = None
    tgz_filename = None
    release_filename = None

    def handle(self, *args, **options):
        logger.info('Downloading {0} build'.format(self.target_name))
        release_name = self.download_linode()

        logger.info('Doing {0} deploy: {1}'.format(self.target_name, release_name))
        self.do_deploy(release_name)

    def download_linode(self):
        endpoint = settings.LINODE_ENDPOINT_URL_DEV_DEPLOYMENTS
        if self.target == BuildType.LIVE:
            endpoint = settings.LINODE_ENDPOINT_URL_LIVE_DEPLOYMENTS

        bucket = settings.LINODE_S3_BUCKET_DEV_DEPLOYMENTS
        if self.target == BuildType.LIVE:
            bucket = settings.LINODE_S3_BUCKET_LIVE_DEPLOYMENTS

        linode_obj_config = {
            "endpoint_url": 'https://%s' % endpoint,
        }

        client = boto3.client('s3', **linode_obj_config)

        client.download_file(bucket, self.tgz_filename, self.tgz_filename)
        client.download_file(bucket, self.release_filename, self.release_filename)

        release_name = self.get_release_name()

        if not release_name:
            raise ValueError('release_name could not be determined')

        os.unlink(self.release_filename)

        return release_name

    def get_release_name(self):
        with open(self.release_filename) as f:
            lines = f.readlines()
            return lines[0].strip()

    def do_deploy(self, release_name):
        if self.deploy_type == DeployType.FRONTEND:
            shell_script = 'deploy_front.sh'

        elif self.deploy_type == DeployType.RUST_BACKEND:
            shell_script = 'deploy_rust.sh'

        else:
            raise ValueError('Unable to determine deploy type')

        proc = subprocess.Popen(['./{0}'.format(shell_script), self.tgz_filename, release_name], stdout=subprocess.PIPE)
        proc.wait()
