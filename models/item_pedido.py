class ItemPedido:
    def __init__(self, prato, quantidade: int, pedido, id: int = None):
        self.__id = id
        self.__prato = prato     
        self.__quantidade = quantidade
        self.__pedido = pedido    

    def get_id(self):
        return self.__id

    def get_prato(self):
        return self.__prato

    def get_quantidade(self):
        return self.__quantidade

    def get_pedido(self):
        return self.__pedido

    def set_prato(self, prato):
        self.__prato = prato

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def set_pedido(self, pedido):
        self.__pedido = pedido

    def subtotal(self) -> float:
        """
        Assume que o objeto Prato possui o método get_preco()
        """
        return self.__quantidade * self.__prato.get_preco()
