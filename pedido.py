from cliente import Cliente
from ponto_entrega import Ponto_entrega
class Pedido:
    def __init__(self, nome:str, cliente:Cliente, ponto_entrega:Ponto_entrega, peso_encomenda:float):
        self._nome =  nome
        self._cliente = cliente
        self._ponto_entrega= ponto_entrega
        self._peso_encomenda= peso_encomenda
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def cliente(self) -> str:
        return self._cliente
    
    @property
    def ponto_entrega(self) -> str:
        return self._ponto_entrega
    
    @property
    def peso_encomenda(self) -> float:
        return self._peso_encomenda
    
    def __str__(self) -> str:
        return f"Pedido {self._nome} de {self._cliente} em ponto de entrega: {self._ponto_entrega} com {self._peso_encomenda} kg"