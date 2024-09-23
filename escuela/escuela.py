from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupos import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint


class Escuela:
    Lista_estudiantes: List[Estudiante]=[]
    Lista_maestros: List[Maestro]=[]
    Lista_grupos: List[Grupo]=[]
    Lista_materias: List [Materia]=[]


    def registar_estudiante(self, estudiante: Estudiante):
        self.Lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        #L #2024 #
       numero_control=f"L{datetime.now().year}{datetime.now().month}{len(self.Lista_estudiantes)+1}{randint(1, 10000)}"
       return numero_control
    
    def registrar_maestros(self, maestro: Maestro):
        self.Lista_maestros.append(maestro)
           
    
    def generar_numero_control_maestros(self, rfc:str, nombre:str, ano_nacimiento:int):
        numero_control_maestros=f"M{ano_nacimiento}{datetime.now().day}{randint(500, 5000)}{nombre[:2]}{rfc[-2:]}{len(self.Lista_maestros)+1}"
        return numero_control_maestros
    
    def generar_numero_control_materia(self, nombre:str, semestre: int, creditos: int):
        numero_control_materia=f"M{nombre[-2:]}{semestre}{creditos}{randint(1,1000)}"
        return numero_control_materia