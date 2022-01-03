from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.DEV
    deploy_type = DeployType.BACKEND

    target_name = 'backend dev'
    tgz_filename = 'my24-develop-build.tgz'
    release_filename = 'release'
