from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupos import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from carrera.carrera import Carrera
from semestre.semestre import Semestre

class Escuela:
    Lista_estudiantes: List[Estudiante]=[]
    Lista_maestros: List[Maestro]=[]
    Lista_grupos: List[Grupo]=[]
    Lista_materias: List [Materia]=[]
    Lista_carreras: List[Carrera]=[]
    Lista_semestre: List[Semestre]=[]


    def registar_estudiante(self, estudiante: Estudiante):
        self.Lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        #L #2024 #
       numero_control=f"L{datetime.now().year}{datetime.now().month}{len(self.Lista_estudiantes)+1}{randint(1, 10000)}"
       return numero_control
    
    def registrar_maestros(self, maestro: Maestro):
        self.Lista_maestros.append(maestro)


    def registrar_materia(self, materia:Materia):
        self.Lista_materias.append(materia)

    def registrar_carrera(self, carrera: Carrera):
        self.Lista_carreras.append(carrera)

    def registrar_grupo(self, grupo: Grupo):
       
        id_semestre= grupo.id_semestre
        for semestre in self.Lista_semestre:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        
        self.Lista_grupos.append(grupo)


    def registrar_semestre(self, semestre: Semestre):
        id_carrera=semestre.id
        for carrera in self.Lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        
        self.Lista_semestre.append(semestre)

    def listar_estudiantes(self, estudiante:Estudiante):
        for estudiante in self.Lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def listar_maestros(self, maestro:Maestro):
        for maestro in self.Lista_maestros:
            maestro.mostrar_info_maestro(maestro)

    def listar_materias(self, materia:Materia):
        for materia in self.Lista_materias:
            print(materia.mostrar_info_materia())

    def listar_carreras(self, carrera:Carrera):
        for carrera in self.Lista_carreras:
            print(carrera.mostrar_info_carrera())

    def listar_semestres(self, semestre: Semestre):
        for semestre in self.Lista_semestre:
            print(semestre.mostrar_info_semestre())

    def listar_grupos(self, grupo:Grupo):
        for grupo in self.Lista_grupos:
            print(grupo.mostrar_info_grupo())
           
     
    def generar_numero_control_maestros(self, rfc:str, nombre:str, ano_nacimiento:int):
        numero_control_maestros=f"M{ano_nacimiento}{datetime.now().day}{randint(500, 5000)}{nombre[:2]}{rfc[-2:]}{len(self.Lista_maestros)+1}"
        return numero_control_maestros
    
    def generar_numero_control_materia(self, nombre:str, semestre: int, creditos: int):
        numero_control_materia=f"M{nombre[-2:]}{semestre}{creditos}{randint(1,1000)}"
        return numero_control_materia
    
    def eliminar_estudiante (self, numero_control:str):
        for estudiante in self.Lista_estudiantes:
            if estudiante.numero_control== numero_control:
                self.Lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return 
        print("No se encontró el estudiante con numero de control: ", numero_control)

    def eliminar_maestro (self, numero_control:str):
        for maestro in self.Lista_maestros:
            if maestro.numero_control==numero_control:
                self.Lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        print("No se encontro el maestro con el numero de control: ", numero_control)

    def eliminar_materia(self, numero_control:str):
        for materia in self.Lista_materias:
            if materia.numero_control==numero_control:
                self.Lista_materias.remove(materia)
                print("Materia eliminada")
                return 
        print("No se encontro la materia con el numero de control: ", numero_control)
