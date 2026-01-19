from database import Database
from models.prato import Prato

class PratoDAO:
    @classmethod
    def inserir(cls, prato: Prato):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO prato (nome, descricao, preco) VALUES (?, ?, ?)",
            (prato.get_nome(), prato.get_descricao(), prato.get_preco())
        )
        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, descricao, preco FROM prato")
        rows = cur.fetchall()
        pratos = []
        for id_, nome, descricao, preco in rows:
            pratos.append(Prato(nome, descricao, preco, id=id_))  # passar id no construtor
        conn.close()
        return pratos

    @classmethod
    def atualizar(cls, prato: Prato):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE prato SET nome=?, descricao=?, preco=? WHERE id=?",
            (prato.get_nome(), prato.get_descricao(), prato.get_preco(), prato.get_id())
        )
        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, id_prato):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM prato WHERE id=?", (id_prato,))
        conn.commit()
        conn.close()
