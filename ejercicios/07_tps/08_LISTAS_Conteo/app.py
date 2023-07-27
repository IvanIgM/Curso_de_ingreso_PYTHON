import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ivan Marrero

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):

        self.lista.clear()
        
        numeros_str = prompt("Numeros", "Ingrese un numero (cancel para parar)")

        while numeros_str != None:

            numeros = int(numeros_str)

            self.lista.append(numeros)
            numeros_str = prompt("Numeros", "Ingrese otro numero")
                 
        pass

    def btn_mostrar_estadisticas_on_click(self):

        minimoNegativo = self.lista[0] #Hacer bandera, minimo y maximo no funcionan
        maximoPositivo = self.lista[0]

        contadorPositivo = 0
        contadorNegativo = 0
        contadorCero = 0
        acumuladorPositivo = 0
        acumuladorNegativo = 0

        for numeros in self.lista:

            if numeros > 0:
                acumuladorPositivo += numeros
                contadorPositivo += 1
                
                if numeros > maximoPositivo:
                    maximoPositivo = numeros

            elif numeros == 0:
                contadorCero += 1

            else:
                acumuladorNegativo += numeros
                contadorNegativo += 1

                if numeros < minimoNegativo:
                    minimoNegativo = numeros


        if acumuladorNegativo != 0 and contadorNegativo != 0:
            promedioNegativo = acumuladorNegativo / contadorNegativo
            alert("Promedio negativo", "Promedio negativo: " + str(promedioNegativo))

        alert("Positivos", "Suma acumulada de los positivos: " + str(acumuladorPositivo))
        alert("Negativos", "Suma acumulada de los negativos: " + str(acumuladorNegativo))

        alert("Cantidad positivos", "Cantidad de numeros positivos: " + str(contadorPositivo))
        alert("Cantidad negativos", "Cantidad de numeros negativos: " + str(contadorNegativo))

        alert("Cantidad ceros", "Cantidad de ceros: " + str(contadorCero))

        alert("Minimo negativo", "El minimo de los negativos: " + str(minimoNegativo))
        alert("Maximo positivo", "El maximo de los positivos: " + str(maximoPositivo))

        


        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
