from datetime import datetime

class Animal:
    tipo:str
    fecha_llegada:datetime
    enfermedades: str
    tipo_alimentacion: str
    fecha_nacimiento:datetime
    peso: float
    frecuencia_alimentacion: str
    vacunas: bool

    def __init__(self, tipo:str, fecha_llegada:datetime, enfermedades:str, tipo_alimentacion: str, fecha_nacimiento:datetime, peso:int, frecuencia_alimentacion: str, vacunas:bool):
        self.tipo=tipo
        self.fecha_llegada=fecha_llegada
        self.enfermedades=enfermedades
        self.tipo_alimentacion=tipo_alimentacion
        self.fecha_nacimiento=fecha_nacimiento
        self.peso=peso
        self.frecuencia_alimentacion=frecuencia_alimentacion
        self.vacunas=vacunas
        
