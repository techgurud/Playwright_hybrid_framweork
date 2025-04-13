import time
from functools import wraps

class RetryUtility:
    def __init__(self, retries=3, delay=2, exceptions=(Exception,)):
        """
        Initialize the RetryUtility.

        :param retries: Number of retry attempts.
        :param delay: Delay between retries in seconds.
        :param exceptions: Tuple of exception types to catch and retry.
        """
        self.retries = retries
        self.delay = delay
        self.exceptions = exceptions

    def retry(self, func):
        """
        Decorator to apply retry logic to a function.

        :param func: Function to wrap with retry logic.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < self.retries:
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    attempts += 1
                    if attempts >= self.retries:
                        raise
                    time.sleep(self.delay)
        return wrapper