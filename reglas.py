# Clasifica el score: 99 o más es "Se puede jugar bien", 50 o más es "Revisar", y menos de 50 es "No se puede jugar".
def clasificar_score(score):
    if score >= 99:
        return "Se puede jugar bien"
    elif score >= 50:
        return "Revisar"
    else:
        return "No se puede jugar"
    