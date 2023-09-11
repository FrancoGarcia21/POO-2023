from Personal import Personal
import random


class NoDocente(Personal):
    def __init__(self, nombre, antiguedad, sector, jornada):
        super().__init__(nombre, antiguedad, sector)
        self._jornada = jornada

    def generar_horas_trabajadas(self):
        if self._jornada == "Completa":
            return random.randint(120, 150)
        
        elif self._jornada == "Reducida":
            return random.randint(80, 100)