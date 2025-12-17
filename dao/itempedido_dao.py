from dao.dao import DAO
from models.item_pedido import ItemPedido

class ItemPedidoDAO(DAO):

    @classmethod
    def inserir(cls, item):
        sql = """
        INSERT INTO item_pedido (id_pedido, id_prato, quantidade, subtotal)
        VALUES (?, ?, ?, ?)
        """
        cls.executar(sql, (
            item.get_id_pedido(),
            item.get_id_prato(),
            item.get_quantidade(),
            item.get_subtotal()
        ))
