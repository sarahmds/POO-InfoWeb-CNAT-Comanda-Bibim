import json
from dao_json.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("clientes.json", "r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = Cliente.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Cliente.to_json)
