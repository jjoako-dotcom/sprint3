# Calcula el score del torneo según salas, PCs y si las partidas comparten sala.
def calcular_score(sala_partida1, sala_partida2, pcs_sala1, pcs_sala2):
    score = 0

    if sala_partida1 == "Sin sala disponible para este turno":
        score = score - 30
    else:
        score = score + 20

    if sala_partida2 == "Sin sala disponible para este turno":
        score = score - 30
    else:
        score = score + 20

    if pcs_sala1 < 10:
        score = score - 20
    elif pcs_sala1 == 10:
        score = score + 25
    else:
        score = score + 15

    if pcs_sala2 < 10:
        score = score - 20
    elif pcs_sala2 == 10:
        score = score + 25
    else:
        score = score + 15

    if sala_partida1 == sala_partida2 and sala_partida1 != "Sin sala disponible para este turno":
        score = score - 45
    else:
        score = score + 10

    return score


# Busca una sala del turno indicado que no sea la excluida. Si no hay, devuelve el texto de "sin sala".
def buscar_sala(salas, turno, excluir):
    for i in range(len(salas)):
        nombre = "Sala " + str(i + 1)
        if salas[i][1] == turno and nombre != excluir:
            return nombre
    return "Sin sala disponible para este turno"


# Arma 2 partidas a partir de 4 equipos y les asigna sala. Cada partida queda como [equipo_a, equipo_b, turno, sala].
def generar_partidas(equipos, salas):
    rival = -1
    for i in range(1, len(equipos)):
        if rival == -1 and equipos[i][1] == equipos[0][1]:
            rival = i
    if rival == -1:
        return []

    restantes = []
    for i in range(1, len(equipos)):
        if i != rival:
            restantes.append(equipos[i])

    turno1 = equipos[0][1]
    turno2 = restantes[0][1]

    sala1 = buscar_sala(salas, turno1, "")
    sala2 = buscar_sala(salas, turno2, sala1)

    partida1 = [equipos[0][0], equipos[rival][0], turno1, sala1]
    partida2 = [restantes[0][0], restantes[1][0], turno2, sala2]
    return [partida1, partida2]