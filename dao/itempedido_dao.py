# dao/item_pedido_dao.py
from .dao import DAO
from models.item_pedido import ItemPedido

class ItemPedidoDAO(DAO):

    @classmethod
    def inserir(cls, item: ItemPedido):
        sql = """
        INSERT INTO item_pedido (id_pedido, id_prato, quantidade, subtotal)
        VALUES (?, ?, ?, ?)
        """
        cls.executar(sql, (
            item.get_pedido().get_id(),
            item.get_prato().get_id(),
            item.get_quantidade(),
            item.subtotal()
        ))

    @classmethod
    def listar(cls):
        sql = "SELECT id, id_pedido, id_prato, quantidade, subtotal FROM item_pedido"
        rows = cls.consultar(sql)
        return rows
