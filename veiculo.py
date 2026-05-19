class Veiculo:
    def __init__(self, modelo:str, capacidade:float):
        self._modelo= modelo
        self._capacidade = capacidade
    
    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def capacidade(self) -> float:
        return self._capacidade
    
    def __str__(self) -> str:
        return f"Veículo: {self._modelo} | Capacidade: {self._capacidade} kg"
    