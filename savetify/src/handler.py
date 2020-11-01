import base64
import json
import requests


def download(url: str, api_token: str) -> dict:
    has_next_key = False
    results = []
    headers = {'Authorization': f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Requests failed : {response.content}")

    if "next" in response.json().keys():
        has_next_key = True

    while has_next_key:
        data = response.json().get("items")
        results.append(data)
        if response.json().get("next"):
            url = response.json().get("next")
            response = requests.get(url, headers=headers)
        else:
            has_next_key = False

    return results

def save_data(data: dict, filename: str="data.json") -> None:
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def get_token(client_id: str, client_secret: str, refresh_token: str) -> str:
    url = "https://accounts.spotify.com/api/token"
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.urlsafe_b64encode(auth_str.encode()).decode()
    headers = {'Authorization': f"Basic {b64_auth_str}"} 
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response  = requests.post(url, payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Requests failed : {response.content}")
    return response.json().get("access_token")