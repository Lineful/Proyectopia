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
from static.PY.funcion_borrar import *
from static.PY.selectlogin import *
from static.PY.funcion_insertarRE import *

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

    dates=insertar_variables_registroE(nom_e,ape_e,id_e,grado)

    if dates is not None and dates:
        print(dates[0][0])
        datos = { 
        'nombre': dates[0][0],
        'apellido': dates[0][1],
        'identificacion': dates[0][2],
        'grado': dates[0][3]
    }
    else:
        print("La función insertar_variables_registroE no ha devuelto ningún valor.")
        datos = None

        print(datos)


    return templates.TemplateResponse("/index.html", {"request": request, "datos": datos})

@app.post("/update")
def form_update(request: Request, identificacion: str=Form(...), nueva_contraseña: str=Form(...)):
    print("RUTA ACTUALIZAR")
    print(identificacion)
    print(nueva_contraseña)

    actualizar_datos(identificacion,nueva_contraseña)
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/borrar")
def form_delete(request: Request, identificacion: str=Form(...), contraseña: str=Form(...)):
    print("RUTA BORRAR")
    print(identificacion)
    print(contraseña)

    borrar_datos(identificacion,contraseña)
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/selectlogin") 
def form_login(request: Request, identificacion: str=Form(...), contraseña: str=Form(...) ):
    print(identificacion) 
    print(contraseña)

    if funcionlogin(identificacion, contraseña):
        #generar token
        return templates.TemplateResponse("/HTML/indexQR.html", {"request": request})

    else:
         return {"error": "Las credenciales no coinciden, no se puede iniciar sesión."}
         
@app.post("/registrarRE")
def formularioregistrar(request: Request, fecha_e: str = Form(...), descripcion: str = Form(...), n_r: str = Form(...), n_e: str = Form(...)):
    print("esta en la ruta principal")
     
    print(fecha_e)
    print(descripcion)
    print(n_r)
    print(n_e)

    insertar_variables_registro_re(fecha_e, descripcion, n_r, n_e)
    return templates.TemplateResponse("/HTML/indexQR.HTML",{"request":request})


if __name__=='__main__':
    print("método principal")
    uvicorn.run(app,host="localhost", port=8022) 




