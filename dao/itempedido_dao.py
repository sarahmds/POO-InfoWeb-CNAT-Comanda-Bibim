from dao.dao import DAO
from models.item_pedido import ItemPedido
from models.prato import Prato
from dao.prato_dao import PratoDAO

class ItemPedidoDAO(DAO):

    @classmethod
    def inserir(cls, item):
        sql = """
        INSERT INTO item_pedido (id_pedido, id_prato, quantidade, subtotal)
        VALUES (?, ?, ?, ?)
        """
        cls.executar(sql, (
            item.get_pedido().get_id(),
            item.get_prato().get_id(),
            item.get_quantidade(),
            item.get_quantidade() * item.get_prato().get_preco()
        ))

    @classmethod
    def listar_por_pedido(cls, id_pedido):
        sql = "SELECT id, id_prato, quantidade, subtotal FROM item_pedido WHERE id_pedido = ?"
        rows = cls.consultar(sql, (id_pedido,))
        itens = []
        for row in rows:
            id_item, id_prato, quantidade, subtotal = row
            prato = PratoDAO.buscar_por_id(id_prato)  # agora existe
            item = ItemPedido(prato, quantidade, id_pedido)
            item.set_id(id_item)
            itens.append(item)
        return itens


    @classmethod
    def excluir(cls, id_item):
        sql = "DELETE FROM item_pedido WHERE id = ?"
        cls.executar(sql, (id_item,))
