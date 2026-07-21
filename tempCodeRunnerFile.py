import requests

def test_api():
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        print(response.status_code)
        data = response.json()
        print(type(data))
        print(data)
test_api()

