from datetime import datetime
from visitantes.utils.roles import Rol


class Visitante():
    nombre: str
    fecha_nacimiento: datetime
    numero_visitas: int
    apellido1: str
    apellido2: str
    ano:str
    dia:str
    mes:str
    curp: str
    fecha_de_registro: datetime
    id_visitante:str
    fecha_de_visitas: datetime
    cant_adultos: int
    rol: Rol


    def __init__(self, fecha_de_visitas:str, cant_adultos:int, nombre: str, fecha_nacimiento: datetime, numero_visitas: int,apellido1: str, apellido2: str,curp: str, fecha_de_registro: datetime, ano:str, dia:str, mes:str, id_visitante:str, rol:Rol):
        self.fecha_de_visitas=fecha_de_visitas
        self.cant_adultos=cant_adultos
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.numero_visitas=numero_visitas
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.curp= curp
        self.fecha_de_registro=fecha_de_registro
        self.mes=mes
        self.dia=dia
        self.ano=ano
        self.id_visitante=id_visitante
        self.rol=rol 

    
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre}{self.apellido1}{self.apellido2}"
        info = f"Nombre completo: {nombre_completo}, Curp: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}, Fecha de registro: {self.fecha_de_registro} Numero de visitas: {self.numero_visitas}"
        return info
    


