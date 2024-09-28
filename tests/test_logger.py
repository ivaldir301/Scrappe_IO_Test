import pytest
from unittest.mock import patch
from loguru import logger
from utils.logger import Logger, ERROR_MESSAGE  

@pytest.fixture
def clear_loggers():
    logger.remove()

def test_logging_invalid_message():
    invalid_message: str = ""
    none_message = None

    assert Logger.info_logging(invalid_message) == ERROR_MESSAGE
    assert Logger.warning_logging(invalid_message) == ERROR_MESSAGE
    assert Logger.error_logging(invalid_message) == ERROR_MESSAGE

    assert Logger.info_logging(none_message) == ERROR_MESSAGE
    assert Logger.warning_logging(none_message) == ERROR_MESSAGE
    assert Logger.error_logging(none_message) == ERROR_MESSAGE

