class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_preco(preco)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço inválido")
        self.__preco = preco

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "descricao": self.__descricao,
            "preco": self.__preco
        }

    @staticmethod
    def from_json(dic):
        return Prato(dic["id"], dic["nome"], dic["descricao"], dic["preco"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - R${self.__preco:.2f}"
