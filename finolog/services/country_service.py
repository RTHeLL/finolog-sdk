from typing import List

from finolog.services.api_service import FinologAPIService
from finolog.types.country_types import Country


class FinologCountryService(FinologAPIService):
    def __init__(self, api_token: str) -> None:
        super().__init__(api_token)

        self.uri = f'country'

    def get_countries(self) -> List[Country]:
        return [Country(**data) for data in self.request('GET', self.uri)]
