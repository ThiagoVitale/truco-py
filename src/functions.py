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
            "1_de_espada", "2_de_espada", "3_de_espada", "4_de_espada", "5_de_espada", "6_de_espada",
            "7_de_espada", "10_de_espada", "11_de_espada", "12_de_espada", "1_de_copa", "2_de_copa",
            "3_de_copa", "4_de_copa", "5_de_copa", "6_de_copa", "7_de_copa", "10_de_copa", "11_de_copa",
            "12_de_copa", "1_de_oro", "2_de_oro", "3_de_oro", "4_de_oro", "5_de_oro", "6_de_oro",
            "7_de_oro", "10_de_oro", "11_de_oro", "12_de_oro", "1_de_basto", "2_de_basto", "3_de_basto",
            "4_de_basto", "5_de_basto", "6_de_basto", "7_de_basto", "10_de_basto", "11_de_basto", "12_de_basto"
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
        image_path = os.path.join(directory, "images", f"{carta}.jpg")
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
        
        for widget in self.maquina_frame.winfo_children():
            widget.destroy()
        for i in range(3):
            image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "red_back.jpg")
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = ImageTk.PhotoImage(image.resize((100, 150)))
                button = tk.Button(self.maquina_frame, image=image)
                button.image = image  
                button.pack(side="left")
            else:
                messagebox.showerror("Error", f"Image not found: {image_path}")

    def jugar_carta(self, carta):
        if self.turno_actual == "el humano":
            self.humano_cartas.remove(carta)
            for button in self.humano_frame.winfo_children():
                if button.cget("text") == carta:
                    button.destroy()
                    break
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
        self.maquina_cartas.append(None)  # Placeholder for the played card
        self.display_cartas()  # Update display after playing card
        return carta_a_tirar_maquina

    def comparar_cartas(self, carta1, carta2):
        orden_cartas = {
            "1_de_espada": 1, "1_de_basto": 2, "7_de_espada": 3, "7_de_oro": 4,
            "3_de_espada": 5, "3_de_copa": 5, "3_de_oro": 5, "3_de_basto": 5,
            "2_de_espada": 6, "2_de_copa": 6, "2_de_oro": 6, "2_de_basto": 6,
            "1_de_copa": 7, "1_de_oro": 7,
            "12_de_espada": 8, "12_de_copa": 8, "12_de_oro": 8, "12_de_basto": 8,
            "11_de_espada": 9, "11_de_copa": 9, "11_de_oro": 9, "11_de_basto": 9,
            "10_de_espada": 10, "10_de_copa": 10, "10_de_oro": 10, "10_de_basto": 10,
            "7_de_basto": 11, "7_de_copa": 11,
            "6_de_espada": 12, "6_de_copa": 12, "6_de_oro": 12, "6_de_basto": 12,
            "5_de_espada": 13, "5_de_copa": 13, "5_de_oro": 13, "5_de_basto": 13,
            "4_de_espada": 14, "4_de_copa": 14, "4_de_oro": 14, "4_de_basto": 14
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
                "1_de_espada", "2_de_espada", "3_de_espada", "4_de_espada", "5_de_espada", "6_de_espada",
                "7_de_espada", "10_de_espada", "11_de_espada", "12_de_espada", "1_de_copa", "2_de_copa",
                "3_de_copa", "4_de_copa", "5_de_copa", "6_de_copa", "7_de_copa", "10_de_copa", "11_de_copa",
                "12_de_copa", "1_de_oro", "2_de_oro", "3_de_oro", "4_de_oro", "5_de_oro", "6_de_oro",
                "7_de_oro", "10_de_oro", "11_de_oro", "12_de_oro", "1_de_basto", "2_de_basto", "3_de_basto",
                "4_de_basto", "5_de_basto", "6_de_basto", "7_de_basto", "10_de_basto", "11_de_basto", "12_de_basto"
            ]
            self.repartir_cartas()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Juego de Truco")

        self.maquina_frame = tk.Frame(self.root)
        self.maquina_frame.pack(pady=20)

        self.played_frame = tk.Frame(self.root)
        self.played_frame.pack(pady=20)

        self.humano_frame = tk.Frame(self.root)
        self.humano_frame.pack(pady=20)

        self.puntos_label = tk.Label(self.root, text="Puntos humano: 0  Puntos maquina: 0")
        self.puntos_label.pack()

        self.repartir_cartas()

        self.root.mainloop()

if __name__ == "__main__":
    juego = JuegoDeTruco()
