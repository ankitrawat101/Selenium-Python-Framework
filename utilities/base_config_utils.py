import inspect
import json
import logging
import os.path
from enum import Enum

import pytest


@pytest.mark.usefixture("setup")
class BaseConfig:
    class WaitConditionTypes(Enum):
        VISIBLE = 1
        CLICKABLE = 2
        PRESENCE = 3
        STALENESS = 4
        INVISIBLE = 5
        VISIBLE_ALL = 6
        PRESENCE_ALL = 7

    def wait_for_element(self, locator, wait_type):
        if wait_type == BaseConfig.WaitConditionTypes.VISIBLE:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.CLICKABLE:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.PRESENCE:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.STALENESS:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.INVISIBLE:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.VISIBLE_ALL:
            pass
        elif wait_type == BaseConfig.WaitConditionTypes.PRESENCE_ALL:
            pass

    def logger_init(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        handler = logging.FileHandler("tests_logs.log")
        log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        handler.setFormatter(log_formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def get_data_from_json(file_path):
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print("File does not exists")
            return None

    @staticmethod
    def get_project_root():
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(current_file_path))
        return project_root
