import requests

class APIClient:
    """
    A utility class for handling API requests.
    """

    def __init__(self, base_url, headers=None, timeout=30):
        """
        Initialize the API client.

        :param base_url: The base URL for the API.
        :param headers: Default headers to include in every request.
        :param timeout: Timeout for API requests in seconds.
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout

    def _build_url(self, endpoint):
        """
        Build the full URL for an API endpoint.

        :param endpoint: The API endpoint.
        :return: Full URL.
        """
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None, headers=None):
        """
        Send a GET request.

        :param endpoint: API endpoint.
        :param params: Query parameters.
        :param headers: Additional headers.
        :return: Response object.
        """
        url = self._build_url(endpoint)
        response = requests.get(url, params=params, headers={**self.headers, **(headers or {})}, timeout=self.timeout)
        response.raise_for_status()
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """
        Send a POST request.

        :param endpoint: API endpoint.
        :param data: Form data.
        :param json: JSON payload.
        :param headers: Additional headers.
        :return: Response object.
        """
        url = self._build_url(endpoint)
        response = requests.post(url, data=data, json=json, headers={**self.headers, **(headers or {})}, timeout=self.timeout)
        response.raise_for_status()
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """
        Send a PUT request.

        :param endpoint: API endpoint.
        :param data: Form data.
        :param json: JSON payload.
        :param headers: Additional headers.
        :return: Response object.
        """
        url = self._build_url(endpoint)
        response = requests.put(url, data=data, json=json, headers={**self.headers, **(headers or {})}, timeout=self.timeout)
        response.raise_for_status()
        return response

    def delete(self, endpoint, headers=None):
        """
        Send a DELETE request.

        :param endpoint: API endpoint.
        :param headers: Additional headers.
        :return: Response object.
        """
        url = self._build_url(endpoint)
        response = requests.delete(url, headers={**self.headers, **(headers or {})}, timeout=self.timeout)
        response.raise_for_status()
        return response