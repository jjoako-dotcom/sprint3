from validaciones import es_turno_valido, es_nombre_valido, es_cantidad_pcs_valida


# Pide el nombre de un equipo y repite hasta que no esté vacío.
def pedir_nombre_equipo(numero):
    nombre = input("Ingrese el nombre del equipo " + str(numero) + ": ")
    while not es_nombre_valido(nombre):
        print("Error: El nombre no puede estar vacio.")
        nombre = input("Ingrese el nombre del equipo " + str(numero) + ": ")
    return nombre


# Pide el turno (mañana/tarde) y repite hasta que sea válido.
def pedir_turno(etiqueta):
    turno = input("Turno de " + etiqueta + " (mañana/tarde): ").lower()
    while not es_turno_valido(turno):
        print("Error: Solo se acepta escribir 'mañana' o 'tarde'.")
        turno = input("Turno de " + etiqueta + " (mañana/tarde): ").lower()
    return turno


# Pide la cantidad de PCs de una sala y repite hasta que sea mayor a 0.
def pedir_cantidad_pcs(numero):
    pcs = int(input("Cantidad de PCs Sala " + str(numero) + ": "))
    while not es_cantidad_pcs_valida(pcs):
        print("Error: Ingrese un numero mayor a 0.")
        pcs = int(input("Cantidad de PCs Sala " + str(numero) + ": "))
    return pcs


# Pide una opción del menú entre 1 y 7 y la devuelve.
def pedir_opcion():
    opcion = int(input("Seleccione una opcion (1 al 7): "))
    while opcion < 1 or opcion > 7:
        print("Error: Opcion invalida. Ingrese un numero del 1 al 7.")
        opcion = int(input("Seleccione una opcion (1 al 7): "))
    return opcion