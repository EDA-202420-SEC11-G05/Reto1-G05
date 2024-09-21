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
    # se abre el archivo csv
    with open(filename, encoding='utf-8') as file:
        movies_file = csv.DictReader(file)
        # se recorre el archivo 
        for movie in movies_file:
            # se extraen todos los datos de cada pelicula
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
            # se crea un diccionario para cada pelicula
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
            # se agrega la pelicla al catalogo
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
        
        if float(a["budget"]) == 0 or float(a["revenue"]) == 0:
            ganancias = 0
        else:
            ganancias = float(a["revenue"])-float(a["budget"])
        
        movie = {"Fecha de publicación de la película" : a["release_date"],
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
    else:
        p_iniciales = peliculas_filtradas_con_formato
        p_finales = peliculas_filtradas_con_formato
                
        
    promedio = suma / peliculas_filtradas_con_formato["size"]
    
    return promedio, p_iniciales, p_finales, peliculas_filtradas_con_formato["size"]
        

def req_4(catalog, estado, fi, ff):
    """
    Retorna el resultado del requerimiento 4
    """
    # se crea un una lista que guardara las peliculas que cumplen los criterios
    pelis = []
    # se crea una variable para sumar la duracion de todas las peliculas que cumplan los criterios
    total_duracion = 0
    # se crea una variable que suma las peliculas que cumplen los criterios
    total_pelis = 0
    # se convierten "fi" y "ff" a obajetos tipo datetime para poder hacer comparaciones de fechas
    fecha_i = datetime.strptime(fi, "%Y-%m-%d")
    fecha_f = datetime.strptime(ff, "%Y-%m-%d")
    # se recorre todo el catalogo
    for movie in catalog['elements']:
        # se saca el status y la fecha de publicacion de cada pelicula
        status = movie['status']
        release_date = movie['release_date']
        # se compara si el estado de la pelicula es igual al requerido
        if status == estado:
            # se saca la fecha de publicacion de cada pelicula en tipo datetime
            fecha_publicacion = datetime.strptime(release_date, "%Y-%m-%d")
            # se compara si la fecha de publicacion de la pelicula esta en el rango de fechas dadas
            if fecha_i <= fecha_publicacion <= fecha_f:
                # se agrega la pelicula a la lista "pelis"
                pelis.append(movie)
                # se suma la duracion de las peliculas y se suma el conteo total de peliculas que cumplen con los criterios dados
                duracion_movie = movie.get('runtime', 'Desconocido')
                if duracion_movie != 'Desconocido':
                    total_duracion += float(duracion_movie)
                total_pelis += 1
    # se calcula la duracion promedio de todas las peliculas
    if total_pelis > 0:
        tiempo_promedio = total_duracion / total_pelis
    # si no se encuentra ninguna pelicula es promedio es 0
    else:
        tiempo_promedio = 0
    # si la lista de peliculas tiene mas de 20 peliculas se guardan solo las primeras 5 y las ultimas 5
    if len(pelis) > 20:
        pelis_resultado = pelis[:5] + pelis[-5:]
    # si hay menos de 20 se guardan todas las peliculas
    else:
        pelis_resultado = pelis
    # se crea el diccionario que se va a retornar
    resultado = {
        'total_peliculas': total_pelis,
        'tiempo_promedio': tiempo_promedio,
        # la lista de diccionarios con los detalles de todas las peliculas que cumplen los criterios
        'peliculas': [{
            'fecha_publicacion': movie['release_date'],
            'titulo': movie['title'],
            'presupuesto': movie['budget'],
            'recaudado': movie['revenue'],
            'ganancia': movie['profit'],
            'duracion': movie['runtime'],
            'calificacion': movie['vote_average'],
            'idioma': movie['original_language']
        } for movie in pelis_resultado]
    }
    return resultado


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, idioma, ai, af):
    """
    Retorna el resultado del requerimiento 6
    """
    
    peliculas_filtradas = lt.new_list()
    diccionario = {}
    suma_votos = 0
    suma_tiempo = 0
    
    for pelicula in catalog["elements"]:
        if pelicula["original_language"] == idioma:
            if int(ai) < datetime.strptime(pelicula['release_date'], '%Y-%m-%d').year and datetime.strptime(pelicula['release_date'], '%Y-%m-%d').year < int(af):
                lt.add_last(peliculas_filtradas,pelicula)
                
    diccionario = {datetime.strptime(peliculas_filtradas["elements"][0]['release_date'], '%Y-%m-%d').year : [peliculas_filtradas["elements"][0]]}
    
    for pelicula in peliculas_filtradas["elements"]:
        if datetime.strptime(pelicula['release_date'], '%Y-%m-%d').year in diccionario:
            diccionario[datetime.strptime(pelicula['release_date'], '%Y-%m-%d').year].append(pelicula)
        else:
            diccionario[datetime.strptime(pelicula['release_date'], '%Y-%m-%d').year] = [pelicula]
            

    
    for ano in diccionario:
        for i in range(0,len(diccionario[ano])):
            mejor = float(diccionario[ano][0]["vote_average"])
            mejor_nombre = diccionario[ano][0]["title"]
            peor = float(diccionario[ano][0]["vote_average"])
            peor_nombre = diccionario[ano][0]["title"]
            if float(diccionario[ano][i]["vote_average"]) > mejor:
                mejor = float(diccionario[ano][i]["vote_average"])
                mejor_nombre = diccionario[ano][i]["title"]
            if float(diccionario[ano][i]["vote_average"]) < peor:
                peor = float(diccionario[ano][i]["vote_average"])
                peor_nombre = diccionario[ano][i]["title"]
            suma_votos = suma_votos+float(diccionario[ano][i]["vote_average"])
            promedio_votos = suma_votos/len(diccionario[ano])
            suma_tiempo = suma_tiempo+float(diccionario[ano][i]["runtime"])
            promedio_tiempo = suma_tiempo/len(diccionario[ano])
            definitivo = {ano: {"El año del listado": ano,
                                "Total de películas": len(diccionario[ano]),
                                "Promedio de la votación promedio": promedio_votos,
                                "Tiempo promedio": promedio_tiempo,
                                "Ganancias acumuladas" : 0,
                                "Mejor pelicula": (mejor,mejor_nombre),
                                "Poer pelicula" : (peor,peor_nombre)}}
    
    return definitivo
            

def req_7(catalog, prod_companie, ai, af):
    """
    Retorna el resultado del requerimiento 7
    """
    # se crea un diccionario para almacenar las peliculas por cada
    peliculas = {}
    # se recorren todas las peliculas en catalog
    for movie in catalog['elements']:
        # se saca el estado, la fecha de publicacion y la compañia de cada pelicula
        estado = movie['status']
        fecha_publicacion = movie['release_date']
        companias = movie['production_companies']
        # si el estado de la pelicula es Released continua
        if estado == 'Released':
            # se saca el año en que se publico la pelicula
            anio_publicacion = str(datetime.strptime(fecha_publicacion, "%Y-%m-%d").year)
            # se compara el año de publicacion para compararlo con el rango de años dados 
            if ai <= anio_publicacion <= af:
                # se recorren la compañia de la pelicula y luego se compara con la compañia
                for compania in companias:
                    if compania['name'] == prod_companie:
                        # si el año de la pelicula no existe en "peliculas" se crea 
                        if anio_publicacion not in peliculas:
                            peliculas[anio_publicacion] = {
                                'total_peliculas': 0,
                                'votaciones': 0,
                                'duracion': 0,
                                'ganancias': 0,
                                'peliculas': []
                            }
                        # se añade la pelicula a "peliculas" segun el año de publicacion
                        peliculas[anio_publicacion]['total_peliculas'] += 1
                        # se extraen los datos importantes de la pelicula
                        votacion = float(movie['vote_average'])
                        duracion = float(movie['runtime'])
                        presupuesto = float(movie['budget'])
                        revenue = float(movie['revenue'])
                        ganancia = revenue - presupuesto
                        # se agregan esos datos a los totales por año
                        peliculas[anio_publicacion]['votaciones'] += votacion
                        peliculas[anio_publicacion]['duracion'] += duracion
                        peliculas[anio_publicacion]['ganancias'] += ganancia
                        # se guardan los datos de cada pelicula en la lista de cada año
                        peliculas[anio_publicacion]['peliculas'].append({
                            'titulo': movie['title'],
                            'votacion': votacion,
                            'duracion': duracion,
                            'ganancias': ganancia
                        })
                        
    resultado = {}
    # se recorre el diccionario "peliculas"
    for anio, data in peliculas.items():
        # se calculan los datos agregados para cada año
        total_pelis = data['total_peliculas']
        promedio_votacion = data['votaciones'] / total_pelis if total_pelis > 0 else 0
        promedio_duracion = data['duracion'] / total_pelis if total_pelis > 0 else 0
        total_ganancias = data['ganancias']
        # se busca la mejor y peor pelicula basandose en la votacion
        mejor_peli = data['peliculas'][0]
        peor_peli = data['peliculas'][0]
        for pelicula in data['peliculas']:
            if pelicula['votacion'] > mejor_peli['votacion']:
                mejor_peli = pelicula
            if pelicula['votacion'] < peor_peli['votacion']:
                peor_peli = pelicula
        # se guardan los resultados en un nuevo diccionario
        resultado[anio] = {
            'total_peliculas': total_pelis,
            'votacion_promedio': promedio_votacion,
            'duracion_promedio': promedio_duracion,
            'ganancias_totales': total_ganancias,
            'mejor_pelicula': mejor_peli,
            'peor_pelicula': peor_peli
        }
    return resultado


def req_8(catalog, anio, genre):
    """
    Retorna el resultado del requerimiento 8
    """
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
