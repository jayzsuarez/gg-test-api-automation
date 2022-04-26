# from utils.mock.helper import mock_enabled
# from utils.mock.mock_env import containers
# from wallet_utils.mock import mock_env
from dynaconf import settings

import logging.config

logging.config.fileConfig('config/logging.ini')


def before_all(context):
    context.test_config = settings
    # if mock_enabled:
    #     mock_env.start()


def after_all(context):
    pass
    # if mock_enabled:
    #     mock_env.stop()


def before_scenario(context, scenario):
    logging.info("SCENARIO: %s \n", scenario.name)
    # if mock_enabled:
    #     containers["wiremock"].remove_all()
    # context.data = {}
    context.response = {}
    context.cleanup = []


def after_scenario(context, scenario):
    context.data = {}


def before_feature(context, feature):
    context.data = {}
