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

        self.validate_payload(
            payload=payload,
            types={
                'page': int,
                'pagesize': int,
                'query': str,
                'item_id': int,
                'kind': str,
                'template': str
            }
        )

        response = self.request('GET', self.uri, payload)

        return [Document(**obj) for obj in response]

    def get_document(self, id_: int) -> Document:
        self.validate_payload(
            payload={'id': id_},
            types={
                'id': int
            }
        )

        return Document(**self.request('GET', f'{self.uri}/{str(id_)}'))

    def get_document_pdf(self, id_: int, **payload) -> DocumentPDF:
        """
        Returns DocumentPDF object.

        Payload:
        no_sign: bool : Don't show print and signature in generated pdf
        """

        payload_copy = payload.copy()
        payload_copy['id'] = id_

        self.validate_payload(
            payload=payload_copy,
            types={
                'id': int,
                'no_sign': bool
            }
        )

        if 'no_sign' in payload:
            payload['no_sign'] = 'true' if payload['no_sign'] is True else 'false'

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

        if 'items' not in payload:
            raise ValueError('items not specified')

        self.validate_payload(
            payload=payload,
            types={
                'kind': str,
                'vat_type': str,
                'type': str,
                'date': str,
                'template': str,
                'from_contractor_id': int,
                'from_requisite_id': int,
                'to_contractor_id': int,
                'to_requisite_id': int,
                'to_contractor_draft': str,
                'number': str,
                'status': str,
                'comment': str,
                'description': str,
                'model_type': str,
                'model_id': int,
                'items': list
            }
        )

        self.validate_payload(
            payload=payload['items'],
            types={
                'id': int,
                'item_id': int,
                'count': int,
                'vat': int,
                'price': int,
                'price_currency_id': int,
                'amortization': int,
                'item_name': str
            }
        )

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

        payload_copy = payload.copy()
        payload_copy['id'] = id_

        self.validate_payload(
            payload=payload_copy,
            types={
                'type': str,
                'kind': str,
                'date': str,
                'template': str,
                'from_contractor_id': int,
                'from_requisite_id': int,
                'to_contractor_id': int,
                'to_requisite_id': int,
                'to_contractor_draft': str,
                'number': str,
                'status': str,
                'comment': str,
                'description': str,
                'model_type': str,
                'model_id': int
            }
        )

        response = self.request('PUT', f'{self.uri}/{str(id_)}', payload)

        return Document(**response)

    def delete_document(self, id_: int) -> Document:
        self.validate_payload(
            payload={'id': id_},
            types={
                'id': int
            }
        )

        return Document(**self.request('DELETE', f'{self.uri}/{str(id_)}'))
