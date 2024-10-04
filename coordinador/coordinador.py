from usuario.usuario import Usuario

class Coordinador(Usuario):
    sueldo:int
    rfc:str
    anos_antiguedad:int

    def __init__(self, numero_control:str, nombre:str, apellido:str, sueldo:int, rfc:str, anos_anitugedad:int, contrasenia:str):
        super().__init__(numero_control=numero_control, nombre=nombre, apeliido=apellido, contrasenia=contrasenia)
        self.sueldo=sueldo
        self.rfc=rfc
        self.anos_antiguedad=anos_anitugedad