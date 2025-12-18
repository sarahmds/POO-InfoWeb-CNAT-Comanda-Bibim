from dao.dao import DAO
from models.pedido import Pedido


class PedidoDAO(DAO):

    @classmethod
    def inserir(cls, pedido: Pedido):
        sql = """
        INSERT INTO pedido (data_hora, status, id_garcom, id_mesa, total)
        VALUES (?, ?, ?, ?, ?)
        """
        cls.executar(sql, (
            pedido.get_dataHora(),
            pedido.get_status(),
            pedido.get_garcom(),
            pedido.get_mesa(),
            pedido.calcularTotal()
        ))
