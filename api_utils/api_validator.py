import requests

class APIValidator:
    @staticmethod
    def validate_status_code(response, expected_status_code):
        """
        Validates the status code of the API response.
        """
        if response.status_code != expected_status_code:
            raise AssertionError(
                f"Expected status code {expected_status_code}, but got {response.status_code}"
            )

    @staticmethod
    def validate_response_json(response, expected_keys):
        """
        Validates that the response JSON contains the expected keys.
        """
        try:
            response_json = response.json()
        except ValueError:
            raise AssertionError("Response is not a valid JSON")

        missing_keys = [key for key in expected_keys if key not in response_json]
        if missing_keys:
            raise AssertionError(f"Missing keys in response JSON: {missing_keys}")

    @staticmethod
    def validate_response_time(response, max_response_time):
        """
        Validates that the response time is within the acceptable limit.
        """
        if response.elapsed.total_seconds() > max_response_time:
            raise AssertionError(
                f"Response time {response.elapsed.total_seconds()} exceeds maximum allowed {max_response_time} seconds"
            )

# Example usage:
# response = requests.get("https://api.example.com/resource")
# APIValidator.validate_status_code(response, 200)
# APIValidator.validate_response_json(response, ["id", "name", "status"])
# APIValidator.validate_response_time(response, 2)