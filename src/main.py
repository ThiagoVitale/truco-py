from functions import JuegoDeTruco
from tkinter import messagebox

def main():
    juego = JuegoDeTruco()
    turno_inicial = juego.quien_comienza()
    messagebox.showinfo("Turno inicial", f"Comienza {turno_inicial}")

if __name__ == '__main__':
    main()