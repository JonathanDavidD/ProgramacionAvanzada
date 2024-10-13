from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol
from random import randint

class Empleado(Usuario):
    id: str
    fecha_ingreso: datetime
    rfc: str
    salario: float
    horario: datetime
    
    def __init__(self,nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, id: str, fecha_ingreso: datetime, rfc: str, salario: float, horario: datetime):
        super().__init__(nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, rol= Rol.EMPLEADO)
        self.id = self.generar_id(id)
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.salario = salario
        self.horario = horario

    def mostrar_info(self):
        pass
    
