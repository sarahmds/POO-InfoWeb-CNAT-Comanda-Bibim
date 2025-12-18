from dao.dao import DAO
from models.mesa import Mesa

class MesaDAO(DAO):

    @classmethod
    def inserir(cls, mesa):
        sql = "INSERT INTO mesa (numero, status) VALUES (?, ?)"
        cls.executar(sql, (mesa.get_numero(), mesa.get_status()))
