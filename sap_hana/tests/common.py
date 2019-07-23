# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_docker_hostname, get_here

HERE = get_here()
COMPOSE_FILE = os.path.join(HERE, 'docker', 'docker-compose.yaml')
SERVER = get_docker_hostname()
PORT = 39017

CONFIG = {'server': SERVER, 'port': PORT, 'username': 'system', 'password': 'Datadog9000'}

# TODO: Remove
E2E_METADATA = {'start_commands': ['pip install pyhdb']}
