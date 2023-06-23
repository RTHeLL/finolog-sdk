import aiohttp

from finolog.services.contractor_service import FinologContractorService
from finolog.services.country_service import FinologCountryService
from finolog.services.document_service import FinologDocumentService
from finolog.services.requisite_service import FinologRequisiteService


class FinologClient:
    def __init__(self, api_token: str, biz_id: int) -> None:
        if not isinstance(biz_id, int):
            raise TypeError("biz_id must be a number")

        self.biz_id = biz_id

        self.session = aiohttp.ClientSession(headers={"Api-Token": api_token})

        self.contractor = FinologContractorService(
            client=self.session, biz_id=self.biz_id
        )
        self.document = FinologDocumentService(
            client=self.session, biz_id=self.biz_id
        )
        self.requisite = FinologRequisiteService(
            client=self.session, biz_id=self.biz_id
        )
        self.country = FinologCountryService(client=self.session)

    async def close(self):
        await self.session.close()
