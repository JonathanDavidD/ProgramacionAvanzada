from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol
from random import randint

class Empleado(Usuario):
    fecha_ingreso: datetime
    rfc: str
    salario: float
    horario: datetime
    
    def __init__(self,nombre: str, apellido: str,id: str, curp: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, rfc: str, salario: float, horario: datetime):
        super().__init__(nombre=nombre, apellido=apellido,id=id, curp=curp, fecha_nacimiento=fecha_nacimiento)
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.salario = salario
        self.horario = horario

    def mostrar_info_empleado(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"-Nombre completo: {nombre_completo}\n-Curp: {self.curp}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de ingreso: {self.fecha_ingreso}\n-RFC: {self.rfc}\n-Salario: {self.salario}\n-Horario laboral: {self.horario}"
        return info