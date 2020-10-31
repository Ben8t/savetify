import json
import requests

def parse(url, api_token):
    has_next_key = False
    next_key = ""
    results = []
    headers = {'Authorization': f"Bearer {api_token}"}
    response = requests.get(url, headers=headers).json()

    if "next" in response.keys():
        has_next_key = True

    while has_next_key:
        data = response.get("items")
        results.append(data)
        if response.get("next"):
            url = response.get("next")
            response = requests.get(url, headers=headers).json()
        else:
            has_next_key = False

    return results

def save_data(data, filename="data.json"):
    with open(filename, 'w') as fp:
        json.dump(data, fp)