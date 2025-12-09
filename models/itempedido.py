class ItemPedido:
    def __init__(self, id, prato, quantidade, id_pedido):
        self.set_id(id)
        self.set_prato(prato)
        self.set_quantidade(quantidade)
        self.set_id_pedido(id_pedido)

    def get_id(self): return self.__id
    def get_prato(self): return self.__prato
    def get_quantidade(self): return self.__quantidade
    def get_id_pedido(self): return self.__id_pedido

    def set_id(self, id): self.__id = id
    def set_prato(self, prato): self.__prato = prato
    def set_quantidade(self, quantidade): self.__quantidade = quantidade
    def set_id_pedido(self, id_pedido): self.__id_pedido = id_pedido

    def subtotal(self):
        return self.__prato.get_preco() * self.__quantidade

    def to_json(self):
        return {
            "id": self.__id,
            "id_prato": self.__prato.get_id(),
            "quantidade": self.__quantidade,
            "id_pedido": self.__id_pedido,
            "subtotal": self.subtotal()
        }

    @staticmethod
    def from_json(dic, prato):
        return ItemPedido(dic["id"], prato, dic["quantidade"], dic["id_pedido"])

    def __str__(self):
        return f"{self.__quantidade}x {self.__prato.get_nome()} (R${self.subtotal():.2f})"
