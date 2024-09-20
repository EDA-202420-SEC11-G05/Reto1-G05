import sys
import App.logic as logic
from DataStructures.Lists import Array_list as lt
import os

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    data = logic.load_data(control, os.path.join('Data', "movies-small.csv"))
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    respuesta = logic.load_data(control)
    print(respuesta)

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    
    tm = int(input("Ingresa el tiempo minimo de las peliculas que desees buscar: "))
    pelicula,num = logic.req_1(control,tm)
    print("El total de peliculas que superan el tiempo indicado es: ",num)
    print("Y la pelicula más reciente es: ")
    print(pelicula)

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    idioma = input ("Ingresa el idioma de la pelicula que desees buscar: ")
    fi = input("Ingresa la fecha inicial que desees acotar: ")
    ff = input("Ingresa la fecha final que desees acotar: ")
    promedio, p_iniciales, p_finales, tamaño = logic.req_3(control, idioma, fi, ff)
    if tamaño > 20:
        print("Las primeras y ultimas 5 peliculas son: ")
        print(p_iniciales)
        print(p_finales)
        print("Fueron un total de ",tamaño,"peliculas que tuvieron un promedio de ", promedio, " minutos")
    else:
        print("Las peliculas son: ")
        print(p_iniciales)
        print("Fueron un total de ", tamaño, " que tuvieron un prmedio de duracion de" ,promedio," minutos")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    estado = input("Ingresa el estado de producción de la película: ")
    fi = input("Ingresa la fecha inicial que desees acotar: ")
    ff = input("Ingresa la fecha final que desees acotar: ")
    respuesta = logic.req_4(control, estado, fi, ff)
    print(respuesta)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    idioma = input("Ingresa el idioma de la película que desees buscar: ")
    ai = int(input("Ingresa el año que desees acotar: "))
    af = int(input("Ingresa el año que desees para acotar : "))
    respuesta = logic.req_6(control, idioma, ai, af)
    print("El diccionario de los años que estas buscando es: ")
    print(respuesta)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    prod_companie = input("Ingrese la compañia productora: ")
    ai = input("Ingrese el año inicial: ")
    af = input("Ingrese el año final: ")
    respuesta = logic.req_7(control, prod_companie, ai, af)
    print(respuesta)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
