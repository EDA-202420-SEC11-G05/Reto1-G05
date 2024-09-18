import time
import json
import csv
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
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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
