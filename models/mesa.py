class Mesa:
    def __init__(self, id, numero, situacao):
        self.__id = id
        self.__numero = numero
        self.__situacao = situacao

    def get_id(self): return self.__id
    def get_numero(self): return self.__numero
    def get_situacao(self): return self.__situacao
