from dao_sql.dao import DAO
from models.produto import Produto

class ProdutoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO produto (nome, categoria, preco)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_categoria(), obj.get_preco()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM produto"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Produto(id, nome, categoria, preco) for (id, nome, categoria, preco) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM produto WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Produto(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE produto SET nome=?, categoria=?, preco=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_categoria(), obj.get_preco(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM produto WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
