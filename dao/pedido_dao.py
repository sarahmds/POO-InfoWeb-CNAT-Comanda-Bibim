from dao_sql.dao import DAO
from models.pedido import Pedido

class PedidoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO pedido (data, total, estado, id_usuario, id_mesa)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_data(), obj.get_total(), obj.get_estado(),
            obj.get_id_usuario(), obj.get_id_mesa()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM pedido"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Pedido(id, data, total, estado, id_usuario, id_mesa)
            for (id, data, total, estado, id_usuario, id_mesa) in rows
        ]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM pedido WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Pedido(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE pedido SET data=?, total=?, estado=?, id_usuario=?, id_mesa=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_data(), obj.get_total(), obj.get_estado(),
            obj.get_id_usuario(), obj.get_id_mesa(), obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM pedido WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
