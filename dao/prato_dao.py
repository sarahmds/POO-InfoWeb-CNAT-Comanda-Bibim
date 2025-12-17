from database import Database
from models.prato import Prato

class PratoDAO:

    @staticmethod
    def inserir(prato):
        conn = Database.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO prato (nome, categoria, preco)
            VALUES (?, ?, ?)
        """, (prato.get_nome(), prato.get_categoria(), prato.get_preco()))

        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = Database.conectar()
        cur = conn.cursor()

        cur.execute("SELECT id, nome, categoria, preco FROM prato")
        rows = cur.fetchall()

        pratos = [Prato(r[0], r[1], r[2], r[3]) for r in rows]

        conn.close()
        return pratos
