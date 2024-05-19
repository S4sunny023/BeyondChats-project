import requests

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data(api_url=API_URL):
    page = 1
    results = []

    while True:
        response = requests.get(api_url, params={'page': page})
        if response.status_code != 200:
            break

        data = response.json()
        if not data:
            break

        results.extend(data)
        page += 1

    return results
