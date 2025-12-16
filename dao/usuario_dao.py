import sqlite3
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, arquivo_banco):
        self.__arquivo_banco = arquivo_banco

    def conectar(self):
        return sqlite3.connect(self.__arquivo_banco)

    def inserir(self, usuario: Usuario):
        con = self.conectar()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO usuario (nome, email, senha, perfil)
            VALUES (?, ?, ?, ?)
        """, (usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_perfil()))
        con.commit()
        con.close()

    def listar_todos(self):
        con = self.conectar()
        cur = con.cursor()
        cur.execute("SELECT id, nome, email, senha, perfil FROM usuario")
        rows = cur.fetchall()
        con.close()

        return [Usuario(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def buscar_por_email(self, email):
        con = self.conectar()
        cur = con.cursor()
        cur.execute("SELECT id, nome, email, senha, perfil FROM usuario WHERE email = ?", (email,))
        row = cur.fetchone()
        con.close()
        if row:
            return Usuario(row[0], row[1], row[2], row[3], row[4])
        return None

    def atualizar(self, usuario: Usuario):
        con = self.conectar()
        cur = con.cursor()
        cur.execute("""
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?, perfil = ?
            WHERE id = ?
        """, (usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_perfil(), usuario.get_id()))
        con.commit()
        con.close()

    def excluir(self, id_usuario):
        con = self.conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM usuario WHERE id = ?", (id_usuario,))
        con.commit()
        con.close()
