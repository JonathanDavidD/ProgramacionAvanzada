from typing import List
from materias.materia import Materia
from grupos.grupos import Grupo
from random import randint


class Semestre:
    id: str
    numero: int 
    id_carrera: str
    materias: List[Materia]
    grupos: List [Grupo]


    def __init__(self, numero: int, id_carrera: str):
        self.id= self.generar_id(numero)
        self.id_carrera=id_carrera


    def generar_id(self, numero_semestre:int)-> str:
        return f"{numero_semestre} - {randint(1,1000)} - {randint(1,10000)}"
