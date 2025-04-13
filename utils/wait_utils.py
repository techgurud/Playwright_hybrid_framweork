import time

def wait_with_retry(func, retries=3, delay=2, *args, **kwargs):
    """
    Wait utility with retry mechanism.

    Args:
        func (callable): The function to execute.
        retries (int): Number of retries before giving up.
        delay (int): Delay in seconds between retries.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Any: The result of the function if successful.

    Raises:
        Exception: The last exception raised if all retries fail.
    """
    last_exception = None
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("All retries failed.")
    raise last_exception