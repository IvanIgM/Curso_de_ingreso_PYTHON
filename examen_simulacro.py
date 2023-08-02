import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ivan Marrero

Enunciado:


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):

        peso_str = self.txt_peso_articulo.get()

        peso = float(peso_str)

        if peso <= 0:
            alert("Error", "Solo se aceptan valores mayores a cero")

        else:
            self.lista_pesos.append(peso)
            alert("Agregado", "Peso agregado a la lista")
                    
                    
        
        self.txt_peso_articulo.delete(0,100)

        pass        

    
    def btn_mostrar_on_click(self):

        contador = 0

        for i in self.lista_pesos:
            onzas = i * 28.3495

            print("Posicion N°" + str(contador) + ": Gramos: " + str(i) + " | Onzas: " + str(onzas))

            contador += 1

            


        pass


    def btn_informar_on_click(self):

        bandera = True

        contadorC = 0

        for j in self.lista_pesos:

            if bandera:

                pesoMenor = j
                pesoMayor = j

                posicionMayor = contadorC
                posicionMenor = contadorC

                bandera = False
            
            if j >= pesoMayor:

                pesoMayor = j
                posicionMayor = contadorC

            else:
                pesoMenor = j
                posicionMenor = contadorC
            

            contadorC += 1

            
        

        gramos = pesoMenor * 0.035274
        onzas = pesoMayor * 28.3495

        print("Peso menor en gramos: " + str(gramos) + ". Esta en la posicion N°" + str(posicionMenor))
        print("Peso mayor en onzas: " + str(onzas) + ". Esta en la posicion N°" + str(posicionMayor))

        
    #0- Valor (en onzas) y posicion del articulo mas pesado
    #1- Valor (en gramos) y posicion del articulo mas liviano
    # 
    # DNI 43 664 281     

        pass


if __name__ == "__main__":
    app = App()

    app.mainloop()
       