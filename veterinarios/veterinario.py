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
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"-Nombre completo: {nombre_completo}\n-ID: {self.id}\n-Curp: {self.curp}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de ingreso: {self.fecha_ingreso}\n-RFC: {self.rfc}\n-Salario: {self.salario}\n-Rol: {self.rol.value}\n"
        return info
    
    def modificar_info(self,id_veterinario: str):
        
        nombre = str(input("Ingrese el nombre del empleado: "))
        apellido = str(input("Ingrese el apellido del empleado: "))
        curp = str(input("Ingrese la curp del empleado: "))
        dia = int(input("Ingrese el dia de nacimiento: "))
        mes = int(input("Ingrese el mes de nacimeinto: "))
        anio = int(input("Ingrese el año de nacimiento: "))
        dia_ingreso = int(input("Ingrese el dia de ingreso al empleo: "))
        mes_ingreso = int(input("Ingrese el mes de ingreso al empleo: "))
        anio_ingreso = int(input("Ingrese el año de ingreso al empleo: "))
        fecha_nacimiento = datetime(anio, mes, dia)
        fecha_ingreso = datetime(anio_ingreso,mes_ingreso,dia_ingreso)
        rfc = str(input("Ingrese el rfc del empleado: "))
        salario = float(input("Ingrese el salario del empleado: "))
        
        veterinario_nuevo = Veterinario(nombre=nombre,apellido=apellido,id=id_veterinario,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario)
        return veterinario_nuevo
        
       
    
