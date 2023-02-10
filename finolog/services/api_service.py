import requests


class FinologAPIService:
    BASE_URI = 'https://api.finolog.ru/v1/'

    def __init__(self, api_token: str) -> None:
        self.client = requests.Session()
        self.client.headers.update({
            'Api-Token': api_token
        })

    def request(self, method, uri, payload=None):
        if payload is None:
            payload = {}

        response = self.client.request(method, self.BASE_URI + uri, json=payload)

        if response.status_code == 404:
            raise ValueError(*response)

        return response.json()
