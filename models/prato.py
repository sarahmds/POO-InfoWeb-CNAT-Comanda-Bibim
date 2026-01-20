class Prato:
    def __init__(self, nome: str, descricao: str, preco: float, id: int = None):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__descricao}) R$ {self.__preco:.2f}"
