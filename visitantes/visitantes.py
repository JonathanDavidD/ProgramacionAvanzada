from datetime import datetime
from usuario.utils.roles import Rol
from usuario.usuario import Usuario


class Visitante(Usuario):
    fecha_de_registro: datetime
    #lista_visita: str
    #fecha_de_visitas:datetime
    rol: Rol
    numero_visitas: int


    def __init__(self, id: str, nombre: str, fecha_nacimiento: datetime,apellido: str,curp: str, fecha_de_registro: datetime, ano:str, dia:str, mes:str):
        super().__init__(nombre=nombre, apellido=apellido,id=id, curp=curp, fecha_nacimiento=fecha_nacimiento, rol=Rol)
        #self.lista_visitas=lista_visitas
        self.fecha_nacimiento=fecha_nacimiento
        #self.numero_visitas=numero_visitas
        self.apellido=apellido
        #self.id=id
        self.curp= curp
        self.fecha_de_registro=fecha_de_registro
        self.mes=mes
        self.dia=dia
        self.ano=ano

        #self.rol=rol
    
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Nombre completo: {nombre_completo}\n-ID: {self.id}\n-Curp: {self.curp}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de registro: {self.fecha_de_registro}\n"
        return info
    
    def sumar_numero_visitas(self,numero_visitas):
        numero_visitas += 1
        return numero_visitas

