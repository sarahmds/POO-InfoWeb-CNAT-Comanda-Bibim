from dao.dao import DAO
from models.prato import Prato

class PratoDAO(DAO):

    @classmethod
    def inserir(cls, prato):
        sql = "INSERT INTO prato (nome, categoria, preco) VALUES (?, ?, ?)"
        cls.executar(sql, (prato.get_nome(), prato.get_categoria(), prato.get_preco()))

    @classmethod
    def listar(cls):
        cur, conn = cls.executar("SELECT * FROM prato")
        pratos = [Prato(*row) for row in cur.fetchall()]
        conn.close()
        return pratos
