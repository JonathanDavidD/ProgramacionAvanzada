from typing import List
from datetime import datetime
from random import randint
from visitantes.visitantes import Visitante
from empleados.empleado import Empleado
from animales.animales import Animal


class Zoologico():
    lista_empleados: List[Empleado] = []
    lista_visitantes: List[Visitante] = []
    lista_animales : List[Animal] = []
    
    
    def __init__(self):
        #Esto para que es?
        self.lista_visitantes: List[Visitante]
        self.lista_empleados: List[Empleado]

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        print("\nSe registro correctamente")


    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        print("\nSe registro correctamente")

    def registrar_visita(self):
        pass
    def registrar_animal(self):
        pass
    def registrar_mantenimiento(self):
        pass
    def modificar_datos_empleado(self):
        pass
    def modificar_datos_visitante(self):
        pass
    def modificar_datos_animal(self):
        pass
    def eliminar_empleado(self, id: str):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                print("\nSe eliminó correctamente")
            return 
        print("\nNo se encontró el empleado con el id: ",id)
        
    def eliminar_visitante(self):
        pass
    def eliminar_animal(self):
        pass
    def mostrar_empleados(self):
        print("** EMPLEADOS **\n")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_info_empleado())
            
    def mostrar_visitantes(self):
        print("** VISITANTES **\n")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        
    def mostrar_animal(self):
        pass
    def mostrar_visitas(self):
        pass
    def mostrar_mantenimiento(self):
        pass
        
    def generar_id_empleado(self,apellido: str,rfc: str ):
        primeros_digitos = apellido[0:2].upper()
        ultimos_digitos = rfc[0:-2].upper()
        id = f"{primeros_digitos}-{ultimos_digitos}-{randint(1,10000)}"
        return id
    
    def generar_id_visitante(self):
        pass
    
    def generar_id_animal(self):
        pass