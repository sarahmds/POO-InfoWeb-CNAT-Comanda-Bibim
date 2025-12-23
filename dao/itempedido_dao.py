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
        return cls.consultar(sql)

    @classmethod
    def atualizar(cls, item: ItemPedido):
        sql = """
        UPDATE item_pedido
        SET quantidade = ?, subtotal = ?
        WHERE id = ?
        """
        cls.executar(sql, (
            item.get_quantidade(),
            item.subtotal(),
            item.get_id()
        ))

    @classmethod
    def excluir(cls, id):
        sql = "DELETE FROM item_pedido WHERE id = ?"
        cls.executar(sql, (id,))
