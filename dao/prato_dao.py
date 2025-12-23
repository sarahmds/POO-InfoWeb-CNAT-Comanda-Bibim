from .dao import DAO
from models.prato import Prato

class PratoDAO(DAO):

    @classmethod
    def inserir(cls, prato: Prato):
        sql = "INSERT INTO prato (nome, descricao, preco) VALUES (?, ?, ?)"
        cls.executar(sql, (
            prato.get_nome(),
            prato.get_descricao(),
            prato.get_preco()
        ))

    @classmethod
    def listar(cls):
        sql = "SELECT id, nome, descricao, preco FROM prato"
        rows = cls.consultar(sql)
        return [Prato(r[1], r[2], r[3], r[0]) for r in rows]

    @classmethod
    def atualizar(cls, prato: Prato):
        sql = """
        UPDATE prato
        SET nome = ?, descricao = ?, preco = ?
        WHERE id = ?
        """
        cls.executar(sql, (
            prato.get_nome(),
            prato.get_descricao(),
            prato.get_preco(),
            prato.get_id()
        ))

    @classmethod
    def excluir(cls, id):
        sql = "DELETE FROM prato WHERE id = ?"
        cls.executar(sql, (id,))
