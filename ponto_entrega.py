class Ponto_entrega:
    def __init__(self, coordenada_x:int, coordenada_y:int):
        self._coordenada_x= coordenada_x
        self._coordenada_y = coordenada_y
    
    @property
    def coordenada_x(self) -> int:
        return self._coordenada_x

    @property
    def coordenada_y(self) -> int:
        return self._coordenada_y
    
    def __str__(self) -> str:
        return f"Ponto de entrega X: {self._coordenada_x} | Y: {self._coordenada_y}"
    

