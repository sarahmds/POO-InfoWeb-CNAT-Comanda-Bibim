from database import Database
from models.item_pedido import ItemPedido
from dao.prato_dao import PratoDAO
from dao.pedido_dao import PedidoDAO

class ItemPedidoDAO:

    @classmethod
    def inserir(cls, item):
        conn = Database.conectar()
        cur = conn.cursor()

        subtotal = item.get_quantidade() * item.get_prato().get_preco()

        cur.execute(
            """
            INSERT INTO item_pedido (id_pedido, id_prato, quantidade, subtotal)
            VALUES (?, ?, ?, ?)
            """,
            (
                item.get_pedido().get_id(),
                item.get_prato().get_id(),
                item.get_quantidade(),
                subtotal
            )
        )

        conn.commit()
        conn.close()

    @classmethod
    def listar_por_pedido(cls, id_pedido):
        conn = Database.conectar()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT id, id_prato, quantidade
            FROM item_pedido
            WHERE id_pedido = ?
            """,
            (id_pedido,)
        )

        rows = cur.fetchall()
        conn.close()

        pedido = next(p for p in PedidoDAO.listar() if p.get_id() == id_pedido)

        itens = []
        for r in rows:
            prato = PratoDAO.buscar_por_id(r[1])
            item = ItemPedido(
                prato=prato,
                quantidade=r[2],
                pedido=pedido,
                id=r[0]          # 👈 ID PASSA AQUI
            )
            itens.append(item)

        return itens

    @classmethod
    def excluir(cls, id_item):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM item_pedido WHERE id = ?", (id_item,))
        conn.commit()
        conn.close()
