from typing import List

from finolog.services.api_service import FinologAPIService
from finolog.types.contractor_types import Contractor


class FinologContractorService(FinologAPIService):
    def __init__(self, api_token: str, biz_id: int) -> None:
        super().__init__(api_token)

        if not isinstance(biz_id, int):
            raise TypeError('biz_id must be a number')

        self.biz_id = biz_id
        self.uri = f'biz/{self.biz_id}/contractor'

    def get_contractors(self, **payload) -> List[Contractor]:
        """
        Returns a list of Contractor.

        Payload:
        email: str : Filter by email
        inn: str : Filter by TIN (ИНН)
        with: str : Include related entities in the request response (comma-separated list of entities).
        Types: requisites, debts, autoeditor
        page: int : Page number
        pagesize: int : Number of items per page
        query: str: Search line
        ids: str : Filter elements by ID (list of id separated by commas)
        is_bizzed: bool : Filter by counterparties that are business counterparties
        """

        if 'is_bizzed' in payload:
            payload['is_bizzed'] = 'true' if payload['is_bizzed'] == True else 'false'

        response = self.request('GET', self.uri, payload)
        return [Contractor(**obj) for obj in response]

    def get_contractor(self, contractor_id: int) -> Contractor:
        self.__validate_contractor_id(contractor_id)

        return Contractor(**self.request('GET', f'{self.uri}/{str(contractor_id)}'))

    def create_contractor(self, contractor_id: int, **payload) -> Contractor:
        """
        Returns Contractor object.

        Payload:
        email: str : Filter by email
        inn: str : Filter by TIN (ИНН)
        with: str : Include related entities in the request response (comma-separated list of entities).
        Types: requisites, debts, autoeditor
        page: int : Page number
        pagesize: int : Number of items per page
        query: str: Search line
        ids: str : Filter elements by ID (list of id separated by commas)
        is_bizzed: bool : Filter by counterparties that are business counterparties
        """
        pass

    def update_contractor(self, contractor_id: int, **payload) -> Contractor:
        pass

    def delete_contractor(self, contractor_id: int) -> Contractor:
        self.__validate_contractor_id(contractor_id)

        return Contractor(**self.request('DELETE', f'{self.uri}/{str(contractor_id)}'))

    @staticmethod
    def __validate_contractor_id(contractor_id: int):
        if not isinstance(contractor_id, int):
            raise TypeError('id_ must be a number')
