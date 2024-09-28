from loguru import logger
import sys

ERROR_MESSAGE: str = "Invalid input was passed to logging function, please pass a valid one."
LOG_FILE: str = "logs/logfile.log"

class Logger:
    """
    This logger class as the goal of taking user input and logging to both console and logfile different states
    and info about the application, such as variables, error messages, etc.

    arguments:
        log_message: str

    usage:
        Logger.info_logging("this is a log function")

    tests:
        tests/test_logger,py
    """

    @staticmethod
    async def info_logging(log_message: str):
        if log_message is not None and log_message != "":
            await logger.add(LOG_FILE, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="INFO")
            await logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="INFO")    
            await logger.info(log_message)

        return ERROR_MESSAGE
    
    @staticmethod
    async def warning_logging(log_message: str):
        if log_message is not None and log_message != "":
            await logger.add(LOG_FILE, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="WARNING")
            await logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="WARNING")    
            await logger.warning(log_message)

        return ERROR_MESSAGE
    
    @staticmethod
    async def error_logging(log_message: str):
        if log_message is not None and log_message != "":
            await logger.add(LOG_FILE, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="ERROR")
            await logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {function} | {message}", level="ERROR")    
            await logger.error(log_message)

        return ERROR_MESSAGE
