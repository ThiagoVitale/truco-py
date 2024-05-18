from functions import JuegoDeTruco

def main():
    juego = JuegoDeTruco()
    turno_inicial = juego.quien_comienza()
    print(f"Comienza {turno_inicial}")
    juego.jugar_ronda()

if __name__ == '__main__':
    main()
