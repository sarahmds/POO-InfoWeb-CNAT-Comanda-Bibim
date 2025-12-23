from .dao import DAO
from models.mesa import Mesa

class MesaDAO(DAO):

    @classmethod
    def inserir(cls, mesa: Mesa):
        sql = "INSERT INTO mesa (numero, status) VALUES (?, ?)"
        cls.executar(sql, (
            mesa.get_numero(),
            mesa.get_status()
        ))

    @classmethod
    def listar(cls):
        sql = "SELECT id, numero, status FROM mesa"
        rows = cls.consultar(sql)
        return [Mesa(r[1], r[2], r[0]) for r in rows]

    @classmethod
    def atualizar(cls, mesa: Mesa):
        sql = """
        UPDATE mesa
        SET numero = ?, status = ?
        WHERE id = ?
        """
        cls.executar(sql, (
            mesa.get_numero(),
            mesa.get_status(),
            mesa.get_id()
        ))

    @classmethod
    def excluir(cls, id):
        sql = "DELETE FROM mesa WHERE id = ?"
        cls.executar(sql, (id,))
