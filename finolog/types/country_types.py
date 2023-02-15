from pydantic import BaseModel


class Country(BaseModel):
    id: int
    code: str
    default_currency_id: int
    name: str
