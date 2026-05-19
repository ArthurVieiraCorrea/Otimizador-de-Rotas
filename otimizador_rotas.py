import math
from ponto_entrega import Ponto_entrega
from pedido import Pedido
from veiculo import Veiculo
from rota import Rota

class OtimizadorRotas:
    DEPOSITO = Ponto_entrega(0, 0)

    def __init__(self):
        self._pedidos_nao_alocados = []

    @property
    def pedidos_nao_alocados(self):
        return self._pedidos_nao_alocados

    def calcular_distancia(self, p1: Ponto_entrega, p2: Ponto_entrega) -> float:
        return math.sqrt((p2.coordenada_x - p1.coordenada_x)**2 + (p2.coordenada_y - p1.coordenada_y)**2)

    def processar_vizinho_proximo(self, rota):
        """
        Recebe um objeto Rota, extrai os pedidos que foram inseridos nela,
        ordena-os usando o algoritmo do vizinho mais próximo e calcula os totais.
        """
        if not rota.pedidos:
            print("[AVISO]: Esta rota não possui pedidos para otimizar.")
            return

        pedidos_para_ordenar = list(rota.pedidos)
        rota.pedidos.clear()

        ponto_atual = self.DEPOSITO
        capacidade_gasta = 0.0
        self._pedidos_nao_alocados.clear()  # Limpa os rejeitados da execução anterior

        while pedidos_para_ordenar:
            proximo_pedido = None
            menor_distancia = float('inf')

            for pedido in pedidos_para_ordenar:
                dist = self.calcular_distancia(ponto_atual, pedido.ponto_entrega)
                if dist < menor_distancia:
                    menor_distancia = dist
                    proximo_pedido = pedido

            if proximo_pedido:
                if capacidade_gasta + proximo_pedido.peso_encomenda <= rota.veiculo.capacidade:
                    rota.adicionar_pedido(proximo_pedido)
                    capacidade_gasta += proximo_pedido.peso_encomenda
                    ponto_atual = proximo_pedido.ponto_entrega 
                else:
                    
                    self._pedidos_nao_alocados.append(proximo_pedido)
                
               
                pedidos_para_ordenar.remove(proximo_pedido)

       
        distancia_total = 0.0
        ponto_anterior = self.DEPOSITO
        
        for ped in rota.pedidos:
            distancia_total += self.calcular_distancia(ponto_anterior, ped.ponto_entrega)
            ponto_anterior = ped.ponto_entrega
            
        distancia_total += self.calcular_distancia(ponto_anterior, self.DEPOSITO)
        
        rota.distancia_total = distancia_total
        rota.carga_total = capacidade_gasta