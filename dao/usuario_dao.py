from dao.dao import DAO
from models.usuario import usuario

class usuarioDAO(DAO):

    @classmethod
    def inserir(cls, usuario):
        sql = "INSERT INTO usuario (nome, email, senha, perfil) VALUES (?, ?, ?, ?)"
        cls.executar(sql, (
            usuario.get_nome(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_perfil()
        ))
