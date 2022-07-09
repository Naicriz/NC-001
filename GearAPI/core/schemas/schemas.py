"""
Los esquemas son los "modelos pydantic", los llamamos esquemas
porque en realidad es usado para crear "OpenAPI schemes", ya que
FastAPI está basado en las especificaciones de OpenAPI, en el 
cual se usan schemas en todas partes, desde "Swagger generation to 
endpoint's expected request body".
"""
#Python
from datetime import date
from enum import Enum
#Typing
from typing import Optional
from fastapi import Path
#Pydantic
from pydantic import BaseModel, EmailStr, Field, validator

class Gender(str, Enum):
    male = 'Másculino'
    female = 'Fémenino'
    other = 'Otro'
    not_given = 'not_given'


class Adress(BaseModel):
    street: str
    number: int
    city: str
    country: str

class Client(BaseModel):

    name: str = Field(
        ...,
        min_length=1,
        max_length=18
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=22
        )
    birthday: date
    
    @validator('birthday', pre=True, always=True)
    def ensure_date_range( cls, d):
        if not date(1950, 1, 1) <= d <= date.today():
            raise ValueError("Date out of range")
        return d

    gender: Gender = Field(None, alias='Gender')
    email: EmailStr
    phone: str
    address: Adress = Field(...)
    #address: Address = Field(None)
    class Config:
        schema_extra = {
            'example': {
                'name': 'Juan',
                'last_name': 'Perez',
                'birthday': '2020-01-01',
                'genre': 'Masculino',
                'email': 'example@example.com',
                'phone': '+56912345678',
                'address':  { 'street': 'Av. Lima', 'number': '123', 'city': 'Lima', 'country': 'Peru' }
            }
        }
