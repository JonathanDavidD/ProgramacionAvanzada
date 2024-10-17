from datetime import datetime
from usuario.utils.roles import Rol
from usuario.usuario import Usuario


class Visitante(Usuario):
    fecha_de_registro: datetime
    #lista_visita: str
    #fecha_de_visitas:datetime
    numero_visitas: int


    def __init__(self, id: str, nombre: str, fecha_nacimiento: datetime,apellido: str,curp: str, fecha_de_registro: datetime, ano: int):
        
        if 2024 - ano > 18:
            #ADULTO
            super().__init__(nombre=nombre, apellido=apellido, id=id, curp=curp, fecha_nacimiento=fecha_nacimiento,rol=Rol.ADULTO)
            self.fecha_de_registro = fecha_de_registro

        else:
            #NIÑO 
            super().__init__(nombre=nombre, apellido=apellido, id=id, curp=curp, fecha_nacimiento=fecha_nacimiento,rol=Rol.NINO)
            self.fecha_de_registro = fecha_de_registro



        #self.lista_visitas=lista_visitas
        
         #self.numero_visitas=numero_visitas
    
    
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"- Nombre completo: {nombre_completo}\n- ID: {self.id}\n-Curp: {self.curp}\n- Fecha de nacimiento: {self.fecha_nacimiento}\n- Fecha de registro: {self.fecha_de_registro}\n- Persona: {self.rol.value}\n"
        return info
    
    def sumar_numero_visitas(self,numero_visitas):
        numero_visitas += 1
        return numero_visitas
