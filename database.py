import sqlite3

class Database:
    NOME_BD = "comanda.db"

    @classmethod
    def conectar(cls):
        conn = sqlite3.connect(cls.NOME_BD)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @classmethod
    def criar_tabelas(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        # ===== USUARIO =====
        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL
        )
        """)

        # ===== MESA =====
        cur.execute("""
        CREATE TABLE IF NOT EXISTS mesa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            status TEXT NOT NULL
        )
        """)

        # ===== PRATO =====
        cur.execute("""
        CREATE TABLE IF NOT EXISTS prato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL
        )
        """)

        # ===== DIA =====
        cur.execute("""
        CREATE TABLE IF NOT EXISTS dia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            aberto INTEGER NOT NULL
        )
        """)

        # ===== PEDIDO =====
        cur.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mesa INTEGER NOT NULL,
            garcom INTEGER NOT NULL,
            status TEXT NOT NULL,
            dataHora TEXT NOT NULL,
            dia_id INTEGER,
            FOREIGN KEY (mesa) REFERENCES mesa(id),
            FOREIGN KEY (garcom) REFERENCES usuario(id),
            FOREIGN KEY (dia_id) REFERENCES dia(id)
        )
        """)

        # ===== ITEM PEDIDO =====
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
