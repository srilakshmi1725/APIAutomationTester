import requests

def test_api(endpoint):
    try:
        response = requests.get(endpoint)
        print(f"URL: {endpoint}")
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example public API
    test_api("https://jsonplaceholder.typicode.com/posts/1")
