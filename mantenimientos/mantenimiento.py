from datetime import datetime

class Mantenimiento:
    #empleado_encargado: Empleado
    proceso_realizado: str
    observaciones: str
    id_animal: str
    fecha_proceso: datetime
    
    def __init__(self,proceso_realizado: str,observaciones: str,id_animal: str,fecha_proceso: datetime):
        self.proceso_realizado = proceso_realizado
        self.observaciones = observaciones
        self.id_animal = id_animal
        self.fecha_proceso = fecha_proceso
    
    def mostrar_info_mantenimiento(self):
        info = f"- Proceso: {self.proceso_realizado}\n- Observaciones: {self.observaciones}\n- ID del animal: {self.id_animal}\n- Fecha del proceso: {self.fecha_proceso}\n"
        return info