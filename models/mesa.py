class Mesa:
    def __init__(self, numero: int, status, id: int = None):
        self.__id = id
        self.__numero = numero
        self.__status = status

    def get_id(self):
        return self.__id

    def get_numero(self):
        return self.__numero

    def get_status(self):
        return self.__status

    def set_numero(self, numero):
        self.__numero = numero

    def set_status(self, status):
        self.__status = status

    def ocupar(self):
        self.__status = "OCUPADA"

    def liberar(self):
        self.__status = "LIVRE"
