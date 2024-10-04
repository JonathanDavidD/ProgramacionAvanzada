from .utils.roles import Rol

class Usuario:
    numero_control:str
    nombre:str
    apellido:str
    contrasenia:str
    rol:Rol

    def __init__(self, numero_control:str, nombre:str, apeliido:str, contrasenia:str):
        self.numero_control=numero_control
        self.nombre=nombre
        self.apellido=apeliido
        self.contrasenia=contrasenia