import time
import json
import csv

csv.field_size_limit(2147483647)

def new_list():
    newlist = {'elements': [],
               'size': 0}
    return newlist

def create_json():
    newgenre = {'id': None,
                'name': None}
    return newgenre

def json_genre(filename):
    movies = csv.DictReader(open(filename, encoding='utf-8'))
    for movie in movies:
        genres_list = json.loads(movie['genres'])
        for genre in genres_list:
            genre = create_json(genre['id'], genre['name'])
    return genre

def json_prod_comp(filename):
    movies = csv.DictReader(open(filename, encoding='utf-8'))
    for movie in movies:
        prod_comp_list = json.loads(movie['production_companie'])
        for prod_comp in prod_comp_list:
            prod_comp = create_json(prod_comp['id'], prod_comp['name'])
    return prod_comp

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {'id': None,
               'title': None,
               'original_language': None,
               'release_date': None,
               'revenue': None,
               'runtime': None,
               'status': None,
               'vote_average': None,
               'vote_count': None,
               'budget': None,
               'genres': None,
               'production_companies': None
               }
    catalog['id'] = new_list()
    catalog['title'] = new_list()
    catalog['original_language'] = new_list()
    catalog['release_date'] = new_list()
    catalog['revenue'] = new_list()
    catalog['runtime'] = new_list()
    catalog['status'] = new_list()
    catalog['vote_average'] = new_list()
    catalog['vote_count'] = new_list()
    catalog['budget'] = new_list()
    catalog['genres'] = json_genre()
    catalog['production_companies'] = json_prod_comp()
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


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
