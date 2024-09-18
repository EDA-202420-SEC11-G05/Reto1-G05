import time
import json
import csv
from DataStructures.Lists import Array_list as lt

csv.field_size_limit(2147483647)

movies = csv.DictReader(open('Data/movies-10.csv', encoding='utf-8'))

def create_json(id, name):
    newgenre = {'id': id,
                'name': name}
    return newgenre

def json_genre(movies):
    movies = csv.DictReader(open('Data/movies-10.csv', 'r', encoding='utf-8'))
    for movie in movies:
        genres_list = json.loads(movie['genres'])
        for genre in genres_list:
            genre = create_json(genre['id'], genre['name'])
    return genre

def json_prod_comp(movies):
    movies = csv.DictReader(open('Data/movies-10.csv', 'r', encoding='utf-8'))
    for movie in movies:
        prod_comp_list = json.loads(movie['production_companies'])
        for prod_comp in prod_comp_list:
            prod_comp = create_json(prod_comp['id'], prod_comp['name'])
    return prod_comp

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = lt.new_list()
    return catalog 

# Funciones para la carga de datos

def load_data(catalog, movies):
    """
    Carga los datos del reto
    """
    with open(movies, encoding='uft-8') as file:
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
            profit = revenue - budget
            
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
            }
            lt.add_last(catalog, movie_info)
    return catalog

catalog = new_logic(movies)
print(load_data(catalog, movies))
    
    

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
