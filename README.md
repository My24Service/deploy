# deploy
Deployments

## Description

- shell script deploy_dev.sh is being called from cli
- it cds into this project, runs `manage.py deploy_front_dev` from venv activate
- that command downloads the latest build and calls a shell command to do the actual deployment with arguments for which files to deploy
- optionally the shell scripts restarts supervisord
- 
