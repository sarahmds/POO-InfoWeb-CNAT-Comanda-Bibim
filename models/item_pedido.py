class ItemPedido:
    def __init__(self, id, id_pedido, id_prato, quantidade, subtotal):
        self.__id = id
        self.__id_pedido = id_pedido
        self.__id_prato = id_prato
        self.__quantidade = quantidade
        self.__subtotal = subtotal

    def get_id(self): return self.__id
    def get_id_pedido(self): return self.__id_pedido
    def get_id_prato(self): return self.__id_prato
    def get_quantidade(self): return self.__quantidade
    def get_subtotal(self): return self.__subtotal
