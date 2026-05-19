class Cliente:
    def __init__(self, nome:str, id:str):
        self._nome= nome
        self._id = id
    
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def id(self) -> float:
        return self._id
    
    def __str__(self) -> str:
        return f"Cliente: {self._nome} | ID: {self._id}"