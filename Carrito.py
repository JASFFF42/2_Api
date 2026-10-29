from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Producto(BaseModel):
    nombre=str  
    precio=float=Field(ge=0)
    stock=int= Field(ge=0, lt=51)

datos = { 
    "nombre": "laptop",
    "precio": 15000.0,
    "stock": 5,
    }

#esto crea el objeto utilizando los datos

objeto=Producto(**datos)
objeto=Producto.model_validate(datos)

db= objeto
i=0
@app.get("/")
def saludar():
    return {"mensaje": "hola desde mi Api"}

#mostrar

@app.get("/db")
def mostrar():
    return{"db":db}

@app.post("/crear")
def crear_producto(datos:Producto):
    nuevo_producto={
        "id":i,
        **datos.model_validate()
    }
    db.append(nuevo_producto)
    i=i+1
    return{"mensaje":"elemento creado"}

@app.delete("/productos/{producto_id}")
def borrar(producto_id):
    for i in db:
        if i["id"] == producto_id:
            db.remove(i)
        return {"mensaje":"Producto eliminado"}