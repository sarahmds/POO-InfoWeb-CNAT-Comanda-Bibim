class Mesa:
    def __init__(self, id, numero, status):
        self.set_id(id)
        self.set_numero(numero)
        self.set_status(status) 

    def get_id(self): return self.__id
    def get_numero(self): return self.__numero
    def get_status(self): return self.__status

    def set_id(self, id): self.__id = id
    def set_numero(self, numero): self.__numero = numero
    def set_status(self, status): self.__status = status

    def ocupar(self): self.__status = "ocupada"
    def liberar(self): self.__status = "livre"

    def to_json(self):
        return {
            "id": self.__id,
            "numero": self.__numero,
            "status": self.__status
        }

    @staticmethod
    def from_json(dic):
        return Mesa(dic["id"], dic["numero"], dic["status"])

    def __str__(self):
        return f"Mesa {self.__numero} - {self.__status}"
