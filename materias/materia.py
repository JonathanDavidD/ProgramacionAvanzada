from random import randint

class Materia:
    #id:"MT(Ultimos digitios del nombre)(semestre)(cantidad creditos)(random 1, 1000)""
    nombre: str
    descripcion: str
    semestre: int
    creditos: int 

    def __init__(self, nombre: str, descripcion: str, semestre: int, creditos:int):
        self.nombre=nombre
        self.descripcion=descripcion
        self.semestre=semestre
        self.creditos=creditos

        
    