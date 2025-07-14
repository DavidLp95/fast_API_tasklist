from fastapi import FastAPI,Request, Form #libreria para crear la api
#validacion de datos 
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.responses import HTMLResponse #libreria para respuestas HTML
from fastapi.templating import Jinja2Templates #libreria para plantillas HTML
from fastapi.staticfiles import StaticFiles



#construcion de fast api                                                            estructura de una fast api 
app = FastAPI()#-----

templates = Jinja2Templates(directory="templates" ) # ruta de las plantillas HTML ------
app.mount("/static", StaticFiles(directory="statics"), name="static") # ruta de los archivos estaticos (CSS, JS, etc.) ------

#se define el modelo de datos para la tarea
class Tarea(BaseModel):
	titulo: str
	descripcion: Optional[str] = None
	estado: str
	fecha_creacion: str
       



#base de datos en memoria para almacenar las tareas (replazar por posgresql o mysql en produccion)-------------------
lista_tareas =[]



@app.get("/", response_class=HTMLResponse) #ruta para la pagina principal
async def leer_html(request: Request):
     return templates.TemplateResponse("index.html", {"request": request, "tareas": lista_tareas}) 
     


# Ruta para crear tarea
@app.post("/crear-tarea/") # se agrega por parametros de la funcion 
async def crear_tarea(
      request: Request,
      titulo: str = Form(...),
      descripcion: Optional[str] = Form(None),
      estado: str = Form(...),
      fecha_creacion: str = Form(...)
):
      nueva_tarea = Tarea(
            titulo = titulo,
            descripcion = descripcion,
            estado = estado,
            fecha_creacion = fecha_creacion
            
      )
      lista_tareas.append(nueva_tarea)  # Agregar la nueva tarea a la lista
      return templates.TemplateResponse("index.html", {"request": request, "tareas": lista_tareas, "mensaje": "Tarea creada exitosamente"})


@app.delete("/eliminar-tarea/{titulo}")  # Ruta para eliminar una tarea por título ---------------------aun no esta borrando--------------------------
async def eliminar_tarea(titulo: str):
    global lista_tareas
    lista_tareas = [tarea for tarea in lista_tareas if tarea.titulo == titulo]
    return {"mensaje": f"Tarea '{titulo}' eliminada exitosamente"}


@app.put("/actualizar-tarea/{titulo}")  # Ruta para actualizar una tarea por título / terminar la actualizacion 
def actualizar_tarea():
      pass


# @app.get("/obtener_tarea/", response_class=HTMLResponse)
# async def ver_datos(
#         request: Request
# ):
#       return templates.TemplateResponse("ver_datos.html", {"request": request, "tareas": lista_tareas})






#   FUNCIONES PARA CONSOLA Y VALIDACION DE DATOS
# def crear_tarea(tarea: Tarea):
#     if tarea.estado.lower() not in estados_validos:
#         return {"error": f"Estado inválido. Debe ser uno de estos: {estados_validos}"}
    
#     tarea.estado = tarea.estado.lower()
#     lista_tareas.append(tarea)
#     return {"mensaje": "Tarea creada exitosamente", "tarea": tarea}

# Ruta para obtener todas las tareas	
# @app.get("/obtener_datos/")
# def nueva_tarea(nueva_tarea: Tarea ):
#    return {Tarea: lista_tareas}  # Retorna la lista de tareas almacenadas


# Iniciar servidor
if __name__ == "__main__":
      uvicorn.run(app, host="127.0.0.1", port=8000,  reload=True)




# def  VALIDACION_DEL_ESTADO(Tarea):
# 	if Tarea.ESTADO not in ['pendiente', 'en progreso', 'completado']:
#             print("Estado inválido. Debe ser 'pendiente', 'en progreso' o 'completado'.")
#         else:
#             #paso dos: crear un diccionario con los datos de la tarea
#             tareas = {

#             "TITULO": "",
#             "DESCRIPCION": "",
#             "ESTADO": "list[str]=['pendiente', 'en progreso', 'completado']" ,# lista para pendientes estructura de una lista de tareas
#             "FECHA_CREACION": ""

#     }
			
# def agregar_la_tarea(VALIDACION_DEL_ESTADO, Tareas):
#             VALIDACION_DEL_ESTADO.lista_tareas =[]
#             VALIDACION_DEL_ESTADO.lista_tareas.append(VALIDACION_DEL_ESTADO.tareas)
#             print("Tarea agregada exitosamente.")
			
	
	


# #ruta para ver todas las tareas
# @app.get('/')
# def obtener_tareas(tareas: Tarea):
#     VALIDACION_DEL_ESTADO.lista_tareas =[]
#     VALIDACION_DEL_ESTADO.lista_tareas.append(VALIDACION_DEL_ESTADO.tareas)
#     return {"mensaje": "Tarea recibida", "tarea": tareas.dict()}
			
#     # Aquí puedes agregar la lógica para almacenar la tarea recibida
#     # Por ejemplo, podrías guardar la tarea en una lista global (no recomendado para producción)
    





# @app.get('/obtener_tareas/')
# def nueva_tarea():
# 	return{'tarea': 'obteniendo tareas'}
	


# if __name__ == "__main__":
# 	uvicorn.run(app, host="http://127.0.0.1/8000", port=8000)
  


