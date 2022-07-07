#Python3
from datetime import date
#Typing
from typing import Optional
#Pydantic
from core.schemas.schemas import Client, Adress
#Fastapi
from fastapi import FastAPI, Body, Query, Path


app = FastAPI() # instancia de fastapi


# Path operations # path parameters /hola/{hola_id}

@app.get("/") #path operations decorator - permite acceder a un path ejecutando la def
def home(): #path operations function
    return {"mensaje": "Este es un mensaje jiejiejie!"}

##REQUEST AND RESPONSE BODY - TEST EJEMPLO

#@app.post("/client/new")
@app.post("/client/new", response_model=Client)  
#def create_userclient(client: Client = Body(...)): # endpoint para crear un nuevo cliente
def create_userclient(client: Client):
    return client


# Validaciones: Query parameters - TEST EJEMPLO

@app.get("/client/detail")
def show_userclient(
    name: str = Query(None,
    min_length=3,
    max_length=18,
    title="Client Name",
    description="This is the name of the client. Required parameter(or will be).",
    ), 
    last_name: str = Query(None,
    min_length=4, 
    max_length=36,
    title="Client Last Name",
    description="This is the last name of the client. Required parameter(or will be)..",
    ), # Parametro opcional
    birthday: date = Query(...), #Se recomienda Path Parameters para elementos obligatorios
    genre: Optional[str] = Query(None) # Parametro opcional
):
    return {"name": name, "last_name": last_name, "birthday": birthday}


# Vaidaciones: Path parameters - TEST EJEMPLO

@app.get("/client/detail/{client_id}")
def show_userclient(
    client_id: int = Path(..., gt=0) # Parametro obligatorio, y que sea mayor a 0
):
    return { client_id: "Existe!"}

# Validation: Request Body - TEST EJEMPLO

@app.put("cliente/{client_id}") #se envia un json, luego lo trabaja en formato diccionario de python yluego se transforma y envie en son again.
def update_userclient(
    client_id: int = Path(
        ...,
        title="Client ID",
        description="This is the ID of the client. Required parameter(or will be).",
        gt=0
    ),
    client: Client = Body(...),
    adress: Adress = Body(...) 
):
#    results = client.dict() # se convierte a diccionario
#    results.update(adress.dict()) 
    results = client.dict() & adress.dict()
    return results

    # Validation: Models - Estan directamente relacionados con los request body - TEST EJEMPLO