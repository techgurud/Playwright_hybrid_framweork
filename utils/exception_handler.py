import logging
import traceback

class ExceptionHandler:
    """
    A utility class for handling exceptions and logging them.
    """

    @staticmethod
    def handle_exception(exception: Exception, custom_message: str = None):
        """
        Handles an exception by logging the error details.

        Args:
            exception (Exception): The exception to handle.
            custom_message (str): Optional custom message to log with the exception.
        """
        logger = logging.getLogger(__name__)
        logger.error("An exception occurred.")
        
        if custom_message:
            logger.error(f"Custom Message: {custom_message}")
        
        logger.error(f"Exception Type: {type(exception).__name__}")
        logger.error(f"Exception Message: {exception}")
        logger.error("Stack Trace:")
        logger.error(traceback.format_exc())