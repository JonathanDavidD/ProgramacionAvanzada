

class Visita:
    dia_v: str
    mes_v: str
    ano_v: str
    
    def __init__(self, dia_v:str, mes_v:str, ano_v:str):
        self.dia_v=dia_v
        self.ano_v=ano_v
        self.mes_v=mes_v

    def mostrar_visita(self):
        info=f"Dia de la visita: {self.dia_v}, Mes de la visita: {self.mes_v}, Año de la visita: {self.ano_v}"
        return info
    


