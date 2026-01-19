from database import Database
from models.pedido import Pedido

class PedidoDAO:

    @classmethod
    def listar(cls):
        """Lista todos os pedidos"""
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, mesa, garcom, status, dataHora, dia_id FROM pedido ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()

        pedidos = []
        for r in rows:
            pedidos.append(Pedido(
                id=r[0],
                mesa=r[1],
                garcom=r[2],
                status=r[3],
                dataHora=r[4],
                dia_id=r[5]
            ))
        return pedidos

    @classmethod
    def listar_por_dia(cls, id_dia):
        """Lista todos os pedidos de um dia específico"""
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, mesa, garcom, status, dataHora, dia_id FROM pedido WHERE dia_id = ? ORDER BY id DESC",
            (id_dia,)
        )
        rows = cur.fetchall()
        conn.close()

        pedidos = []
        for r in rows:
            pedidos.append(Pedido(
                id=r[0],
                mesa=r[1],
                garcom=r[2],
                status=r[3],
                dataHora=r[4],
                dia_id=r[5]
            ))
        return pedidos

    @classmethod
    def inserir(cls, pedido):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO pedido (mesa, garcom, status, dataHora, dia_id) VALUES (?, ?, ?, ?, ?)",
            (pedido.get_mesa(), pedido.get_garcom(), pedido.get_status(), pedido.get_dataHora(), getattr(pedido, "dia_id", None))
        )
        conn.commit()
        conn.close()

    @classmethod
    def atualizar(cls, pedido):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE pedido SET mesa=?, garcom=?, status=?, dataHora=?, dia_id=? WHERE id=?",
            (pedido.get_mesa(), pedido.get_garcom(), pedido.get_status(), pedido.get_dataHora(), getattr(pedido, "dia_id", None), pedido.get_id())
        )
        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, id_pedido):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM pedido WHERE id=?", (id_pedido,))
        conn.commit()
        conn.close()
