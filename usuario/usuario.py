from datetime import datetime
from .utils.roles import Rol

class Usuario:
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime
    rol: Rol
    
    def __init__(self,nombre: str,apellido: str,curp: str,fecha_nacimiento: datetime,rol: Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        self.rol = rol
