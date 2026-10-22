# Verifica que el turno sea 'mañana' o 'tarde'.
def es_turno_valido(turno):
    return turno == "mañana" or turno == "tarde"


# Verifica que el nombre no esté vacío.
def es_nombre_valido(nombre):
    return nombre != ""


# Verifica que la cantidad de PCs sea mayor a 0.
def es_cantidad_pcs_valida(pcs):
    return pcs > 0