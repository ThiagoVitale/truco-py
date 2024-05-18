import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import os

class JuegoDeTruco:
    def __init__(self):
        self.humano_cartas = []
        self.maquina_cartas = []
        self.humano_puntos = 0
        self.maquina_puntos = 0
        self.turno_actual = ""
        self.cartas_total = [
            "1 de espada", "2 de espada", "3 de espada", "4 de espada", "5 de espada", "6 de espada",
            "7 de espada", "10 de espada", "11 de espada", "12 de espada", "1 de copa", "2 de copa",
            "3 de copa", "4 de copa", "5 de copa", "6 de copa", "7 de copa", "10 de copa", "11 de copa",
            "12 de copa", "1 de oro", "2 de oro", "3 de oro", "4 de oro", "5 de oro", "6 de oro",
            "7 de oro", "10 de oro", "11 de oro", "12 de oro", "1 de basto", "2 de basto", "3 de basto",
            "4 de basto", "5 de basto", "6 de basto", "7 de basto", "10 de basto", "11 de basto", "12 de basto"
        ]
        self.setup_gui()

    def quien_comienza(self):
        self.turno_actual = random.choice(["el humano", "la maquina"])
        return self.turno_actual

    def repartir_cartas(self):
        self.humano_cartas = random.sample(self.cartas_total, 3)
        for carta in self.humano_cartas:
            self.cartas_total.remove(carta)
        self.maquina_cartas = random.sample(self.cartas_total, 3)
        self.display_cartas()

    def get_image_path(self, carta):
        directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(directory, "images", f"{carta.replace(' ', '_')}.jpg")
        return image_path

    def display_cartas(self):
        for widget in self.humano_frame.winfo_children():
            widget.destroy()
        for carta in self.humano_cartas:
            image_path = self.get_image_path(carta)
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = ImageTk.PhotoImage(image.resize((100, 150)))
                button = tk.Button(self.humano_frame, image=image, command=lambda c=carta: self.jugar_carta(c))
                button.image = image  
                button.pack(side="left")
            else:
                messagebox.showerror("Error", f"Image not found: {image_path}")

    def jugar_carta(self, carta):
        if self.turno_actual == "el humano":
            self.humano_cartas.remove(carta)
            carta_2 = self.solicitar_carta_maquina()
            ganador_ronda = self.comparar_cartas(carta, carta_2)
            self.process_result(ganador_ronda)
            self.turno_actual = "la maquina"
        else:
            carta_2 = self.solicitar_carta_maquina()
            ganador_ronda = self.comparar_cartas(carta, carta_2)
            self.process_result(ganador_ronda)
            self.turno_actual = "el humano"

    def solicitar_carta_maquina(self):
        carta_a_tirar_maquina = random.choice(self.maquina_cartas)
        self.maquina_cartas.remove(carta_a_tirar_maquina)
        messagebox.showinfo("Turno de la maquina", f"La maquina tiró {carta_a_tirar_maquina}")
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

    def process_result(self, ganador_ronda):
        if ganador_ronda == "humano":
            self.humano_puntos += 1
            messagebox.showinfo("Resultado", "Ganaste la ronda")
        elif ganador_ronda == "maquina":
            self.maquina_puntos += 1
            messagebox.showinfo("Resultado", "Ganó la maquina la ronda")
        else:
            self.humano_puntos += 1
            self.maquina_puntos += 1
            messagebox.showinfo("Resultado", "Empate en la ronda")
        self.update_puntos()

    def update_puntos(self):
        self.puntos_label.config(text=f"Puntos humano: {self.humano_puntos}  Puntos maquina: {self.maquina_puntos}")
        if self.humano_puntos >= 2 or self.maquina_puntos >= 2:
            if self.humano_puntos > self.maquina_puntos:
                messagebox.showinfo("Juego terminado", "¡Ganaste la partida!")
            else:
                messagebox.showinfo("Juego terminado", "¡Ganó la maquina la partida!")
            self.humano_puntos = 0
            self.maquina_puntos = 0
            self.cartas_total = [
                "1 de espada", "2 de espada", "3 de espada", "4 de espada", "5 de espada", "6 de espada",
                "7 de espada", "10 de espada", "11 de espada", "12 de espada", "1 de copa", "2 de copa",
                "3 de copa", "4 de copa", "5 de copa", "6 de copa", "7 de copa", "10 de copa", "11 de copa",
                "12 de copa", "1 de oro", "2 de oro", "3 de oro", "4 de oro", "5 de oro", "6 de oro",
                "7 de oro", "10 de oro", "11 de oro", "12 de oro", "1 de basto", "2 de basto", "3 de basto",
                "4 de basto", "5 de basto", "6 de basto", "7 de basto", "10 de basto", "11 de basto", "12 de basto"
            ]
            self.repartir_cartas()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Juego de Truco")
        self.humano_frame = tk.Frame(self.root)
        self.humano_frame.pack(pady=20)
        self.puntos_label = tk.Label(self.root, text="Puntos humano: 0  Puntos maquina: 0")
        self.puntos_label.pack()
        self.repartir_cartas()
        self.root.mainloop()

        def get_image_path(carta):
            directory = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(directory, "images", f"{carta.replace(' ', '_')}.png")
            return image_path

        def display_cartas(self):
            for widget in self.humano_frame.winfo_children():
                widget.destroy()
            for carta in self.humano_cartas:
                image_path = get_image_path(carta)
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = ImageTk.PhotoImage(image.resize((100, 150)))
                    button = tk.Button(self.humano_frame, image=image, command=lambda c=carta: self.jugar_carta(c))
                    button.image = image  
                    button.pack(side="left")
                else:
                    messagebox.showerror("Error", f"Image not found: {image_path}")