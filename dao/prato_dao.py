from dao.dao import DAO
from models.prato import Prato

class PratoDAO(DAO):

    @classmethod
    def inserir(cls, prato):
        sql = "INSERT INTO prato (nome, descricao, preco) VALUES (?, ?, ?)"
        cls.executar(sql, (prato.get_nome(), prato.get_descricao(), prato.get_preco()))

    @classmethod
    def listar(cls):
        sql = "SELECT id, nome, descricao, preco FROM prato"
        rows = cls.consultar(sql)
        pratos = []
        for row in rows:
            id_, nome, descricao, preco = row
            pratos.append(Prato(nome, descricao, preco, id_))
        return pratos

    @classmethod
    def atualizar(cls, prato):
        sql = "UPDATE prato SET nome = ?, descricao = ?, preco = ? WHERE id = ?"
        cls.executar(sql, (prato.get_nome(), prato.get_descricao(), prato.get_preco(), prato.get_id()))

    @classmethod
    def excluir(cls, id_prato):
        sql = "DELETE FROM prato WHERE id = ?"
        cls.executar(sql, (id_prato,))

    @classmethod
    def buscar_por_id(cls, id_prato):
        sql = "SELECT id, nome, descricao, preco FROM prato WHERE id = ?"
        row = cls.consultar(sql, (id_prato,))
        if row:
            id_, nome, descricao, preco = row[0]
            return Prato(nome, descricao, preco, id_)
        return None
