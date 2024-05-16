import time
from functions import quien_comienza, repartir_cartas, solicitar_carta_jugador, solicitar_carta_maquina, comparar_cartas

def main():
    empieza = quien_comienza()

    if empieza == "el humano":
        humano_puntos = 0
        maquina_puntos = 0
        print("Comenzas jugando vos")
        cartas_humano, cartas_maquina = repartir_cartas()
        time.sleep(1.5)  
        print("Tus cartas son: ")
        print(cartas_humano)
        while humano_puntos < 2 and maquina_puntos < 2:
            carta_1 = solicitar_carta_jugador()
            carta_2 = solicitar_carta_maquina()
            print(f'La maquina tiro {carta_2}')

            gano_1 = comparar_cartas(carta_1, carta_2)
            if gano_1 == carta_1:
                humano_puntos += 1
                print("Ganaste")
                print("Puntos humano: ", humano_puntos)
                print("Puntos maquina: ", maquina_puntos)
            elif gano_1 == carta_2:
                maquina_puntos += 1
                print("Ganó la maquina")
                print("Puntos humano: ", humano_puntos)
                print("Puntos maquina: ", maquina_puntos)
            elif gano_1 == "Las cartas son iguales":
                humano_puntos += 1
                maquina_puntos += 1
                print("Empate en la primera ronda")
                print("Se determinará el ganador en la siguiente ronda")
                print("Puntos humano: ", humano_puntos)
                print("Puntos maquina: ", maquina_puntos)


    elif empieza == "la maquina":
        humano_puntos = 0
        maquina_puntos = 0
        print("Comienza jugando la maquina")
        cartas_humano, cartas_maquina = repartir_cartas()
        time.sleep(1.5)  
        print("Tus cartas son: ")
        print(cartas_humano)

        while humano_puntos < 2 and maquina_puntos < 2:
                carta_2 = solicitar_carta_maquina()
                print(f'La maquina tiro {carta_2}')
                carta_1 = solicitar_carta_jugador()

                gano_1 = comparar_cartas(carta_1, carta_2)
                if gano_1 == carta_1:
                    humano_puntos += 1
                    print("Ganaste")
                    print("Puntos humano: ", humano_puntos)
                    print("Puntos maquina: ", maquina_puntos)
                elif gano_1 == carta_2:
                    maquina_puntos += 1
                    print("Ganó la maquina")
                    print("Puntos humano: ", humano_puntos)
                    print("Puntos maquina: ", maquina_puntos)
                elif gano_1 == "Las cartas son iguales":
                    humano_puntos += 1
                    maquina_puntos += 1
                    print("Empate en la primera ronda")
                    print("Se determinará el ganador en la siguiente ronda")
                    print("Puntos humano: ", humano_puntos)
                    print("Puntos maquina: ", maquina_puntos)

if __name__ == '__main__':
    main()
