from dao.dao import DAO
from models.pedido import Pedido

class PedidoDAO(DAO):

    @classmethod
    def inserir(cls, pedido):
        sql = """
        INSERT INTO pedido (data, total, estado, id_garcom, id_mesa)
        VALUES (?, ?, ?, ?, ?)
        """
        cls.executar(sql, (
            pedido.get_data(),
            pedido.get_total(),
            pedido.get_estado(),
            pedido.get_id_garcom(),
            pedido.get_id_mesa()
        ))
