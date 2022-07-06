"""
Los esquemas son los "modelos pydantic", los llamamos esquemas
porque en realidad es usado para crear "OpenAPI schemes", ya que
FastAPI está basado en las especificaciones de OpenAPI, en el 
cual se usan schemas en todas partes, desde "Swagger generation to 
endpoint's expected request body".
"""
#Python
from datetime import date
from typing import Optional
#Pydantic
from pydantic import BaseModel


class Client(BaseModel):
    name: str
    last_name: str
    birthday: date = None
    genre: Optional[str] = None
    email: str
    phone: str
    adress: str