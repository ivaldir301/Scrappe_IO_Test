import pytest
from unittest.mock import patch
from loguru import logger
from utils.logger import Logger, ERROR_MESSAGE  
import asyncio

@pytest.fixture
def clear_loggers():
    logger.remove()

def run_async(coro):
    return asyncio.run(coro)

def test_logging_invalid_message():
    invalid_message: str = ""
    none_message = None

    assert run_async(Logger.info_logging(invalid_message)) == ERROR_MESSAGE
    assert run_async(Logger.warning_logging(invalid_message)) == ERROR_MESSAGE
    assert run_async(Logger.error_logging(invalid_message)) == ERROR_MESSAGE

    assert run_async(Logger.info_logging(none_message)) == ERROR_MESSAGE
    assert run_async(Logger.warning_logging(none_message)) == ERROR_MESSAGE
    assert run_async(Logger.error_logging(none_message)) == ERROR_MESSAGE
