# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

Objetivo del proyecto : Con la intención de hacer un trabajo situándose en el rol de un **Data Engineer** ,se espera que alumno logre internalizar los conocimientos requeridos para la elaboración y ejecución de una API.

El trabajo consistió ,en una _primera parte_, de un proceso de limpieza y normalización de los datos, para luego realizar la consultas requeridas en las consignas del proyecto. Este proceso se encuentra disponible en el archivo **"ETL.ipynb"**

En una _segunda parte_ se realizó la tranformación los draframes resultantes del proceso de ETL, el data dataframe "df" y el "df_final", en archivos csv diferentes. Los mismos se encuentran disponibles en la carpera Dataset_Consultas y reciben el nombre de **"tabla_consultas.csv"** para el dataframe "df" y **"actores.csv"** para el dataframe "df_final". Este paso se realizó para poder disponer de los dataframes resultantes del ETL , en el archivo donde se realizan las consultas que es **consultas.py**

En un tercer momento, se crea la API en un entorno Docker, y se realizan las consultas de manera local.

y por último, y como parte del PLUS que prone este proyecto, se levanto la API en la nube, utilizando el servidor Mogenius.

_A continuación se detalla la URL de la API y los resultados esperados:_

_URL:_ http://pi01-data05-prod-apisup-dxd47n.mo1.mogenius.io

A) Máxima duración según tipo de film (película/serie), por plataforma y por año

http://pi01-data05-prod-apisup-dxd47n.mo1.mogenius.io/get_max_duration/anio/2018/plataforma/Hulu/min_or_season/min

Resultado esperado: 'La pelicula de mayor duración es : The House That Jack Built'

B) Cantidad de películas y series (separadas) por plataforma:

https://pi01-data05-prod-apisup-dxd47n.mo1.mogenius.io/get_count_plataform/plataforma/Netflix

Resultado esperado: {"Movie":6131,"TV Show":2676}

C) Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo:

https://pi01-data05-prod-apisup-dxd47n.mo1.mogenius.io/get_listedin/genero/Comedy

Resultado esperado: "La plataforma en la que más se repite el género Comedy es Amazon apareciendo 2099"

D) Actor que más se repite según plataforma y año:

https://pi01-data05-prod-apisup-dxd47n.mo1.mogenius.io/get_actor/plataforma/Netflix/anio/2018

Resultado esperado: "El/la actor/actriz que más se repite en la plataforma Netflix, en el año 2018, es: Andrea Libman apareciendo 8 veces"
