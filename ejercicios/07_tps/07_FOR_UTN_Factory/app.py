'''
Ivan Marrero

UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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

        cantidadPuntoA = 0

        acumuladorNBinario = 0
        contadorNBinario = 0
        acumuladorFemenino = 0
        contadorFemenino = 0
        acumuladorMasculino = 0
        contadorMasculino = 0

        contadorPython = 0
        contadorJS = 0
        contadorASP = 0

        menorNombreJr = ""

        postulantes = 0

        flag = True


        for i in range(0, 3, 1):

            nombre = prompt("Nombre", "Ingrese su nombre: ")
            edad_str = prompt("Edad", "Ingrese su edad: ")
            genero = prompt("Genero", "Ingrese su genero (F-M-NB): ")
            tecnologia = prompt("Tecnologia", "Tecnología (PYTHON - JS - ASP.NET): ")

            if tecnologia == "PYTHON":
                contadorPython += 1
            elif tecnologia == "JS":
                contadorJS += 1
            elif tecnologia == "ASP.NET":
                contadorASP += 1

            puesto = prompt("Puesto", "Puesto (Jr - Ssr - Sr): ")

            edad = int(edad_str)

            if contadorASP > contadorJS and contadorASP > contadorPython:
                mayorTecnologia = tecnologia

            elif contadorPython > contadorJS and contadorPython > contadorASP:
                mayorTecnologia = tecnologia

            elif contadorJS > contadorASP and contadorJS > contadorPython:
                mayorTecnologia = tecnologia
            
            

            if genero == "F":

                acumuladorFemenino += edad
                contadorFemenino += 1
            
            elif genero == "M":

                acumuladorMasculino += edad
                contadorMasculino += 1
            
            else:
                acumuladorNBinario += edad
                contadorNBinario += 1

            if puesto == "Jr" and flag:

                menorEdadJR = edad
                menorNombreJr = nombre
                flag = False

            elif puesto == "Jr" and edad < menorEdadJR:

                menorEdadJR = edad
                menorNombreJr = nombre

            if genero == "NB" and tecnologia == "ASP.NET" or tecnologia == "JS" and edad > 25 and edad < 40 and puesto == "Ssr":
                cantidadPuntoA += 1

            postulantes += 1
            

        
        promedioFemenino = acumuladorFemenino / contadorFemenino
        promedioMasculino = acumuladorMasculino / contadorMasculino
        promedioNBinario = acumuladorNBinario / contadorNBinario

        porcentajeFemenino = contadorFemenino * 100 / postulantes
        porcentajeMasculino = contadorMasculino * 100 / postulantes
        porcentajeNBinario = contadorNBinario * 100 / postulantes

        print("Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: " + str(cantidadPuntoA))

        print("Promedio de edades femenino: " + str(promedioFemenino))
        print("Porcentaje femenino: %" + str(porcentajeFemenino))
        print("Promedio de edades masculino: " + str(promedioMasculino))
        print("Porcentaje masculino: %" + str(porcentajeMasculino))
        print("Promedio de edades no binario: " + str(promedioNBinario))
        print("Porcentaje no binario: %" + str(porcentajeNBinario))

        print("Nombre del postulante Jr con menor edad: " + menorNombreJr)

        print("Tecnologia con mas postulantes: " + mayorTecnologia)






        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
