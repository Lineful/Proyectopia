from importlib.metadata import PathDistribution
from multiprocessing import connection
import uvicorn
import mysql.connector
from fastapi import *
from fastapi.templating import *
from fastapi.staticfiles import *
from static.PY.funcion_conexion import * 
from static.PY.funcion_insertar import *
from static.PY.funcion_actualizar import *

templates = Jinja2Templates(directory="C:/Users/Usuario/Music/Proyectopia/static")

app=APIRouter() 
app.mount("/static", StaticFiles(directory=r"C:\Users\Usuario\Music\Proyectopia\static"),name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/registrar")
def formularioregistrar(request: Request, nom: str = Form(...), ape: str = Form(...), id: str = Form(...), pas: str = Form(...), cargo: str = Form(...)):
    print("esta en la ruta principal")
     
    print(nom)
    print(ape)
    print(id)
    print(pas)
    print(cargo)

    insertar_variables_registro(nom, ape, id, pas, cargo)
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/registrarE")
def formularioregistrarE(request: Request, nom_e: str = Form(...), ape_e: str = Form(...), id_e: str = Form(...), grado: str = Form(...)):
    print("esta en la ruta principal")
     
    print(nom_e)
    print(ape_e)
    print(id_e)
    print(grado)

    insertar_variables_registroE(nom_e, ape_e, id_e, grado)
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/update")
def form_update(request: Request, identificacion: str=Form(...), nueva_contraseña: str=Form(...)):
    print("RUTA ACTUALIZAR")
    print(identificacion)
    print(nueva_contraseña)

    actualizar_datos(identificacion,nueva_contraseña)
    return templates.TemplateResponse("/index.html",{"request":request})

if __name__=='__main__':
    print("método principal")
    uvicorn.run(app,host="localhost", port=8022) 




