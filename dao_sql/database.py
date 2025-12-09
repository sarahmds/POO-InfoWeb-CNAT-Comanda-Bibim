import sqlite3
from dao_sql.usuariodao import UsuarioDAO
from models.usuario import Usuario

class Database:
    conn = None
    nome_bd = "restaurante.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        if cls.conn:
            cls.conn.close()

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @classmethod
    def criar_tabelas(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                perfil TEXT NOT NULL
            );
        """)

        cls.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            );
        """)

        cls.execute("""
            CREATE TABLE IF NOT EXISTS mesa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                lugares INTEGER NOT NULL,
                situacao TEXT NOT NULL
            );
        """)

        cls.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL
            );
        """)

        cls.execute("""
            CREATE TABLE IF NOT EXISTS pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                total REAL NOT NULL,
                estado TEXT NOT NULL,
                id_cliente INTEGER,
                id_mesa INTEGER,
                FOREIGN KEY (id_cliente) REFERENCES cliente(id),
                FOREIGN KEY (id_mesa) REFERENCES mesa(id)
            );
        """)

        cls.execute("""
            CREATE TABLE IF NOT EXISTS itempedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                id_produto INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedido(id) ON DELETE CASCADE,
                FOREIGN KEY (id_produto) REFERENCES produto(id)
            );
        """)


def criar_gerente_padrao():
    dao = UsuarioDAO(Database.nome_bd)
usuarios = dao.listar_todos()
    existe = any(u.get_email() == "gerente" for u in usuarios)

    if not existe:
        gerente = Usuario(
            id=None,
            nome="Gerente do Sistema",
            email="gerente",   
            senha="",         
            perfil="gerente"
        )
        UsuarioDAO.inserir(gerente)
        print("Usuário gerente criado sem senha. Defina uma senha ao acessar.")


if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    criar_gerente_padrao()
    Database.fechar()
