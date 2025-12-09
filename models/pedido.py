from datetime import datetime

class Pedido:
    def __init__(self, id, dataHora, status, mesa, garcom):
        self.set_id(id)
        self.set_dataHora(dataHora)
        self.set_status(status)
        self.set_mesa(mesa)
        self.set_garcom(garcom)
        self.__itens = []

    def get_id(self): return self.__id
    def get_dataHora(self): return self.__dataHora
    def get_status(self): return self.__status
    def get_mesa(self): return self.__mesa
    def get_garcom(self): return self.__garcom
    def get_itens(self): return self.__itens

    def set_id(self, id): self.__id = id
    def set_dataHora(self, dataHora): self.__dataHora = dataHora
    def set_status(self, status): self.__status = status
    def set_mesa(self, mesa): self.__mesa = mesa
    def set_garcom(self, garcom): self.__garcom = garcom

    def adicionar_item(self, item):
        self.__itens.append(item)

    def atualizar_status(self, novo_status):
        self.__status = novo_status

    def calcular_total(self):
        return sum(i.subtotal() for i in self.__itens)

    def to_json(self):
        return {
            "id": self.__id,
            "dataHora": self.__dataHora.strftime("%d/%m/%Y %H:%M"),
            "status": self.__status,
            "id_mesa": self.__mesa.get_id(),
            "id_garcom": self.__garcom.get_id(),
        }

    @staticmethod
    def from_json(dic, mesa, garcom):
        return Pedido(
            dic["id"],
            datetime.strptime(dic["dataHora"], "%d/%m/%Y %H:%M"),
            dic["status"],
            mesa,
            garcom
        )

    def __str__(self):
        return f"Pedido {self.__id} - Mesa {self.__mesa.get_numero()} - {self.__status}"
