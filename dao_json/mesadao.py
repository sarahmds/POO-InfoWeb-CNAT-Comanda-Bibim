import json
from dao_json.dao import DAO
from models.mesa import Mesa

class MesaDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("mesas.json", "r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = Mesa.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("mesas.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Mesa.to_json)
