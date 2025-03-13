import httpx
# function to get the auth token
def get_auth_token():
    url = "https://api.com/auth"
    payload = {
        "username": "test",
        "password": "test"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()["token"]



BASE_URL = "https://jsonplaceholder.typicode.com"  # Example API

def get(endpoint, params=None):
    response = httpx.get(f"{BASE_URL}{endpoint}", params=params)
    return response

def post(endpoint, data=None):
    response = httpx.post(f"{BASE_URL}{endpoint}", json=data)
    return response

def put(endpoint, data=None):
    response = httpx.put(f"{BASE_URL}{endpoint}", json=data)
    return response

def patch(endpoint, data=None):
    response = httpx.patch(f"{BASE_URL}{endpoint}", json=data)
    return response

def delete(endpoint):
    response = httpx.delete(f"{BASE_URL}{endpoint}")
    return response