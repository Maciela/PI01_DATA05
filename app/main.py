from fastapi import FastAPI 
import consultas
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def presentacion():
    return FileResponse("./Presentacion.md")

@app.get("/get_max_duration/anio/{anio}/plataforma/{plataforma}/min_or_season/{min_or_season}")
async def get_max_duration_controler(anio, plataforma, min_or_season):
    rta1= consultas.get_max_duration(int(anio), plataforma, min_or_season)
    return rta1

@app.get("/get_count_plataform/plataforma/{plataforma}")
async def get_count_plataform_controler(plataforma):
    rta2= consultas.get_count_plataform(plataforma)
    return rta2

@app.get("/get_listedin/genero/{genero}")
async def get_listedin_controler(genero):
    rta3= consultas.get_listedin(genero)
    return rta3
    
@app.get("/get_actor/plataforma/{plataforma}/anio/{anio}")
async def get_actor_controler(plataforma, anio):
    rta4= consultas.get_actor(plataforma, int(anio))
    return rta4
