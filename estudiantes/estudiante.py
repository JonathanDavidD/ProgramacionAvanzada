from datetime import datetime


class Estudiante: 
    numero_control: str
    nombre: str
    apellido: str
    curp: str
    ano: int
    mes: int
    dia: int
    fecha_nacimiento: datetime
    nombre_completo:str


    def __init__(self,numero_control:str, nombre:str, apellido:str, curp:str,ano:int,  mes: int, dia: int, fecha_nacimiento:datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.fecha_nacimiento = fecha_nacimiento


    def mostrar_info_estudiante(self):
        self.nombre_completo=f"{self.nombre}{self.apellido}"
        info= f"Numero de control: {self.numero_control}, nombre completo: {self.nombre_completo}, curp: {self.curp}, fecha de nacimiento: {self.fecha_nacimiento}"
        print(info)
