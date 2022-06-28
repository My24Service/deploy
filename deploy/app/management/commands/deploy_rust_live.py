from app.deploy import DeployBase, BuildType, DeployType

from django.core.management.base import BaseCommand


class Command(DeployBase, BaseCommand):
    target = BuildType.LIVE
    deploy_type = DeployType.RUST_BACKEND

    target_name = 'rust live'
    tgz_filename = 'my24-rust-backend-build.tgz'
    release_filename = 'my24-rust-backend-release'
