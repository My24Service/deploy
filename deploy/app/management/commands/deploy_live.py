from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.LIVE
    deploy_type = DeployType.BACKEND

    target_name = 'backend live'
    tgz_filename = 'my24-master-build.tgz'
    release_filename = 'release'
