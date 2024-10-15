from typing import List
from datetime import datetime
from random import randint
from visitantes.visitantes import Visitante
#from empleado.empleado import Empleado


class Zoologico():

    def __init__(self):
        #self.lista_empleados: List[Empleado]=[]
        self.lista_visitantes: List[Visitante]=[]



    def registrar_visitante_adulto(self, Adulto: Visitante):
        self.lista_visitantes.append(Adulto)

    def registrar_visitante_nino(self, Nino: Visitante):
        self.lista_visitantes.append(Nino)

    #def registrar_empleado(self, empleado: Empleados):
        #self.lista_empleados.append(empleado)

    #def registrar_visita(self):
        #self.lista_visitas.append(visita)
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
        pass
    def mostrar_visitas(self):
        pass
    def mostrar_mantenimiento(self):
        pass


    def listar_visitantes(self):
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        return
    
    def generar_id_visitantes(self, apellido1:str, apellido2:str):
        primer_letra = apellido1[:2].upper()
        segunda_letra = apellido2[:2].upper()
        aleatorio = randint(200, 6000)
        id_visitante = f"M-{primer_letra}{segunda_letra}{aleatorio}"
        return id_visitante
    
    def generar_visita(self, id_visitante:str)
        

        