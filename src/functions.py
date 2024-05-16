import random

humano_cartas = []
maquina_cartas = []

def quien_comienza():
    return random.choice(["el humano", "la maquina"])

def repartir_cartas():
    cartas_total = [
        "1 de espada", "2 de espada", "3 de espada", "4 de espada", "5 de espada", "6 de espada",
        "7 de espada", "10 de espada", "11 de espada", "12 de espada", "1 de copa", "2 de copa",
        "3 de copa", "4 de copa", "5 de copa", "6 de copa", "7 de copa", "10 de copa", "11 de copa",
        "12 de copa", "1 de oro", "2 de oro", "3 de oro", "4 de oro", "5 de oro", "6 de oro",
        "7 de oro", "10 de oro", "11 de oro", "12 de oro", "1 de basto", "2 de basto", "3 de basto",
        "4 de basto", "5 de basto", "6 de basto", "7 de basto", "10 de basto", "11 de basto", "12 de basto"
    ]
    for i in range(3):
        carta_humano = cartas_total.pop(random.randint(0, len(cartas_total)-1))
        humano_cartas.append(carta_humano)
        carta_maquina = cartas_total.pop(random.randint(0, len(cartas_total)-1))
        maquina_cartas.append(carta_maquina)
    return humano_cartas, maquina_cartas

def solicitar_carta_jugador():
    carta_a_tirar_jugador = input("¿Qué carta quieres tirar? ")
    while carta_a_tirar_jugador not in humano_cartas:
        carta_a_tirar_jugador = input("No tienes esa carta. ¿Qué carta quieres tirar? ")
    humano_cartas.remove(carta_a_tirar_jugador)
    return carta_a_tirar_jugador

def solicitar_carta_maquina():
    carta_a_tirar_maquina = random.choice(maquina_cartas)
    maquina_cartas.remove(carta_a_tirar_maquina)
    return carta_a_tirar_maquina

def comparar_cartas(carta1, carta2):
    orden_cartas = {
    "1 de espada": 1,
    "1 de basto": 2,
    "7 de espada": 3,
    "7 de oro": 4,
    "3 de espada": 5,"3 de copa": 5,"3 de oro": 5,"3 de basto": 5,
    "2 de espada": 6,"2 de copa": 6,"2 de oro": 6,"2 de basto": 6,
    "1 de copa": 7,"1 de oro": 7,
    "12 de espada": 8,"12 de copa": 8, "12 de oro": 8,"12 de basto": 8,
    "11 de espada": 9,"11 de copa": 9,"11 de oro": 9,"11 de basto": 9,
    "10 de espada": 10,"10 de copa": 10,"10 de oro": 10,"10 de basto": 10,
    "7 de basto": 11,"7 de copa": 11,
    "6 de espada": 12,"6 de copa": 12,"6 de oro": 12,"6 de basto": 12,
    "5 de espada": 13,"5 de copa": 13,"5 de oro": 13,"5 de basto": 13,
    "4 de espada": 14,"4 de copa": 14,"4 de oro": 14,"4 de basto": 14
    }

    valor_carta1 = orden_cartas[carta1]
    valor_carta2 = orden_cartas[carta2]
    
    if  valor_carta1 < valor_carta2:
        return carta1
    elif  valor_carta1 > valor_carta2:
        return carta2
    else:
        return "Las cartas son iguales"

def solicitar_envido():
    elección = input("¿Quieres cantar envido? (s/n) ")
    if elección == "s":
        return True
    else:
        return False

def solicitar_truco():
    elección = input("¿Quieres cantar truco? (s/n) ")
    if elección == "s":
        return True
    else:
        return False

def solicitar_real_envido():
    elección = input("¿Quieres cantar real envido? (s/n) ")
    if elección == "s":
        return True
    else:
        return False

def solicitar_falta_envido():
    elección = input("¿Quieres cantar falta envido? (s/n) ")
    if elección == "s":
        return True
    else:
        return False