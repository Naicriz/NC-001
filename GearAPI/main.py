#Python3
from datetime import date
#Typing
from typing import Optional

from pydantic import Field
#Pydantic
from core.schemas.schemas import Client, Adress
#Fastapi
from fastapi import FastAPI, Body, Query, Path


app = FastAPI() # Instancia de FastAPI


# Path operations # Path parameters /hola/{hola_id}

@app.get("/") #Path operations; decorator # Permite acceder a un path ejecutando la def
def home(): #Path operations; function
    return {"mensaje": "Este es un mensaje jiejiejie!"}

### REQUEST AND RESPONSE BODY EJEMPLOs ###

#@app.post("/client/new") # ALT 1.0 (Otra forma de definir el path) 
#def create_userclient(client: Client = Body(...)): # ALT 1.1 (Otra forma de crear la funcion)

@app.post("/user/new", response_model=Client)
# Endpoint para crear un nuevo cliente
def create_userclient(client: Client):
    return client


# Validaciones: Query parameters - TEST EJEMPLO

@app.get("/user/detail")
def show_userclient(
    name: str = Query(None,
    min_length=3,
    max_length=18,
    title="Client Name",
    description="This is the name of the client.",
    ),
    last_name: str = Query(None,
    min_length=4, 
    max_length=36,
    title="Client Last Name",
    description="This is the last name of the client.",
    ), # Parametro opcional
    birthday: Optional[str] = Path(...),#Se recomienda Path Parameters para elementos obligatorios
    gender: Optional[str] = Query(None) # type: ignore
):
    return {"name": name, "last_name": last_name, "birthday": birthday, "gender": gender}


# Validaciones: Path parameters - TEST EJEMPLO

@app.get("/user/{client_id}")
def show_userclient_id(
    client_id: int = Path(..., gt=0) # Parametro obligatorio, y que sea mayor a 0
):
    return { client_id: "Existe!"}

# Validación: Request Body - TEST EJEMPLO

@app.put("user/update/{client_id}") #se envia un json, luego lo trabaja en formato diccionario de python yluego se transforma y envie en son again.
def update_userclient(
    client_id: int = Path(
        ...,
        title="Client ID",
        description="This is the ID of the client that you want to update.",
        gt=0
    ),
    client: Client = Body(...)
    #adress: Adress = Body(...) 
):
### Formas en las que se pueden combinar diccionarios en python ###
    #results = client.dict() # se convierte a diccionario
    #results.update(adress.dict()) # se agrega el diccionario de adress
    #results = client.dict() and adress.dict()
    #results = dict(client.dict(), **adress.dict())

    results = dict(client)#.update(adress)
    return results

# Validación: Models - Estan directamente relacionados con los request body - TEST EJEMPLO
