from typing import List, Any, Optional, Dict, Union, Tuple

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

        self.validate_payload(
            payload=payload,
            types={
                'email': str,
                'inn': str,
                'with': str,
                'page': int,
                'pagesize': int,
                'query': str,
                'ids': str,
                'is_bizzed': bool
            }
        )

        if 'is_bizzed' in payload:
            payload['is_bizzed'] = 'true' if payload['is_bizzed'] is True else 'false'

        response = self.request('GET', self.uri, payload)
        return [Contractor(**obj) for obj in response]

    def get_contractor(self, contractor_id: int) -> Contractor:
        self.validate_payload(
            payload={'id': contractor_id},
            types={
                'id': int
            }
        )

        return Contractor(**self.request('GET', f'{self.uri}/{str(contractor_id)}'))

    def get_or_create_by_inn(
            self,
            inn: str,
            defaults: Optional[Dict[str, Any]] = None
    ) -> Tuple[Union[Contractor, List[Contractor]], bool]:
        """
        Returns Contractor object.

        Defaults payload:
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

        if defaults:
            self.validate_payload(
                payload=defaults,
                types={
                    'name': str,
                    'email': str,
                    'phone': str,
                    'person': str,
                    'description': str
                }
            )

        contractors = self.get_contractors(inn=inn)

        if not contractors:
            return self.create_contractor(defaults['name'], **defaults), True

        return contractors, False

    def create_contractor(self, name: str, **payload) -> Contractor:
        """
        Returns Contractor object.

        Payload:
        email: str : Email
        phone: str : Phone number
        person: str : The contact person
        description: str : Description
        """

        payload['name'] = name

        self.validate_payload(
            payload=payload,
            types={
                'name': str,
                'email': str,
                'phone': str,
                'person': str,
                'description': str
            }
        )

        return Contractor(**self.request('POST', self.uri, payload=payload))

    def update_contractor(self, contractor_id: int, **payload) -> Contractor:
        """
        Returns Contractor object.

        Payload:
        name: str : Name
        email: str : Email
        phone: str : Phone number
        person: str : The contact person
        description: str : Description
        """

        payload_copy = payload.copy()
        payload_copy['id'] = contractor_id

        self.validate_payload(
            payload=payload_copy,
            types={
                'id': int,
                'name': str,
                'email': str,
                'phone': str,
                'person': str,
                'description': str
            }
        )

        return Contractor(**self.request('PUT', f'{self.uri}/{str(contractor_id)}', payload))

    def delete_contractor(self, contractor_id: int) -> Contractor:
        self.validate_payload(
            payload={'id': contractor_id},
            types={
                'id': int
            }
        )

        return Contractor(**self.request('DELETE', f'{self.uri}/{str(contractor_id)}'))
