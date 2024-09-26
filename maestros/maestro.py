class Maestro:

    numero_control: int 
    nombre: str
    apellido: str
    rfc: str
    sueldo: int 
    ano_nacimiento: int 
    nombre_completo:str
    

    def __init__ (self,numero_control:str, nombre: str,apellido: str, rfc: str, sueldo:int, ano_nacimineto:int):
        self.numero_control=numero_control
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo
        self.ano_nacimiento=ano_nacimineto

    def mostrar_info_maestro(self):
        self.nombre_completo=f"{self.nombre}{self.apellido}"
        info=f"Numero de control:{self.numero_control}, Nombre: {self.nombre_completo}, RFC: {self.rfc}, Sueldo:{self.sueldo}" 
        return info
