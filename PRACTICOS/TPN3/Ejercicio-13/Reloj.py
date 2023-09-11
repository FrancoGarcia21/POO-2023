from Docente import Docente
from NoDocente import NoDocente

class Reloj:
    def __init__(self, personas):
        self.__personas = personas
    
    def generar_informe(self):
        informe = {}
        for persona in self.__personas:
            horas_trabajadas = persona.generar_horas_trabajadas()
            persona.registrar_horas(horas_trabajadas)
            informe[persona._nombre] = {
                "Antigüedad": persona._antiguedad,
                "Sector": persona._sector,
                "Horas Trabajadas": horas_trabajadas,
                "Cumplió Mínimo": persona.cumplio_horas_minimas(self.calcular_minimo_esperado(persona))
            }
        return informe

    def calcular_minimo_esperado(self, persona):
        if isinstance(persona, Docente):
            if persona._categoria == "Simple":
                return 40
            elif persona._categoria == "Semiexclusiva":
                return 80
            elif persona._categoria == "Exclusiva":
                return 160
        elif isinstance(persona, NoDocente):
            if persona._jornada == "Completa":
                return 120
            elif persona._jornada == "Reducida":
                return 80