import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
        2 - Camioneta - 2000 km
        etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []

    def btn_agregar_on_click(self):
        
        continuar = True

        while continuar:
            tipo_vehiculo = prompt("Tipo de vehículo", "Ingrese el tipo del vehiculo")
            while tipo_vehiculo == None or not (tipo_vehiculo.lower() == "auto" or tipo_vehiculo.lower() == "camioneta" or tipo_vehiculo.lower() == "moto"):
                tipo_vehiculo = prompt("Error", "El tipo de vehiculo debe ser auto, camioneta o moto")
            
            km_vehiculo = prompt("Kilometros del vehículo", "Ingrese los kilometros del vehiculo")
            while km_vehiculo == None or float(km_vehiculo) <= 0:
                km_vehiculo = prompt("Error", "El kilometraje del vehiculo debe ser mayor a 0")

            km_vehiculo = float(km_vehiculo)

            self.lista_tipo_vehiculo.append(tipo_vehiculo.lower())
            self.lista_marca_vehiculo.append(km_vehiculo)

            continuar = question("Continuar", "¿Desea continuar?")

    
    def btn_mostrar_on_click(self):
        
        cantidad_vehiculos = len(self.lista_tipo_vehiculo)
        mensaje = ""

        for i in range(0, cantidad_vehiculos):
            mensaje += str(i) + " - " + self.lista_tipo_vehiculo[i] + " - " + str(self.lista_marca_vehiculo[i]) + "\n"

        alert("Mensaje", mensaje)


    def btn_informar_on_click(self):

        indice_mayor_kilometraje = 0
        indice_menor_kilometraje = 0
        km_mayor_kilometraje = 0
        km_menor_kilometraje = 0
        kilometraje_total = 0
        kilometraje_promedio = 0
        precio_total_servicios = 0
        precio_promedio_servicios = 0
        vehiculos_gran_kilometraje = []
        precio_total_servicios_gran_kilometraje = 0
        precio_promedio_servicios_gran_kilometraje = "Ningún vehículo supera los 10.000 km"
        kilometrajes_mayores_al_promedio = []
        kilometrajes_menores_al_promedio = []
        cantidad_autos = 0
        cantidad_motos = 0
        cantidad_camionetas = 0

        lista_km_autos = []
        promedio_km_autos = 0

        lista_km_camionetas = []
        promedio_km_camionetas = 0

        lista_km_motos = []
        promedio_km_motos = 0

        mayor_promedio_km = 0
        cantidad_vehiculos = len(self.lista_tipo_vehiculo)
        flag_mayor_kilometraje = True
        flag_menor_kilometraje = True

        informe = ""

        # consignas 0-3
        for i in range(0, cantidad_vehiculos):

            km_vehiculo = self.lista_marca_vehiculo[i]
            tipo_vehiculo = self.lista_tipo_vehiculo[i]
            #  0-1) mayor y menor kilometraje
            if flag_mayor_kilometraje or km_vehiculo > km_mayor_kilometraje:
                flag_mayor_kilometraje = False
                km_mayor_kilometraje = km_vehiculo
                indice_mayor_kilometraje = i
            if flag_menor_kilometraje or km_vehiculo < km_menor_kilometraje:
                flag_menor_kilometraje = False
                km_menor_kilometraje = km_vehiculo
                indice_menor_kilometraje = i

            # 2) kilometraje promedio
            kilometraje_total += km_vehiculo

            # 3) precio promedio ; 6) cantidad de vehiculos de cada tipo ; y 8) mayor de los promedios por tipo de vehiculo
            match tipo_vehiculo:
                case "auto":
                    precio_total_servicios += 15000
                    cantidad_autos += 1
                    lista_km_autos.append(km_vehiculo)
                    if km_vehiculo > 10000:
                        vehiculos_gran_kilometraje.append(15000)
                case "camioneta":
                    precio_total_servicios += 25000
                    cantidad_camionetas += 1
                    lista_km_camionetas.append(km_vehiculo)
                    if km_vehiculo > 10000:
                        vehiculos_gran_kilometraje.append(25000)
                case "moto":
                    precio_total_servicios += 10000
                    cantidad_motos += 1
                    lista_km_motos.append(km_vehiculo)
                    if km_vehiculo > 10000:
                        vehiculos_gran_kilometraje.append(10000)

            """ # 7) precio promedio de los servicios que superan los 10000km
            if km_vehiculo > 10000:
                vehiculos_gran_kilometraje.append(km_vehiculo) """

        # 2) y 3)
        if cantidad_vehiculos > 0:
            precio_promedio_servicios = precio_total_servicios / cantidad_vehiculos
            kilometraje_promedio = kilometraje_total / cantidad_vehiculos

        # consignas 4-5
        for kilometros_vehiculo in self.lista_marca_vehiculo:
            if kilometros_vehiculo > kilometraje_promedio:
                kilometrajes_mayores_al_promedio.append(kilometros_vehiculo)
            else:
                kilometrajes_menores_al_promedio.append(kilometros_vehiculo)
        
        # consigna 7
        for km in vehiculos_gran_kilometraje:
            precio_total_servicios_gran_kilometraje += km

        if len(vehiculos_gran_kilometraje) > 0:
            precio_promedio_servicios_gran_kilometraje = precio_total_servicios_gran_kilometraje / len(vehiculos_gran_kilometraje)

        # consigna 8
        for km in lista_km_autos:
            promedio_km_autos += km
        if cantidad_autos > 0:
            promedio_km_autos = promedio_km_autos / cantidad_autos
        """ else:
            promedio_km_autos = "No hay ningún auto" """

        for km in lista_km_camionetas:
            promedio_km_camionetas += km
        if cantidad_camionetas > 0:
            promedio_km_camionetas = promedio_km_camionetas / cantidad_camionetas
        """ else:
            promedio_km_camionetas = "No hay ninguna camionera" """

        for km in lista_km_motos:
            promedio_km_motos += km
        if cantidad_motos > 0:
            promedio_km_motos = promedio_km_motos / cantidad_motos
        """ else:
            promedio_km_motos = "No hay ninguna moto" """
        
        if promedio_km_autos >= promedio_km_motos and promedio_km_autos >= promedio_km_camionetas:
            mayor_promedio_km = str(promedio_km_autos) + " - autos"
        elif promedio_km_camionetas >= promedio_km_autos and promedio_km_camionetas >= promedio_km_motos:
            mayor_promedio_km = str(promedio_km_camionetas) + " - camionetas"
        elif promedio_km_motos > promedio_km_autos and promedio_km_motos > promedio_km_camionetas:
            mayor_promedio_km = str(promedio_km_motos) + " - motos"

        


        if cantidad_vehiculos > 0:
            informe += "Mayor kilometraje: " + str(km_mayor_kilometraje) + "; tipo de vehiculo: " + self.lista_tipo_vehiculo[indice_mayor_kilometraje] + "\n"
            informe += "Menor kilometraje: " + str(km_menor_kilometraje) + "; tipo de vehiculo: " + self.lista_tipo_vehiculo[indice_menor_kilometraje] + "\n"
            informe += "Kilometraje promedio de los vehiculos: " + str(kilometraje_promedio) + "\n"
            informe += "Precio promedio de todos los servicios: " + str(precio_promedio_servicios) + "\n"
            informe += "Kilometrajes que superan al promedio: " + str(kilometrajes_mayores_al_promedio) + "\n"
            informe += "Kilometrajes que NO superan al promedio: " + str(kilometrajes_menores_al_promedio) + "\n"
            informe += "Cantidad de autos: " + str(cantidad_autos) + "\n"
            informe += "Cantidad de camionetas: " + str(cantidad_camionetas) + "\n"
            informe += "Cantidad de motos: " + str(cantidad_motos) + "\n"
            informe += "Precio promedio de los servicios cuyo kilometraje es mayor a 10000 km: " + str(precio_promedio_servicios_gran_kilometraje) + "\n"
            informe += "Mayor de los promedios por tipo de vehículo: " + mayor_promedio_km
        else:
            informe = "No se ingresó ingún vehículo"

        alert("Informe", informe)

if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

