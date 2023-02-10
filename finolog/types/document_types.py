from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class DocumentItemItem(BaseModel):
    id: int
    biz_id: int
    type: str
    sku: Any
    name: str
    description: Any
    price: int
    price_currency_id: int
    is_archived: bool
    created_at: datetime
    updated_at: datetime
    created_by_id: int
    updated_by_id: int
    deleted_at: Optional[datetime]
    deleted_by_id: Optional[int]
    vat: int
    unit_id: int
    initial_count: Any
    initial_price: Any
    initial_currency_id: Any
    can_edit_initial_balance: bool


class DocumentItem(BaseModel):
    id: int
    package_id: int
    item_id: int
    count: float
    price: float
    price_currency_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    created_by_id: int
    updated_by_id: int
    deleted_by_id: Optional[int]
    vat: int
    editable: bool
    project_id: Optional[int]
    item_name: str
    item_sku: Any
    item_type: str
    amortization: Any
    item: DocumentItemItem


class DocumentPackage(BaseModel):
    id: int
    biz_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    created_by_id: int
    updated_by_id: int
    deleted_by_id: Optional[int]
    currency_id: int
    total_price: float
    total_vat: int
    base_total_price: float
    vat_type: str
    base_total_vat: int
    items: List[DocumentItem]


class DocumentFromContractor(BaseModel):
    id: int
    biz_id: int
    name: str
    email: Any
    phone: Any
    person: Any
    description: Any
    created_at: datetime
    updated_at: datetime
    created_by_id: int
    updated_by_id: int
    deleted_at: datetime
    deleted_by_id: Any
    alien_id: Any
    is_bizzed: bool
    group_id: Any
    autoeditor_id: Any
    summary: List


class DocumentFromRequisite(BaseModel):
    id: int
    contractor_id: int
    name: str
    description: Any
    full_name: str
    inn: Any
    kpp: Any
    bank_name: Any
    bank_bic: Any
    bank_ks: Any
    bank_account: Any
    address_postal_index: Any
    address_city: Any
    address_street: Any
    created_at: datetime
    updated_at: datetime
    created_by_id: int
    updated_by_id: int
    deleted_at: datetime
    deleted_by_id: Any
    email: Any
    web: Any
    phone: Any
    is_bizzed: bool
    bank_iban: Any
    bank_mfo: Any
    country_id: int
    biz_id: int


class DocumentSummary(BaseModel):
    date: str
    currency_id: int
    balance: float
    incoming: int
    outcoming: int
    base_balance: float
    base_incoming: int
    base_outcoming: int
    contractor_id: int


class DocumentToContractor(BaseModel):
    id: int
    biz_id: int
    name: str
    email: Optional[str]
    phone: Optional[str]
    person: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    created_by_id: int
    updated_by_id: int
    deleted_at: datetime
    deleted_by_id: Any
    alien_id: Any
    is_bizzed: bool
    group_id: Optional[int]
    autoeditor_id: Any
    summary: List[DocumentSummary]


class Document(BaseModel):
    id: int
    biz_id: int
    kind: str
    from_contractor_id: Optional[int]
    from_requisite_id: Optional[int]
    to_contractor_id: Optional[int]
    to_requisite_id: Any
    package_id: int
    number: str
    date: str
    comment: Any
    description: Any
    status: str
    token: str
    pdf: Any
    payload: Any
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    created_by_id: int
    updated_by_id: int
    deleted_by_id: Optional[int]
    template: str
    file_id: Optional[int]
    model_id: Optional[int]
    model_type: Optional[str]
    to_contractor_draft: Optional[str]
    type: str
    qr_code_string: Optional[str]
    package: Optional[DocumentPackage]
    from_contractor: Optional[DocumentFromContractor]
    from_requisite: Optional[DocumentFromRequisite]
    to_contractor: Optional[DocumentToContractor]
    to_requisite: Any
    file: Any


class DocumentPDF(BaseModel):
    id: int = Field(..., alias='model_id')
    type: str = Field(..., alias='model_type')
    created_by_id: int
    original_name: str
    size: int
    updated_at: datetime
    created_at: datetime
    biz_id: int = Field(..., alias='id')
    url: str
