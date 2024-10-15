from typing import List
from datetime import datetime
from random import randint
from visitantes.visitantes import Visitante
from empleados.empleado import Empleado
from animales.animales import Animal
from visitas.visita import Visita



class Zoologico():
    lista_empleados: List[Empleado] = []
    lista_visitantes: List[Visitante] = []
    lista_visitantes_adulto: List[Visitante] = []
    lista_visitantes_nino: List[Visitante] = []
    lista_animales : List[Animal] = []
    lista_visita: List[Visita]=[]
    
    
    ##def __init__(self):
        #Esto para que es?
        ##self.lista_visitantes: List[Visitante]
        ##self.lista_empleados: List[Empleado]

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        print("\nSe registro correctamente")


    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        print("\nSe registro correctamente")

    def registrar_visitante_adulto(self, Adulto: Visitante):
        self.lista_visitantes.append(Adulto)
        self.lista_visitantes_adulto.append(Adulto)

    def registrar_visitante_nino(self, Nino: Visitante):
        self.lista_visitantes.append(Nino)
        self.lista_visitantes_nino.append(Nino)

    #def registrar_empleado(self, empleado: Empleados):
        #self.lista_empleados.append(empleado)

    def registrar_visita(self, visita:Visita):
        self.lista_visita.append(visita)

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
        
    def eliminar_visitante(self, id: str):
        for visitante in self.lista_visitantes:
            if visitante.id == id:
                self.lista_visitantes.remove(visitante)
                print("\nSe eliminó correctamente")
            return 
        print("\nNo se encontró el empleado con el id: ",id)

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
    
    def generar_id_visitantes(self, apellido:str):
        primer_letra = apellido[:2].upper()
        aleatorio = randint(200, 6000)
        id_visitante= f"M-{primer_letra}{aleatorio}"
        return id_visitante
    
    def generar_id_animal(self):
        pass

    def generar_fecha_de_visita(self, id: str, visita:Visita):
        for visitante in self.lista_visitantes:
            if visitante.id == id:
                self.lista_visita.append(visita)
                visitante.sumar_numero_visitas()


                print("\nSe registró correctamente")
            return 
        print("\nNo se encontró el empleado con el id: ",id)

    def listar_visita(self):
        for visita in self.lista_visita:
            print(visita.mostrar_visita())
