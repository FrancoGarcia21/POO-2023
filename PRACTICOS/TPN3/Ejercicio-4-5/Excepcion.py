class VidaCeroError(Exception):
    def __init__(self, personaje):
        self._personaje = personaje
        personaje.set_vida(0)  # Establece la vida del personaje en 0
        super().__init__(f"{self._personaje.get_nombre()} ha perdido toda su vida")

    