class Pedido:
    def __init__(self, id, data, total, estado, id_garcom, id_mesa):
        self.__id = id
        self.__data = data
        self.__total = total
        self.__estado = estado
        self.__id_garcom = id_garcom
        self.__id_mesa = id_mesa

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_total(self): return self.__total
    def get_estado(self): return self.__estado
    def get_id_garcom(self): return self.__id_garcom
    def get_id_mesa(self): return self.__id_mesa
