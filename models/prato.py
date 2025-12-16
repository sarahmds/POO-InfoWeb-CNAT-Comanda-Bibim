class Prato:
    def __init__(self, id, nome, categoria, preco):
        self.__id = id
        self.__nome = nome
        self.__categoria = categoria
        self.__preco = preco

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_categoria(self): return self.__categoria
    def get_preco(self): return self.__preco

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__categoria}) R$ {self.__preco:.2f}"
