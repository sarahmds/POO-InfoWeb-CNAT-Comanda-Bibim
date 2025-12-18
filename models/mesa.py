class Mesa:
    def __init__(self, id, numero, status):
        self.__id = id
        self.__numero = numero
        self.__status = status

    def get_id(self): return self.__id
    def get_numero(self): return self.__numero
    def get_status(self): return self.__status
