from usuario.utils.roles import Rol
from usuario.usuario import Usuario
from datetime import datetime


class Veterinario(Usuario):
    fecha_ingreso: datetime
    rfc: str
    salario: float
    
    def __init__(self,nombre: str, apellido: str,id: str, curp: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, rfc: str, salario: float):
        super().__init__(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento, rol=Rol.VETERINARIO)
        self.fecha_ingreso = fecha_ingreso
        self.rfc = rfc
        self.salario = salario
       
        
    def mostrar_info_veterinario(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"-Nombre completo: {nombre_completo}\n-ID: {self.id}\n-Curp: {self.curp}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de ingreso: {self.fecha_ingreso}\n-RFC: {self.rfc}\n-Salario: {self.salario}\n-Rol: {self.rol.value}\n"
        return info