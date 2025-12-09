from dao_sql.dao import DAO
from models.prato import Prato

class PratoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO prato (nome, categoria, preco)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_categoria(), obj.get_preco()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM prato"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Prato(id, nome, categoria, preco) for (id, nome, categoria, preco) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM prato WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Prato(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE prato SET nome=?, categoria=?, preco=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_categoria(), obj.get_preco(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM prato WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
