from datetime import datetime


class Pedido:
    def __init__(self, mesa, garcom, status, dataHora=None, id=None):
        self.__id = id
        self.__dataHora = dataHora or datetime.now()
        self.__status = status
        self.__mesa = mesa
        self.__garcom = garcom
        self.__itens = []  # lista de (id_prato, qtd, preco)

    # ===== GETTERS =====
    def get_id(self):
        return self.__id

    def get_dataHora(self):
        return self.__dataHora

    def get_status(self):
        return self.__status

    def get_mesa(self):
        return self.__mesa

    def get_garcom(self):
        return self.__garcom

    # ===== SETTERS =====
    def set_status(self, status):
        self.__status = status

    def set_mesa(self, mesa):
        self.__mesa = mesa

    def set_garcom(self, garcom):
        self.__garcom = garcom

    def adicionarItem(self, prato: int, qtd: int, preco: float):
        self.__itens.append((prato, qtd, preco))

    def calcularTotal(self):
        total = 0
        for _, qtd, preco in self.__itens:
            total += qtd * preco
        return total

    def atualizarStatus(self, novo_status):
        self.__status = novo_status
