from Personal import Personal
import random

class Docente(Personal):
    def __init__(self, nombre, antiguedad, sector, categoria):
        super().__init__(nombre, antiguedad, sector)
        self._categoria = categoria

    def generar_horas_trabajadas(self):
        if self._categoria == "Simple":
            return random.randint(35, 45)
        elif self._categoria == "Semiexclusiva":
            return random.randint(70, 90)
        elif self._categoria == "Exclusiva":
            return random.randint(140, 180)