from flask import Flask, jsonify, request

class MockServerHelper:
    def __init__(self, host='127.0.0.1', port=5000):
        self.app = Flask(__name__)
        self.host = host
        self.port = port

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        if endpoint and handler:
            self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)

    def start(self):
        self.app.run(host=self.host, port=self.port)

# Example usage
if __name__ == "__main__":
    mock_server = MockServerHelper()

    # Example handler function
    def sample_handler():
        return jsonify({"message": "This is a mock response"}), 200

    # Adding an endpoint
    mock_server.add_endpoint(endpoint="/mock-endpoint", endpoint_name="mock_endpoint", handler=sample_handler, methods=["GET"])

    # Start the server
    mock_server.start()