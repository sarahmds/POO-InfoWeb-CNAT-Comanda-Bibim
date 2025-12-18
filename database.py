import sqlite3

class Database:
    NOME_BD = "restaurante.db"

    @classmethod
    def conectar(cls):
        conn = sqlite3.connect(cls.NOME_BD)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @classmethod
    def criar_tabelas(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS mesa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            situacao TEXT NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS prato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            total REAL NOT NULL,
            estado TEXT NOT NULL,
            id_usuario INTEGER,
            id_mesa INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuario(id),
            FOREIGN KEY (id_mesa) REFERENCES mesa(id)
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS item_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pedido INTEGER NOT NULL,
            id_prato INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedido(id),
            FOREIGN KEY (id_prato) REFERENCES prato(id)
        )
        """)

        conn.commit()
        conn.close()
