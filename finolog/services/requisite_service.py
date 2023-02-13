from typing import List

from finolog.services.api_service import FinologAPIService
from finolog.types.requisite_types import Requisite
from finolog.utils import validate_string_length


class FinologRequisiteService(FinologAPIService):
    def __init__(self, api_token: str, biz_id: int) -> None:
        super().__init__(api_token)

        if not isinstance(biz_id, int):
            raise TypeError('biz_id must be a number')

        self.biz_id = biz_id
        self.uri = f'biz/{self.biz_id}/requisite'

    def get_requisites(self, **payload) -> List[Requisite]:
        """
        Returns a list of Contractor.

        Payload:
        contractor_id: int : Contractor ID
        ids: str : Filter by id details (list of id details separated by commas)
        is_bizzed: bool : Filter by counterparties that are business counterparties
        """

        self.validate_payload(
            payload=payload,
            types={
                'contractor_id': int,
                'ids': str,
                'is_bizzed': bool
            }
        )

        if 'is_bizzed' in payload:
            payload['is_bizzed'] = 'true' if payload['is_bizzed'] is True else 'false'

        response = self.request('GET', self.uri, payload)
        return [Requisite(**obj) for obj in response]

    def get_requisite(self, id_: int) -> Requisite:
        self.validate_payload(
            payload={'id': id_},
            types={
                'id': int
            }
        )

        return Requisite(**self.request('GET', f'{self.uri}/{str(id_)}'))

    def create_requisite(self, contractor_id: int, name: str, **payload) -> Requisite:
        """
        Creates and returns Requisite object.

        contractor_id: int : Contractor ID
        name: str: Name

        Payload:
        description: str: Description
        full_name: str: Full name
        inn: str: TIN (ИНН)
        kpp: str: KPP (КПП)
        bank_account: str: Account number
        bank_bic: str: Bank BIC (БИК банка)
        address_postal_index: str: Legal address - index (Юридический адрес - индекс)
        address_city: str: Legal address - city (Юридический адрес - город)
        address_street: str: Legal address - street and house (Юридический адрес - улица и дом)
        country_id: int: Country ID
        phone: str: Phone number
        email: str: Email
        web: str: Website
        bank_iban: str : IBAN code (IBAN)
        bank_mfo: str : MFI code (код МФО)
        """

        payload['contractor_id'] = contractor_id
        payload['name'] = name

        self._validate_update_or_create_payload(payload)

        return Requisite(**self.request('POST', self.uri, payload=payload))

    def update_requisite(self, id_: int, **payload) -> Requisite:
        """
        Creates and returns Requisite object.

        Payload:
        contractor_id: int : Contractor ID
        name: str: Name
        description: str: Description
        full_name: str: Full name
        inn: str: TIN (ИНН)
        kpp: str: KPP (КПП)
        bank_account: str: Account number
        bank_bic: str: Bank BIC (БИК банка)
        address_postal_index: str: Legal address - index (Юридический адрес - индекс)
        address_city: str: Legal address - city (Юридический адрес - город)
        address_street: str: Legal address - street and house (Юридический адрес - улица и дом)
        country_id: int: Country ID
        phone: str: Phone number
        email: str: Email
        web: str: Website
        bank_iban: str : IBAN code (IBAN)
        bank_mfo: str : MFI code (код МФО)
        """

        self._validate_update_or_create_payload(payload)

        return Requisite(**self.request('PUT', f'{self.uri}/{str(id_)}', payload))

    def _validate_update_or_create_payload(self, payload):
        self.validate_payload(
            payload=payload,
            types={
                'contractor_id': int,
                'name': str,
                'description': str,
                'full_name': str,
                'inn': str,
                'kpp': str,
                'bank_account': str,
                'bank_bic': str,
                'address_postal_index': str,
                'address_city': str,
                'address_street': str,
                'country_id': int,
                'phone': str,
                'email': str,
                'web': str,
                'bank_iban': str,
                'bank_mfo': str
            }
        )

        if 'inn' in payload:
            validate_string_length('inn', payload['inn'], min_l=10, max_l=12)
        if 'kpp' in payload:
            validate_string_length('kpp', payload['kpp'], min_l=9, max_l=9)
        if 'bank_account' in payload:
            validate_string_length('bank_account', payload['bank_account'], min_l=20, max_l=28)
        if 'bank_bic' in payload:
            validate_string_length('bank_bic', payload['bank_bic'], min_l=9, max_l=9)

    def delete_requisite(self, id_: int) -> Requisite:
        self.validate_payload(
            payload={'id': id_},
            types={
                'id': int
            }
        )

        return Requisite(**self.request('DELETE', f'{self.uri}/{str(id_)}'))
