from finolog.services.contractor_service import FinologContractorService
from finolog.services.document_service import FinologDocumentService


class FinologClient:
    def __init__(self, api_token: str, biz_id: int) -> None:
        if not isinstance(biz_id, int):
            raise TypeError('biz_id must be a number')

        self.biz_id = biz_id

        self.contractor = FinologContractorService(api_token=api_token, biz_id=self.biz_id)
        self.document = FinologDocumentService(api_token=api_token, biz_id=self.biz_id)
