#Pydantic
from core.schemas.schemas import Client
#Fastapi
from fastapi import Body, FastAPI

app = FastAPI() # instancia de fastapi

#BaseModel of a client for recauding information for marketing porpuses

@app.post("/clients/new") # endpoint para crear un nuevo cliente 
def create_userclient(client: Client = Body(...)):
    return client

# Path operations # path parameters /hola/{hola_id}
@app.get("/") #path operations decorator - permite acceder a un path ejecutando la def
def home(): #path operations function
    return {"mensaje": "Holanda po man, ya era hora!"}