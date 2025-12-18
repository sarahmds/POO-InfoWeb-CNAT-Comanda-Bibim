# models/mesa.py
class Mesa:
    def __init__(self, numero: int, status: str = "LIVRE", id: int = None):
        self.__id = id
        self.__numero = numero
        self.__status = status

    def get_id(self):
        return self.__id

    def get_numero(self):
        return self.__numero

    def get_status(self):
        return self.__status

    def ocupar(self):
        self.__status = "OCUPADA"

    def liberar(self):
        self.__status = "LIVRE"

    def __str__(self):
        return f"Mesa {self.__numero} - {self.__status}"
