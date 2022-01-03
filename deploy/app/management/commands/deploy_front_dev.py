from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.DEV
    deploy_type = DeployType.FRONTEND

    target_name = 'frontend dev'
    tgz_filename = 'my24-frontend-develop-build.tgz'
    release_filename = 'frontend-release'
