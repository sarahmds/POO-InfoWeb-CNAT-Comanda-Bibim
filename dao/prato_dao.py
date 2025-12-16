from dao.dao import DAO
from models.prato import Prato

class PratoDAO(DAO):

    @classmethod
    def inserir(cls, prato):
        sql = "INSERT INTO prato (nome, categoria, preco) VALUES (?, ?, ?)"
        cls.executar(sql, (prato.get_nome(), prato.get_categoria(), prato.get_preco()))

    @classmethod
    def listar(cls):
        sql = "SELECT * FROM prato"
        cur, conn = cls.executar(sql)
        rows = cur.fetchall()
        conn.close()
        return [Prato(*row) for row in rows]
