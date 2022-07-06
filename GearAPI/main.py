from fastapi import FastAPI

app = FastAPI() # instancia de fastapi

# Path operations # path parameters /hola/{hola_id}
@app.get("/") #path operations decorator - permite acceder a un path ejecutando la def
def home(): #path operations function
    return {"mensaje": "Holanda po man, ya era hora!"}