'''
Ivan Marrero

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        bandera = True
        votosTotales = 0

        contador = 0

        pregunta = prompt("Inicio", "¿Desea empezar? (s/n): ")

        while pregunta != "n":
            
            nombre = prompt("Nombre", "Ingrese el nombre")
            edad_str = prompt("Edad", "Ingrese la edad")
            votos_str = prompt("Votos", "Ingrese la cantidad de votos")

            votos = int(votos_str)
            edad = int(edad_str)

            votosTotales += votos
            contador += 1

            if edad < 25:
                alert("Error", "Edad menor a 25")
                break

            if votos < 0:
                alert("Error", "Voto menor a 0")
                break

            if bandera:

                masVotos = votos
                nombreMasVotos = nombre
                nombreMenorVotos = nombre
                edadMenorVotos = edad
                bandera = False

            
            if votos > masVotos:

                masVotos = votos
                nombreMasVotos = nombre

            else:

                nombreMenorVotos = nombre
                edadMenorVotos = edad

            pregunta = prompt("Pregunta", "¿Desea continuar? s/n")

        promedio = edad / contador

        print("Candidato con mas votos: " + nombreMasVotos)
        print(nombreMenorVotos + " de " + str(edadMenorVotos) + " años tuvo menos votos")
        print("Promedio entre todas las edades: " + str(promedio))
        print("Total de votos emitidos: " + str(votosTotales))
            

pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
