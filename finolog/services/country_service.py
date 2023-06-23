from typing import List

from aiohttp import ClientSession

from finolog.services.api_service import FinologAPIService
from finolog.types.country_types import Country


class FinologCountryService(FinologAPIService):
    def __init__(self, client: ClientSession) -> None:
        super().__init__(client)

        self.uri = "country"

    async def get_countries(self) -> List[Country]:
        return [
            Country(**data) for data in (await self.request("GET", self.uri))
        ]
