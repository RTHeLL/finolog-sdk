from typing import Dict, Any

import requests

from finolog.exceptions import ErrorDetail, ValidationError


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

    def validate_payload(self, payload: Dict[str, Any], types) -> bool:
        errors = list()

        if isinstance(payload, list):
            for i in payload:
                self.validate_payload(i, types)
        else:
            for field, value in payload.items():
                _type = types[field]

                if not isinstance(value, _type):
                    errors.append(ErrorDetail(f'must be of type {_type}', field))

        if errors:
            raise ValidationError(errors)

        return True
