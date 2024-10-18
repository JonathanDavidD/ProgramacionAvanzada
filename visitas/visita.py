from visitantes.visitantes import Visitante
from guias.guia import Guia
from typing import List
from datetime import datetime



class Visita:
    
    fecha_visita:datetime
    guia_a_cargo: Guia
    id_visitante:str
    visitante_v: List[Visitante]=[]
    
    id:str

    
    def __init__(self,fecha_visita:datetime , guia_a_cargo: Guia, id_visitante:str, id:str):
        self.fecha_visita=fecha_visita
        self.guia_a_cargo=guia_a_cargo
        self.id_visitante=id_visitante
        self.id=id

    def mostrar_visita(self):
        info=f"Dia de la visita: {self.dia_v}, Mes de la visita: {self.mes_v}, Año de la visita: {self.ano_v}, Visitante: {self.visitante_v}, Guia a cargo: {self.guia_a_cargo}"
        return info
    
    def ingresar_visitantes(self, visitante):
        self.visitante_v.append(visitante)
        


    
    
    


