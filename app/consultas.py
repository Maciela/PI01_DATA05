#Librerias importadas:
import pandas as pd

#Ingesta de  lo csv a utilizar:
df = pd.read_csv("./Datasets_Consultas/tabla_consultas.csv")
df_final=pd.read_csv("./Datasets_Consultas/actores.csv")


##FUNCIONES PARA REALIZAR LAS CONSULTAS##

#Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser:
# get_max_duration(año, plataforma, [min o season])
def get_max_duration(anio, plataforma, min_or_season):
        df_rta=df[df['Plataforma'] == plataforma][df['release_year'] ==anio][df['min_or_season'] == min_or_season]
        rta=df_rta.groupby(['Plataforma', 'min_or_season', 'release_year'])['time'].idxmax()
        if min_or_season == "min":
            titulo_pelicula=df["title"].get(rta[0])
            return f'La pelicula de mayor duración es : {titulo_pelicula}'
        
        elif min_or_season == "Season":
            titulo_serie=df["title"].get(rta[0])
            return f'La serie de mayor cantidad de temporadas es : {titulo_serie}'
        else:
            return 'Los valores ingresados son incorrectos'

#Cantidad de películas y series (separadas) por plataforma El request debe ser: get_count_plataform(plataforma)
def get_count_plataform(plataforma):
    df_type_por_plataforma=df[df["Plataforma"] == plataforma]
    df_type= df_type_por_plataforma.groupby(["type"])["type"].count()
    return df_type.to_dict()

#Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
def get_listedin(genero):
    df1=df[df["listed_in"].str.contains(f'{genero}')]
    Rta=df1.groupby(["Plataforma"])["Plataforma"].count()
    nombre_plataforma=Rta.idxmax()
    genero_repetido=Rta[0]
    return f'La plataforma en la que más se repite el género {genero} es {nombre_plataforma} apareciendo {genero_repetido}'

#Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
def get_actor(plataforma, anio):
    condicion=df_final[df_final["año"]==anio][df_final["plataforma"]==plataforma]
    nombre_actor=condicion.groupby(["actor"])["actor"].count().idxmax()
    veces_repetido=condicion.groupby(["actor"])["actor"].count().max()
    return f'El/la actor/actriz que más se repite en la plataforma {plataforma}, en el año {anio}, es: {nombre_actor} apareciendo {veces_repetido} veces'
 