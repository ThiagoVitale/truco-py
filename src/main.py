import time
import termcolor as colored
from functions import quien_comienza, repartir_cartas, solicitar_carta_jugador, solicitar_carta_maquina

def main():
    empieza = quien_comienza()
    if empieza == "el humano":
        print("Comenzas jugando vos")
        cartas_humano, cartas_maquina = repartir_cartas()
        time.sleep(1.5)  
        print("Tus cartas son: ")
        print(cartas_humano)
        print(solicitar_carta_jugador())
    elif empieza == "la maquina":
        print("Comienza jugando la maquina")
        cartas_humano, cartas_maquina = repartir_cartas()
        time.sleep(1.5)  
        print("Tus cartas son: ")
        print(cartas_humano)
        print(solicitar_carta_maquina())

if __name__ == '__main__':
    main()
