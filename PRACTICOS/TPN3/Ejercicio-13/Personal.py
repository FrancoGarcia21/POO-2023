class Personal:
    
    def __init__(self, nombre, antiguedad, sector):
        self._nombre = nombre
        self._antiguedad = antiguedad
        self._sector = sector
        self._horas_trabajadas = 0
    
    def registrar_horas(self, horas):
        self._horas_trabajadas += horas
    
    def cumplio_horas_minimas(self, horas_minimas):
        return self._horas_trabajadas >= horas_minimas