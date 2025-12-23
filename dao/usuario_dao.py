from .dao import DAO
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

    @classmethod
    def listar(cls):
        sql = "SELECT id, nome, email, senha, perfil FROM usuario"
        rows = cls.consultar(sql)
        return [Usuario(r[1], r[2], r[3], r[4], id=r[0]) for r in rows]

    @classmethod
    def atualizar(cls, usuario: Usuario):
        sql = """
        UPDATE usuario
        SET nome = ?, email = ?, senha = ?, perfil = ?
        WHERE id = ?
        """
        cls.executar(sql, (
            usuario.get_nome(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_perfil(),
            usuario.get_id()
        ))

    @classmethod
    def excluir(cls, id):
        sql = "DELETE FROM usuario WHERE id = ?"
        cls.executar(sql, (id,))
