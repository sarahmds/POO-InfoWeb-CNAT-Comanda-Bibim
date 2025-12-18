from dao.dao import DAO
from models.usuario import Usuario


class UsuarioDAO(DAO):

    @classmethod
    def inserir(cls, usuario: Usuario):
        usuario.validarDados()

        sql = """
        INSERT INTO usuario (nome, email, senha, perfil)
        VALUES (?, ?, ?, ?)
        """
        cls.executar(sql, (
            usuario.get_nome(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_perfil()
        ))
