import requests

API_KEY = "dYjYDbsHdEYnaPfFtzd955l5NesyI0gb"

url = "https://calendarific.com/api/v2/holidays"

params = {"api_key": API_KEY, "country": "IN", "year": 2026}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print("Indian Holidays & Festivals\n")

    for index, holiday in enumerate(data["response"]["holidays"], start=1):
        print(f"{index}. {holiday['name']}")

else:
    print(f"Error: {response.status_code}")
    print(response.text)


print(data["response"]["holidays"][0])