import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ivan Marrero

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos 
    La suma acumulada de los positivos 
    Cantidad de números positivos ingresados 
    Cantidad de números negativos ingresados 
    Cantidad de ceros 
    Diferencia entre la cantidad de los números positivos ingresados y los negativos 

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        acumuladorNegativo = 0
        acumuladorPositivo = 0
        contadorPositivo = 0
        contadorNegativo = 0
        cantidadCeros = 0

        ingreso_str = prompt("Ingreso", "Ingrese un numero:")

        while ingreso_str != None:
            
            ingreso = int(ingreso_str)


            if ingreso < 0:

                acumuladorNegativo += ingreso
                contadorNegativo += 1
            
            elif ingreso > 0:

                acumuladorPositivo += ingreso
                contadorPositivo += 1

            else:
                cantidadCeros += 1

            ingreso_str = prompt("Ingreso", "Ingrese otro numero:")
        

        diferencia = contadorPositivo - contadorNegativo

        if diferencia < 0:
            diferencia = diferencia * -1


        alert("Alerta","La suma acumulada de los negativos: " + str(acumuladorNegativo))
        alert("Alerta","La suma acumulada de los positivos: " + str(acumuladorPositivo))
        alert("Alerta","Cantidad de números negativos ingresados: " + str(contadorNegativo))
        alert("Alerta","Cantidad de números positivos ingresados: " + str(contadorPositivo))
        alert("Alerta","Cantidad de ceros: " + str(cantidadCeros))
        alert("Alerta","Diferencia entre la cantidad de los números positivos ingresados y los negativos: " + str(diferencia))
                
        

        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
