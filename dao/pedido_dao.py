from .dao import DAO
from models.pedido import Pedido
from datetime import datetime

class PedidoDAO(DAO):

    @classmethod
    def inserir(cls, pedido: Pedido):
        sql = """
        INSERT INTO pedido (data_hora, status, id_garcom, id_mesa, total)
        VALUES (?, ?, ?, ?, ?)
        """
        cls.executar(sql, (
            pedido.get_dataHora().strftime("%Y-%m-%d %H:%M:%S"),
            pedido.get_status(),
            pedido.get_garcom(),
            pedido.get_mesa(),
            pedido.calcularTotal()
        ))

    @classmethod
    def listar(cls):
        sql = "SELECT id, data_hora, status, id_garcom, id_mesa, total FROM pedido"
        rows = cls.consultar(sql)
        pedidos = []
        for r in rows:
            pedidos.append(Pedido(
                mesa=r[4],
                garcom=r[3],
                status=r[2],
                dataHora=datetime.strptime(r[1], "%Y-%m-%d %H:%M:%S"),
                id=r[0]
            ))
        return pedidos

    @classmethod
    def atualizar(cls, pedido: Pedido):
        sql = """
        UPDATE pedido
        SET status = ?, total = ?
        WHERE id = ?
        """
        cls.executar(sql, (
            pedido.get_status(),
            pedido.calcularTotal(),
            pedido.get_id()
        ))

    @classmethod
    def excluir(cls, id):
        sql = "DELETE FROM pedido WHERE id = ?"
        cls.executar(sql, (id,))
