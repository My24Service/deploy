from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.DEV
    deploy_type = DeployType.RUST_BACKEND

    target_name = 'rust dev'
    tgz_filename = 'my24-rust-backend-build.tgz'
    release_filename = 'my24-rust-backend-release'
