from database import Database
from models.dia import Dia

class DiaDAO:

    @classmethod
    def listar(cls):
        """Lista todos os dias"""
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, data, aberto FROM dia ORDER BY data DESC")
        rows = cur.fetchall()
        conn.close()

        dias = []
        for r in rows:
            dias.append(Dia(id=r[0], data=r[1], aberto=r[2]))
        return dias

    @classmethod
    def dia_aberto(cls):
        """Retorna o dia que está aberto (se houver)"""
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, data, aberto FROM dia WHERE aberto = 1")
        row = cur.fetchone()
        conn.close()
        if row:
            return Dia(id=row[0], data=row[1], aberto=row[2])
        return None

    @classmethod
    def buscar_por_id(cls, id_dia):
        """Retorna um dia pelo ID"""
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, data, aberto FROM dia WHERE id = ?", (id_dia,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Dia(id=row[0], data=row[1], aberto=row[2])
        return None

    @classmethod
    def inserir(cls, dia):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO dia (data, aberto) VALUES (?, ?)", (dia.get_data(), dia.get_aberto()))
        conn.commit()
        conn.close()

    @classmethod
    def atualizar(cls, dia):
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("UPDATE dia SET data = ?, aberto = ? WHERE id = ?", (dia.get_data(), dia.get_aberto(), dia.get_id()))
        conn.commit()
        conn.close()
