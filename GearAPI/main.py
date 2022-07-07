#Pydantic
from typing import Optional
from core.schemas.schemas import Client
#Fastapi
from fastapi import FastAPI, Body, Path, Query


app = FastAPI() # instancia de fastapi


# Path operations # path parameters /hola/{hola_id}

@app.get("/") #path operations decorator - permite acceder a un path ejecutando la def
def home(): #path operations function
    return {"mensaje": "Este es un mensaje jiejiejie!"}

# Request and Response Body

@app.post("/client/new", response_model=Client) # endpoint para crear un nuevo cliente 
#def create_userclient(client: Client = Body(...)):
def create_userclient(client: Client):
    return client

# Validaciones: Query parameters

@app.get("/client/detail")
def show_userclient(
    name: Optional[str] = Query(None, min_length=3, max_length=18), # Parametro opcional
    last_name: Optional[str] = Query(None, min_length=4, max_length=36),
    birthday: str = Query(None),
):
    return {"name": name, "last_name": last_name, "birthday": birthday}