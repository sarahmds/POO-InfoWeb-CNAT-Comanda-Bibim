from database import Database

class DAO:
    @classmethod
    def executar(cls, sql, params=()):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur, conn

    @classmethod
    def consultar(cls, sql, params=()):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
        conn.close()
        return rows
