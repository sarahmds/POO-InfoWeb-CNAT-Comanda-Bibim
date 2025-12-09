import json
from dao_json.dao import DAO
from models.itempedido import ItemPedido

class ItemPedidoDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("itenspedido.json", "r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = ItemPedido.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("itenspedido.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=ItemPedido.to_json)
