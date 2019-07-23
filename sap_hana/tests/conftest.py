# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from copy import deepcopy

import pyhdb
import pytest

from datadog_checks.dev import WaitFor, docker_run
from datadog_checks.dev.conditions import CheckDockerLogs

from .common import COMPOSE_FILE, CONFIG, E2E_METADATA


class DbManager(object):
    def __init__(self, config):
        self.host = config['server']
        self.port = config['port']
        self.user = config['username']
        self.password = config['password']
        self.conn = None

    def initialize(self):
        pass

    def connect(self):
        self.conn = pyhdb.connect(host=self.host, port=self.port, user=self.user, password=self.password)


@pytest.fixture(scope='session')
def dd_environment():
    db = DbManager(CONFIG)

    with docker_run(
        COMPOSE_FILE,
        conditions=[
            CheckDockerLogs(COMPOSE_FILE, ['Startup finished!'], wait=5, attempts=120),
            db.initialize,
            WaitFor(db.connect),
        ],
        env_vars={'PASSWORD': CONFIG['password']}
    ):
        yield CONFIG, E2E_METADATA


@pytest.fixture
def instance():
    return deepcopy(CONFIG)
