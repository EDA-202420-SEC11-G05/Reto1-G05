import time
import json
import csv
from datetime import datetime
from DataStructures.Lists import Array_list as lt

csv.field_size_limit(2147483647)

def create_json(id, name):
    newgenre = {'id': id,
                'name': name}
    return newgenre

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = lt.new_list()
    return catalog 

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    with open(filename, encoding='utf-8') as file:
        movies_file = csv.DictReader(file)
        for movie in movies_file:
            id = movie.get('id', 'Desconocido')
            title = movie.get('title', 'Desconocido')
            org_language = movie.get('original_language', 'Desconocido')
            release_date = movie.get('release_date', 'Desconocido')
            revenue = movie.get('revenue', 'Desconocido')
            runtime = movie.get('runtime', 'Desconocido')
            status = movie.get('status', 'Desconocido')
            vote_avg = movie.get('vote_average', 'Desconocido')
            vote_count = movie.get('vote_count', 'Desconocido')
            budget = movie.get('budget', 'Desconocido')
            profit = float(revenue) - float(budget)
            genre = json.loads(movie.get('genres', 'Desconocido'))
            companies = json.loads(movie.get('production_companies', 'Desconocido'))
            
            movie_info = {
                'id': id,
                'title': title,
                'original_language': org_language,
                'release_date': release_date,
                'revenue': revenue,
                'runtime': runtime,
                'status': status,
                'vote_average': vote_avg,
                'vote_count': vote_count,
                'budget': budget,
                'profit': profit,
                'production_companies': companies,
                'genre': genre
            }
            lt.add_last(catalog, movie_info)
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    return catalog[id]


def req_1(catalog, tm):
    """
    Retorna el resultado del requerimiento 1
    """
    peliculas_filtradas=lt.new_list()
    
    peliculas = catalog["elements"]
    for pelicula in peliculas:
        if float(pelicula["runtime"]) > tm:
            lt.add_last(peliculas_filtradas, pelicula)
            
    peliculas_filtradas["elements"].sort(key=lambda p: datetime.strptime(p["release_date"],'%Y-%m-%d'), reverse=True)
    
    if float(peliculas_filtradas['elements'][0]["revenue"]) == 0 or float(peliculas_filtradas['elements'][0]["budget"]) == 0:
        ganancias = 0
    else:
        ganancias = float(peliculas_filtradas['elements'][0]["revenue"]) - float(peliculas_filtradas['elements'][0]["budget"])
     
     
    pelicula_mas_reciente = {"Tiempo de duracion": peliculas_filtradas['elements'][0]["runtime"],
                             "Fecha de publiación de la pelicula" : peliculas_filtradas['elements'][0]["release_date"],
                             "Titulo original de la pelicula" : peliculas_filtradas['elements'][0]["title"],
                             "Presupuesto destinado a la realizacion de la pelicula" : peliculas_filtradas['elements'][0]["budget"],
                             "Dinero recaudado neto por la pelicula" : peliculas_filtradas['elements'][0]["revenue"],
                             "Ganancia final de una pelicula" : ganancias,
                             "Puntaje de calificación de la pelicula" : peliculas_filtradas['elements'][0]["vote_average"],
                             "Idioma original de publicación" : peliculas_filtradas['elements'][0]["original_language"]
                             }

    
    return pelicula_mas_reciente, peliculas_filtradas["size"]

    
    
            
            
            
                
                    
                
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, idioma, fi, ff):
    """
    Retorna el resultado del requerimiento 3
    """
    suma = 0
    fi_dt = datetime.strptime(fi,"%Y-%m-%d")
    ff_dt = datetime.strptime(ff,"%Y-%m-%d")
    
    peliculas_filtradas = lt.new_list()
    peliculas_filtradas_con_formato = lt.new_list()
    
    for pelicula in catalog["elements"]:
        
        if pelicula["original_language"] == idioma:
            if fi_dt<= datetime.strptime(pelicula["release_date"],"%Y-%m-%d") and datetime.strptime(pelicula["release_date"],"%Y-%m-%d") <= ff_dt:
               lt.add_last(peliculas_filtradas, pelicula) 
    
    for a in peliculas_filtradas["elements"]:
        
        if float(a["budget"]) == 0 or float(a["revenue"]):
            ganancias = 0
        else:
            ganancias = float(a["revenue"]-a["budget"])
        
        movie = {"Fecha de publicación de la película" : datetime.strptime(a["release_date"],"%Y-%m-%d"),
                 "Título original de la película" : a["title"],
                 "Presupuesto destinado a la realización de la película" : a["budget"],
                 "Dinero recaudado por la película" : a["revenue"],
                 "Ganancia de final de la película" : ganancias,
                 "Tiempo de duración en minutos de la pelicula" : a["runtime"],
                 "Puntaje de clasificación de la película" : a["vote_average"],
                 "Estado de la película" : a["status"]
                 }
        lt.add_last(peliculas_filtradas_con_formato, movie)
        suma += float(a["runtime"])
        
    promedio = suma / peliculas_filtradas_con_formato["size"]
        
    if peliculas_filtradas_con_formato["size"] > 20:
        p_iniciales = lt.sub_list(peliculas_filtradas_con_formato,1,5 )
        p_finales = lt.sub_list(peliculas_filtradas_con_formato,peliculas_filtradas_con_formato["size"]-5,peliculas_filtradas_con_formato["size"])
        return 
        
    promedio = suma / peliculas_filtradas_con_formato["size"]
    
    return promedio, 
        

        
        



def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
