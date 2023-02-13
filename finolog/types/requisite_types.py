from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class Requisite(BaseModel):
    id: int
    contractor_id: int
    name: str
    description: Any
    full_name: Optional[str]
    inn: Any
    kpp: Any
    bank_name: Any
    bank_bic: Any
    bank_ks: Any
    bank_account: Any
    address_postal_index: Any
    address_city: Any
    address_street: Any
    created_at: str
    updated_at: str
    created_by_id: int
    updated_by_id: int
    deleted_at: Optional[datetime]
    deleted_by_id: Optional[int]
    email: Any
    web: Any
    phone: Any
    is_bizzed: bool
    bank_iban: Any
    bank_mfo: Any
    country_id: int
    biz_id: int
