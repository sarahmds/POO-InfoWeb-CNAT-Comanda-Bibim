from dao_sql.dao import DAO
from models.mesa import Mesa

class MesaDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO mesa (numero, , situacao)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_numero(), obj.get_situacao()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM mesa"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Mesa(id, numero, situacao) for (id, numero, situacao) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM mesa WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Mesa(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE mesa SET numero=?, situacao=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_numero(), obj.get_situacao(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM mesa WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
