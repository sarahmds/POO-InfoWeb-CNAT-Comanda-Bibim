import json
from dao_json.dao import DAO
from models.produto import Produto

class ProdutoDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = Produto.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Produto.to_json)
