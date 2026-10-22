# Calcula el promedio de una lista de scores. Si la lista está vacía, devuelve 0.
def calcular_promedio(scores):
    if len(scores) == 0:
        return 0
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)


# Muestra cuántos escenarios cayeron en cada categoría, con asteriscos.
def mostrar_grafico(cantidad_se_puede, cantidad_revisar, cantidad_no_se_puede):
    print("Se puede jugar    |", "*" * cantidad_se_puede)
    print("Revisar           |", "*" * cantidad_revisar)
    print("No se puede jugar |", "*" * cantidad_no_se_puede)
    