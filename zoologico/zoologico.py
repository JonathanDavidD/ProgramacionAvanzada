from typing import List
from datetime import datetime
from visitantes.visitantes import Visitante
from empleados.empleado import Empleado
from animales.animales import Animal


class Zoologico():
    
    def __init__(self):
        self.lista_visitantes: List[Visitante]=[]
        self.lista_empleados: List[Empleado]=[]
        self.lista_animales: List[Animal]=[]

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)

    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)

    def registrar_visita(self):
        pass
    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)


    def registrar_mantenimiento(self):
        pass
    def modificar_datos_empleado(self):
        pass
    def modificar_datos_visitante(self):
        pass
    def modificar_datos_animal(self):
        pass
    def eliminar_empleado(self):
        pass
    def eliminar_visitante(self):
        pass
    def eliminar_animal(self):
        pass
    def mostrar_empleados(self):
        pass
    def mostrar_visitantes(self):
        pass
    def mostrar_animal(self):
        for animal in self.lista_animales:
            print(animal.mostrar_info_animales())
        return


    def mostrar_visitas(self):
        pass
    def mostrar_mantenimiento(self):
        pass


    def listar_visitantes(self):
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        return

        