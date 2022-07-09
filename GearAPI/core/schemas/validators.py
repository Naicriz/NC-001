from datetime import date

from pydantic import validator
from pydantic.dataclasses import dataclass




"""
@dataclass
class DemoDataclass:
    ts: date = None  # type: ignore

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or date.today()

print(DemoDataclass())
"""
#Create a validator of phone numbers with codes of FastAPI with pydantic
#@validator('phone', pre=True, always=True)
#def validate_phone(cls, v):
#    if not v.startswith('+'):
#        raise ValueError('Phone number must start with +')
#    return v