from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from finolog.types.requisite_types import Requisite


class ContractorSummary(BaseModel):
    date: date
    currency_id: int
    balance: float
    incoming: int
    outcoming: int
    base_balance: float
    base_incoming: int
    base_outcoming: int
    contractor_id: int


class Contractor(BaseModel):
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
    deleted_at: Optional[datetime]
    deleted_by_id: Optional[int]
    alien_id: Optional[int]
    is_bizzed: bool
    group_id: Optional[int]
    autoeditor_id: Optional[int]
    summary: List[ContractorSummary]
    requisites: List[Requisite] = Field(default=list())
