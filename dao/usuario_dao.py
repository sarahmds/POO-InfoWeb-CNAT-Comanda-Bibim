from dao.dao import DAO
from models.garcom import garcom

class garcomDAO(DAO):

    @classmethod
    def inserir(cls, garcom):
        sql = "INSERT INTO garcom (nome, email, senha, perfil) VALUES (?, ?, ?, ?)"
        cls.executar(sql, (
            garcom.get_nome(),
            garcom.get_email(),
            garcom.get_senha(),
            garcom.get_perfil()
        ))
