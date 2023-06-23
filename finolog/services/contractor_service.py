from typing import List, Any, Optional, Dict, Union, Tuple

from aiohttp import ClientSession

from finolog.services.api_service import FinologAPIService
from finolog.types.contractor_types import Contractor
from finolog.utils import validate_string_length


class FinologContractorService(FinologAPIService):
    def __init__(self, client: ClientSession, biz_id: int) -> None:
        super().__init__(client)

        if not isinstance(biz_id, int):
            raise TypeError("biz_id must be a number")

        self.biz_id = biz_id
        self.uri = f"biz/{self.biz_id}/contractor"

    async def get_contractors(self, **payload) -> List[Contractor]:
        """
        Returns a list of Contractor.

        Payload:
        email: str : Filter by email
        inn: str : Filter by TIN (ИНН)
        with_: str : Include related entities in the request response (comma-separated list of entities).
        Types: requisites, debts, autoeditor
        page: int : Page number
        pagesize: int : Number of items per page
        query: str: Search line
        ids: str : Filter elements by ID (list of id separated by commas)
        is_bizzed: bool : Filter by counterparties that are business counterparties
        """  # noqa E501

        if "with_" in payload:
            payload["with"] = payload.pop("with_")

        self.validate_payload(
            payload=payload,
            types={
                "email": str,
                "inn": str,
                "with": str,
                "page": int,
                "pagesize": int,
                "query": str,
                "ids": str,
                "is_bizzed": bool,
            },
        )

        if "inn" in payload:
            validate_string_length("inn", payload["inn"], min_l=10, max_l=12)

        if "is_bizzed" in payload:
            payload["is_bizzed"] = (
                "true" if payload["is_bizzed"] is True else "false"
            )

        response = await self.request("GET", self.uri, payload)

        try:
            return [Contractor(**obj) for obj in response]
        except TypeError:
            raise TypeError(response)

    async def get_contractor(self, contractor_id: int) -> Contractor:
        self.validate_payload(
            payload={"id": contractor_id}, types={"id": int}
        )

        return Contractor(
            **(await self.request("GET", f"{self.uri}/{str(contractor_id)}"))
        )

    async def get_or_create_by_inn(
        self, inn: str, defaults: Optional[Dict[str, Any]] = None
    ) -> Tuple[Union[Contractor, List[Contractor]], bool]:
        """
        Returns tuple with Contractor object and bool.

        Defaults payload:
        email: str : Email
        phone: str : Phone number
        person: str : The contact person
        description: str : Description
        """

        if defaults:
            self.validate_payload(
                payload=defaults,
                types={
                    "name": str,
                    "email": str,
                    "phone": str,
                    "person": str,
                    "description": str,
                },
            )
        else:
            defaults = {}

        contractors = await self.get_contractors(inn=inn, with_="requisites")

        if not contractors:
            return (
                await self.create_contractor(
                    defaults.pop("name"), **defaults
                ),
                True,
            )

        return contractors, False

    async def create_contractor(self, name: str, **payload) -> Contractor:
        """
        Returns Contractor object.

        Payload:
        email: str : Email
        phone: str : Phone number
        person: str : The contact person
        description: str : Description
        """

        payload["name"] = name

        self.validate_payload(
            payload=payload,
            types={
                "name": str,
                "email": str,
                "phone": str,
                "person": str,
                "description": str,
            },
        )

        return Contractor(
            **(await self.request("POST", self.uri, payload=payload))
        )

    async def update_contractor(
        self, contractor_id: int, **payload
    ) -> Contractor:
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
        payload_copy["id"] = contractor_id

        self.validate_payload(
            payload=payload_copy,
            types={
                "id": int,
                "name": str,
                "email": str,
                "phone": str,
                "person": str,
                "description": str,
            },
        )

        return Contractor(
            **(
                await self.request(
                    "PUT", f"{self.uri}/{str(contractor_id)}", payload
                )
            )
        )

    async def delete_contractor(self, contractor_id: int) -> Contractor:
        self.validate_payload(
            payload={"id": contractor_id}, types={"id": int}
        )

        return Contractor(
            **(
                await self.request(
                    "DELETE", f"{self.uri}/{str(contractor_id)}"
                )
            )
        )
