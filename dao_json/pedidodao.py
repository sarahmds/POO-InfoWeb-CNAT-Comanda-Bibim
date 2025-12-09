import json
from dao_json.dao import DAO
from models.pedido import Pedido

class PedidoDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("pedidos.json", "r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = Pedido.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("pedidos.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Pedido.to_json)
