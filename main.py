from inputs import pedir_opcion, pedir_nombre_equipo, pedir_turno, pedir_cantidad_pcs
from calculos import generar_partidas, calcular_score
from reglas import clasificar_score
from estadisticas import calcular_promedio, mostrar_grafico


# Muestra el menú de opciones del torneo.
def mostrar_menu():
    print("\n" + "=" * 35)
    print("--- TORNEO DE VALORANT (Sprint 3) ---")
    print("1. Registrar equipos")
    print("2. Registrar salas")
    print("3. Generar partidas")
    print("4. Mostrar partidas")
    print("5. Calcular score y guardar resultado")
    print("6. Ver Estadisticas y Grafico")
    print("7. Salir")
    print("=" * 35)


# Muestra cada partida con sus equipos, turno y sala.
def mostrar_partidas(partidas):
    for partida in partidas:
        print("Partida (" + partida[2].upper() + "):", partida[0], "vs", partida[1], "--> Sala:", partida[3])


# Ejecuta el programa: muestra el menú y responde a la opción elegida.
def main():
    equipos = []
    salas = []
    partidas = []
    scores = []
    cantidad_se_puede = 0
    cantidad_revisar = 0
    cantidad_no_se_puede = 0

    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            equipos = []
            for numero in range(1, 5):
                nombre = pedir_nombre_equipo(numero)
                turno = pedir_turno("equipo " + str(numero))
                equipos.append([nombre, turno])
            print("Equipos registrados:", len(equipos))
        elif opcion == 2:
            salas = []
            for numero in range(1, 3):
                pcs = pedir_cantidad_pcs(numero)
                turno = pedir_turno("sala " + str(numero))
                salas.append([pcs, turno])
            print("Salas registradas:", len(salas))
        elif opcion == 3:
            if len(equipos) == 0 or len(salas) == 0:
                print("Error: Faltan registrar equipos o salas.")
            else:
                partidas = generar_partidas(equipos, salas)
                if len(partidas) == 0:
                    print("No hay un rival del mismo turno para el equipo 1.")
                else:
                    mostrar_partidas(partidas)
        elif opcion == 4:
            if len(partidas) == 0:
                print("No hay partidas generadas todavia.")
            else:
                mostrar_partidas(partidas)
        elif opcion == 5:
            if len(partidas) == 0:
                print("Primero tenes que generar las partidas (opcion 3).")
            else:
                score = calcular_score(partidas[0][3], partidas[1][3], salas[0][0], salas[1][0])
                resultado = clasificar_score(score)
                scores.append(score)
                if resultado == "Se puede jugar bien":
                    cantidad_se_puede = cantidad_se_puede + 1
                elif resultado == "Revisar":
                    cantidad_revisar = cantidad_revisar + 1
                else:
                    cantidad_no_se_puede = cantidad_no_se_puede + 1
                print("Score total:", score)
                print("Resultado general:", resultado)
                print("(Resultado guardado en estadisticas.)")
        elif opcion == 6:
            if len(scores) == 0:
                print("Todavia no se calculo ningun score.")
            else:
                promedio = calcular_promedio(scores)
                print("Cantidad de escenarios calculados:", len(scores))
                print("Score promedio de los escenarios:", promedio)
                print("\n-- GRAFICO DE RESULTADOS --")
                mostrar_grafico(cantidad_se_puede, cantidad_revisar, cantidad_no_se_puede)
        elif opcion == 7:
            print("¡Hasta luego!")


main()