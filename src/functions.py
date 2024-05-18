import random
import time

class JuegoDeTruco:
    def __init__(self):
        self.humano_cartas = []
        self.maquina_cartas = []
        self.humano_puntos = 0
        self.maquina_puntos = 0
        self.turno_actual = ""

    def quien_comienza(self):
        self.turno_actual = random.choice(["el humano", "la maquina"])
        return self.turno_actual

    def repartir_cartas(self):
        cartas_total = [
            "1 de espada", "2 de espada", "3 de espada", "4 de espada", "5 de espada", "6 de espada",
            "7 de espada", "10 de espada", "11 de espada", "12 de espada", "1 de copa", "2 de copa",
            "3 de copa", "4 de copa", "5 de copa", "6 de copa", "7 de copa", "10 de copa", "11 de copa",
            "12 de copa", "1 de oro", "2 de oro", "3 de oro", "4 de oro", "5 de oro", "6 de oro",
            "7 de oro", "10 de oro", "11 de oro", "12 de oro", "1 de basto", "2 de basto", "3 de basto",
            "4 de basto", "5 de basto", "6 de basto", "7 de basto", "10 de basto", "11 de basto", "12 de basto"
        ]
        self.humano_cartas = random.sample(cartas_total, 3)
        for carta in self.humano_cartas:
            cartas_total.remove(carta)
        self.maquina_cartas = random.sample(cartas_total, 3)

    def solicitar_carta_jugador(self):
        while True:
            carta_a_tirar_jugador = input("¿Qué carta quieres tirar? ")
            if carta_a_tirar_jugador in self.humano_cartas:
                self.humano_cartas.remove(carta_a_tirar_jugador)
                return carta_a_tirar_jugador
            else:
                print("No tienes esa carta. Intenta de nuevo.")

    def solicitar_carta_maquina(self):
        carta_a_tirar_maquina = random.choice(self.maquina_cartas)
        self.maquina_cartas.remove(carta_a_tirar_maquina)
        return carta_a_tirar_maquina

    def comparar_cartas(self, carta1, carta2):
        orden_cartas = {
            "1 de espada": 1, "1 de basto": 2, "7 de espada": 3, "7 de oro": 4,
            "3 de espada": 5, "3 de copa": 5, "3 de oro": 5, "3 de basto": 5,
            "2 de espada": 6, "2 de copa": 6, "2 de oro": 6, "2 de basto": 6,
            "1 de copa": 7, "1 de oro": 7,
            "12 de espada": 8, "12 de copa": 8, "12 de oro": 8, "12 de basto": 8,
            "11 de espada": 9, "11 de copa": 9, "11 de oro": 9, "11 de basto": 9,
            "10 de espada": 10, "10 de copa": 10, "10 de oro": 10, "10 de basto": 10,
            "7 de basto": 11, "7 de copa": 11,
            "6 de espada": 12, "6 de copa": 12, "6 de oro": 12, "6 de basto": 12,
            "5 de espada": 13, "5 de copa": 13, "5 de oro": 13, "5 de basto": 13,
            "4 de espada": 14, "4 de copa": 14, "4 de oro": 14, "4 de basto": 14
        }
        valor_carta1 = orden_cartas[carta1]
        valor_carta2 = orden_cartas[carta2]
        if valor_carta1 < valor_carta2:
            return "humano"
        elif valor_carta1 > valor_carta2:
            return "maquina"
        else:
            return "empate"

    def jugar_ronda(self):
        self.repartir_cartas()
        time.sleep(1.5)
        print("Tus cartas son: ", self.humano_cartas)
        
        while self.humano_puntos < 2 and self.maquina_puntos < 2:
            if self.turno_actual == "el humano":
                carta_1 = self.solicitar_carta_jugador()
                carta_2 = self.solicitar_carta_maquina()
                print(f'La maquina tiró {carta_2}')
                ganador_ronda = self.comparar_cartas(carta_1, carta_2)
                if ganador_ronda == "humano":
                    self.humano_puntos += 1
                    print("Ganaste la ronda")
                    self.turno_actual = "el humano"
                elif ganador_ronda == "maquina":
                    self.maquina_puntos += 1
                    print("Ganó la maquina la ronda")
                    self.turno_actual = "la maquina"
                else:
                    self.humano_puntos += 1
                    self.maquina_puntos += 1
                    print("Empate en la ronda")
            else:
                carta_2 = self.solicitar_carta_maquina()
                print(f'La maquina tiró {carta_2}')
                carta_1 = self.solicitar_carta_jugador()
                ganador_ronda = self.comparar_cartas(carta_1, carta_2)
                if ganador_ronda == "humano":
                    self.humano_puntos += 1
                    print("Ganaste la ronda")
                    self.turno_actual = "el humano"
                elif ganador_ronda == "maquina":
                    self.maquina_puntos += 1
                    print("Ganó la maquina la ronda")
                    self.turno_actual = "la maquina"
                else:
                    self.humano_puntos += 1
                    self.maquina_puntos += 1
                    print("Empate en la ronda")
            print("Puntos humano: ", self.humano_puntos)
            print("Puntos maquina: ", self.maquina_puntos)
        if self.humano_puntos > self.maquina_puntos:
            print("¡Ganaste la partida!")
        else:
            print("¡Ganó la maquina la partida!")
