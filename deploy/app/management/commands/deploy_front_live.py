from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.LIVE
    deploy_type = DeployType.FRONTEND

    target_name = 'frontend live'
    tgz_filename = 'my24-frontend-main-build.tgz'
    release_filename = 'frontend-release'
