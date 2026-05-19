from veiculo import Veiculo
from pedido import Pedido

class Rota:
    def __init__(self, pedidos_iniciais: list, veiculo: Veiculo, motorista: str):
       
        self._pedidos = []
        self._motorista = motorista
        self._veiculo = veiculo
        self._distancia_total = 0.0

    @property
    def distancia_total(self) -> float:
        return self._distancia_total
    
    @distancia_total.setter
    def distancia_total(self, valor: float):
        self._distancia_total = valor

    @property
    def pedidos(self) -> list: 
        return self._pedidos
    
    @property
    def veiculo(self) -> Veiculo: 
        return self._veiculo
    
    @property
    def motorista(self) -> str:
        return self._motorista

   
    @property
    def carga_total(self) -> float:
        return self.calcular_peso_atual()
    
    @carga_total.setter
    def carga_total(self, valor: float):
        pass

    def calcular_peso_atual(self) -> float:
        return sum(pedido.peso_encomenda for pedido in self._pedidos)
    
    def adicionar_pedido(self, pedido: Pedido):
        self._pedidos.append(pedido)

    def __str__(self) -> str:
        """
        Formata a saída da rota de forma limpa e profissional,
        convertendo a lista de objetos em um itinerário de texto legível.
        """
        cabecalho = (
            f"Veículo: {self.veiculo.modelo}\n"
            f"Motorista: {self.motorista}\n"
            f"Capacidade Máxima: {self.veiculo.capacidade} kg\n"
            f"Carga Total Alocada: {self.calcular_peso_atual():.2f} kg\n"
            f"Distância Total do Circuito: {self.distancia_total:.2f} km\n"
        )
        
        caminho = "Depósito"
        if self._pedidos:
            for pedido in self._pedidos:
                caminho += f" -> {pedido.nome}" 
            caminho += " -> Depósito"
        else:
            caminho += " -> (Sem entregas) -> Depósito"
            
        return f"{cabecalho}\nItinerário Planejado:\n{caminho}"