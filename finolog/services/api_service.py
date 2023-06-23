from typing import Dict, Any

from aiohttp import ClientSession

from finolog.exceptions import ErrorDetail, ValidationError


class FinologAPIService:
    BASE_URI = "https://api.finolog.ru/v1/"

    def __init__(self, client: ClientSession) -> None:
        self.client = client

    async def request(self, method, uri, payload=None):
        if payload is None:
            payload = {}
        async with self.client.request(
            method, self.BASE_URI + uri, json=payload
        ) as response:
            if response.status == 404:
                raise ValueError(*response)

            return await response.json()

    def validate_payload(self, payload: Dict[str, Any], types) -> bool:
        errors = list()

        if isinstance(payload, list):
            for i in payload:
                self.validate_payload(i, types)
        else:
            for field, value in payload.items():
                _type = types[field]

                if not isinstance(value, _type):
                    errors.append(
                        ErrorDetail(f"must be of type {_type}", field)
                    )

        if errors:
            raise ValidationError(errors)

        return True
