from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol


class Estudiante(Usuario): 
    curp: str
    ano: int
    mes: int
    dia: int
    fecha_nacimiento: datetime
    nombre_completo:str


    def __init__(self,numero_control:str, nombre:str, apellido:str, curp:str,ano:int,  mes: int, dia: int, fecha_nacimiento:datetime, contrasenia:str):
        super().__init__(numero_control=numero_control, nombre=nombre, apeliido=apellido, contrasenia=contrasenia, rol=Rol.ESTUDIANTE)
        self.curp = curp
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.fecha_nacimiento = fecha_nacimiento


    def mostrar_info_estudiante(self):
        self.nombre_completo=f"{self.nombre}{self.apellido}"
        info= f"Numero de control: {self.numero_control}, nombre completo: {self.nombre_completo}, curp: {self.curp}, fecha de nacimiento: {self.fecha_nacimiento}"
        print(info)
