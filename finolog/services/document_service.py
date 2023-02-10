from typing import List

from finolog.services.api_service import FinologAPIService
from finolog.types.document_types import Document, DocumentPDF


class FinologDocumentService(FinologAPIService):
    def __init__(self, api_token: str, biz_id: int) -> None:
        super().__init__(api_token)

        if not isinstance(biz_id, int):
            raise TypeError('biz_id must be a number')

        self.biz_id = biz_id
        self.uri = f'biz/{self.biz_id}/orders/document'

    def get_documents(
            self,
            **payload
    ) -> List[Document]:
        """
        Returns a list of Document.

        Payload:
        page: int : Page number
        pagesize: int : Number of items per page
        query: str: Search line
        item_id: int : Filter by product ID
        kind: str : Filter by document type. Types: invoice, shipment
        template: str : Filter by document template if kind is specified. Types: ru, international, stock, asset
        ru - русифицированный шаблон, если kind равен invoice
        international - интернациональный шаблон, если kind равен invoice
        stock - отгрузка по остаткам, если kind равен shipment
        asset - отгрузка по средствам, если kind равен shipment
        """

        response = self.request('GET', self.uri, payload)

        return [Document(**obj) for obj in response]

    def get_document(self, id_: int) -> Document:
        self.__validate_document_id(id_)

        return Document(**self.request('GET', f'{self.uri}/{str(id_)}'))

    def get_document_pdf(self, id_: int, **payload) -> DocumentPDF:
        """
        Returns DocumentPDF object.

        Payload:
        no_sign: bool : Don't show print and signature in generated pdf
        """

        self.__validate_document_id(id_)

        if 'no_sign' in payload:
            payload['no_sign'] = 'true' if payload['no_sign'] == True else 'false'

        return DocumentPDF(**self.request('GET', f'{self.uri}/{str(id_)}/pdf/invoice', payload))

    def create_document(self, **payload) -> Document:
        """
        Returns a list of FinologDocument.

        Payload:
        kind: str : Filter by document type. Types: invoice, shipment
        vat_type: str : VAT (НДС) type
        type: str : Document type. Types: in, out
        date: str : Document date. Format: YYYY-MM-DD
        template: str : Document template. Templates: ru, international
        from_contractor_id: int : Vendor counterparty ID
        from_requisite_id: int : Supplier details ID
        to_contractor_id: int : Buyer counterparty ID
        to_requisite_id: int : Buyer ID
        to_contractor_draft: str : Name of the receiving counterparty
        (for example, when it has not yet been created as a counterparty)
        number: str : Document Number
        status: str : Document status. Statuses: draft, published, viewed, paid, wrong
        comment: str : A comment
        description: str : Description
        model_type: str : The model to which the document will be bound, for example Order
        model_id: int : ID of the model to which the document will be linked
        items: dict : List of goods and services.
        Example:
        "items": [
            {
                "id": -1,
                "item_id": 134204,
                "count": 1,
                "vat": 0,
                "price": 0,
                "price_currency_id": 1,
                "amortization": 1,
                "item_name": "Мука"
            }
        ]
        """

        return Document(**self.request('POST', self.uri, payload=payload))

    def update_document(self, id_: int, **payload) -> Document:
        """
        Returns Document object.

        Payload:
        type: str : Document type. Types: in, out
        kind: str : Filter by document type. Types: invoice, shipment
        date: str : Document date. Format: YYYY-MM-DD
        template: str : Document template. Templates: ru, international
        from_contractor_id: int : Vendor counterparty ID
        from_requisite_id: int : Supplier details ID
        to_contractor_id: int : Buyer counterparty ID
        to_requisite_id: int : Buyer ID
        to_contractor_draft: str : Name of the receiving counterparty
        (for example, when it has not yet been created as a counterparty)
        number: str : Document Number
        status: str : Document status. Statuses: draft, published, viewed, paid, wrong
        comment: str : A comment
        description: str : Description
        model_type: str : The model to which the document will be bound, for example Order
        model_id: int : ID of the model to which the document will be linked
        """

        self.__validate_document_id(id_)

        response = self.request('PUT', f'{self.uri}/{str(id_)}', payload)

        return Document(**response)

    def delete_document(self, id_: int) -> Document:
        self.__validate_document_id(id_)

        return Document(**self.request('DELETE', f'{self.uri}/{str(id_)}'))

    def __validate_payload(self):
        pass

    @staticmethod
    def __validate_document_id(id_: int):
        if not isinstance(id_, int):
            raise TypeError('id_ must be a number')
