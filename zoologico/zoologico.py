from typing import List
from datetime import datetime
from random import randint
from visitantes.visitantes import Visitante
from veterinarios.veterinario import Veterinario
from guias.guia import Guia
from animales.animales import Animal
from visitas.visita import Visita




class Zoologico():
    lista_veterinarios: List[Veterinario] = []
    lista_guias: List[Guia] = []
    lista_visitantes: List[Visitante] = []
    lista_visitantes_adulto: List[Visitante] = []
    lista_visitantes_nino: List[Visitante] = []
    lista_animales : List[Animal] = []
    lista_visita: List[Visita]=[]
    
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        print("\nSe registro correctamente\n")

    def registrar_veterinario(self, veterinario: Veterinario):
        self.lista_veterinarios.append(veterinario)
        print("\nSe registro correctamente\n")
    
    def registrar_guia(self, guia: Guia):
        self.lista_guias.append(guia)
        print("\nSe registro correctamente\n")

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
    
    def eliminar_veterinario(self, id_veterinario: str):
        for veterinario in self.lista_veterinarios:
            if veterinario.id == id_veterinario:
                self.lista_veterinarios.remove(veterinario)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el veterinario con el id: ",id_veterinario)
    
    def eliminar_guia(self, id_guia: str):
        for guia in self.lista_guias:
            if guia.id == id_guia:
                self.lista_guias.remove(guia)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el guia con el id: ",id_guia)
        
    def eliminar_visitante(self, id: str):
        for visitante in self.lista_visitantes:
            if visitante.id == id:
                self.lista_visitantes.remove(visitante)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id)

    def eliminar_animal(self):
        pass
    
    def mostrar_veterinarios(self):
        print("** VETERINARIOS **\n")
        for veterinario in self.lista_veterinarios:
            print(veterinario.mostrar_info_veterinario())
    
    def mostrar_guias(self):
        print("** GUIAS **\n")
        for guia in self.lista_guias:
            print(guia.mostrar_info_guia())
            
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
        id_visitante = f"M-{primer_letra}{aleatorio}"
        
        return id_visitante
    
    
    def generar_id_animal(self):
        pass

    def generar_fecha_de_visita(self, id: str, visita:Visita):
        for visitante in self.lista_visitantes:
            if visitante.id == id:
                self.lista_visita.append(visita)
                visitante.sumar_numero_visitas()


                print("\nSe registró correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id)

    def listar_visita(self):
        for visita in self.lista_visita:
            print(visita.mostrar_visita())
