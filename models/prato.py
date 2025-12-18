class Prato:
    def __init__(self, id, nome, preco):
        self.__id = id
        self.__nome = nome
        self.__preco = preco

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_preco(self): return self.__preco

    def __str__(self):
        return f"{self.__id} - {self.__nome}  R$ {self.__preco:.2f}"
