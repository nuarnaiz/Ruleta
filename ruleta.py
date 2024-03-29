import tkinter as tk
import random
import math

class RuletaCasino:
    def __init__(self, master):
        self.master = master
        self.master.title("Ruleta de Casino")
        self.master.geometry("800x800")

        self.canvas = tk.Canvas(self.master, width=700, height=700)
        self.canvas.pack()

        self.btn_spin = tk.Button(self.master, text="Girar", command=self.girar_ruleta)
        self.btn_spin.pack(pady=20)

        self.resultado_label = tk.Label(self.master, text="")
        self.resultado_label.pack(pady=20)

    def girar_ruleta(self):
        self.resultado_label.config(text="")
        self.canvas.delete("all")

        # Números en la ruleta
        numeros = list(range(0, 37))

        # Color de cada número en la ruleta
        colores = ["green"] + ["red", "black"] * 18 + ["red", "black"]
        numeros=[32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26,0]
        # Seleccionar un número aleatorio
        numero_ganador = random.choice(numeros)

        # Dibujar la ruleta
      
        radio_exterior = 350
        radio_interior = 150

        for i in range(0, 37):
            start_angle = i * (360 / 37)
            end_angle = (i + 1) * (360 / 37)
            # Dibujamos el arco
            self.canvas.create_arc(10, 10, 700, 700, start=start_angle, extent=(360 / 37), fill=colores[i])
            # Calculamos el centro del gajo
            centro_angle = (start_angle + end_angle) / 2
            centro_x = 350 + (radio_exterior + radio_interior) / 2 * math.cos(math.radians(centro_angle))
            centro_y = 350 + (radio_exterior + radio_interior) / 2 * math.sin(math.radians(centro_angle))

        # Dibujar los números encima de los colores
        for i in range(0, 37):
            start_angle = i * (360 / 37)
            end_angle = (i + 1) * (360 / 37)
            # Calculamos el centro del gajo
            centro_angle = (start_angle + end_angle) / 2
            centro_x = 350 + (radio_exterior + radio_interior) / 2 * math.cos(math.radians(centro_angle))
            centro_y = 350 + (radio_exterior + radio_interior) / 2 * math.sin(math.radians(centro_angle))
            # Dibujamos el número encima del color
            self.canvas.create_text(centro_x, centro_y, text=str(numeros[i]), font=("Arial", 12),fill="blue")

        angulo_flecha = numero_ganador * (360 / 37) + (360 / 37 / 2)

# Si el ángulo de la flecha es exacto al cambio de sector circular,
# centrar las coordenadas en el punto medio de ese sector
        if angulo_flecha % (360 / 37) == 0:
            angulo_flecha += (360 / 37) / 2

# Convertir el ángulo a radianes
        angulo_radianes = math.radians(angulo_flecha)

# Calcular las coordenadas finales de la flecha
        longitud_flecha=200
        x_final = 350 +longitud_flecha * math.cos(angulo_radianes)
        print(math.cos(angulo_radianes))
        y_final = 350 -longitud_flecha * math.sin(angulo_radianes)
        # Dibujar la flecha que indica el número ganador
        #self.canvas.create_line(355, 355, x_final, y_final, arrow=tk.LAST, width=2, fill="blue")
        self.canvas.create_line(355, 355, x_final,y_final , arrow=tk.LAST, width=2, fill="blue")
        
       


if __name__ == "__main__":
    root = tk.Tk()
    ruleta = RuletaCasino(root)
    root.mainloop()
    # Mostrar el número ganador
    