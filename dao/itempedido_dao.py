from dao_sql.dao import DAO
from models.itempedido import ItemPedido

class ItemPedidoDAO(DAO):

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO item_pedido (id_pedido, id_prato, quantidade, subtotal)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_id_pedido(), obj.get_prato().get_id(),
            obj.get_quantidade(), obj.subtotal()
        ))
        cls.fechar()

    @classmethod
    def listar_por_pedido(cls, id_pedido):
        cls.abrir()
        sql = "SELECT * FROM item_pedido WHERE id_pedido=?"
        cursor = cls.execute(sql, (id_pedido,))
        rows = cursor.fetchall()
        objs = [
            ItemPedido(id, id_pedido, id_produto, qtd, subtotal)
            for (id, id_pedido, id_produto, qtd, subtotal) in rows
        ]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM itempedido WHERE id=?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = ItemPedido(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM itempedido WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()
