from database import Database

class DAO:
    @classmethod
    def executar(cls, sql, params=()):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur, conn
