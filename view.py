import sqlite3
from database import Database
from models.usuario import Usuario
from models.mesa import Mesa
from models.prato import Prato
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from models.dia import Dia

from dao.usuario_dao import UsuarioDAO
from dao.mesa_dao import MesaDAO
from dao.prato_dao import PratoDAO
from dao.pedido_dao import PedidoDAO
from dao.itempedido_dao import ItemPedidoDAO
from dao.dia_dao import DiaDAO

from datetime import datetime


class View:

    # ===== USUÁRIO =====
    @staticmethod
    def usuario_criar_gerente_padrao():
        Database.criar_tabelas()
        for u in UsuarioDAO.listar():
            if u.get_email() == "admin@admin.com":
                return
        UsuarioDAO.inserir(
            Usuario("admin", "admin@admin.com", "admin", "GERENTE")
        )

    @staticmethod
    def usuario_autenticar(email, senha):
        for u in UsuarioDAO.listar():
            if u.get_email() == email and u.get_senha() == senha:
                return {
                    "id": u.get_id(),
                    "nome": u.get_nome(),
                    "perfil": u.get_perfil()
                }
        return None

    @staticmethod
    def usuario_inserir(nome, email, senha, perfil):
        try:
            UsuarioDAO.inserir(Usuario(nome, email, senha, perfil))
        except sqlite3.IntegrityError:
            raise ValueError("E-mail já cadastrado")

    @staticmethod
    def usuario_listar():
        return UsuarioDAO.listar()

    @staticmethod
    def usuario_atualizar(id_usuario, nome, email, senha, perfil):
        try:
            usuario = Usuario(id=id_usuario, nome=nome, email=email, senha=senha, perfil=perfil)
            UsuarioDAO.atualizar(usuario)
        except sqlite3.IntegrityError:
            raise ValueError("E-mail já cadastrado")

    @staticmethod
    def usuario_excluir(id_usuario):
        UsuarioDAO.excluir(id_usuario)

    # ===== MESA =====
    @staticmethod
    def mesa_inserir(numero):
        MesaDAO.inserir(Mesa(numero))

    @staticmethod
    def mesa_listar():
        return MesaDAO.listar()

    @staticmethod
    def mesa_ocupar(id_mesa):
        for m in MesaDAO.listar():
            if m.get_id() == id_mesa:
                m.ocupar()
                MesaDAO.atualizar(m)

    @staticmethod
    def mesa_liberar(id_mesa):
        for m in MesaDAO.listar():
            if m.get_id() == id_mesa:
                m.liberar()
                MesaDAO.atualizar(m)

    @staticmethod
    def mesa_excluir(id_mesa):
        MesaDAO.excluir(id_mesa)

    @staticmethod
    def pedido_por_mesa(id_mesa):
        for p in PedidoDAO.listar():
            if p.get_mesa() == id_mesa and p.get_status() in ["ABERTO", "EM ANDAMENTO"]:
                return p
        return None

    # ===== PRATO =====
    @staticmethod
    def prato_inserir(nome, descricao, preco):
        PratoDAO.inserir(Prato(nome, descricao, preco))

    @staticmethod
    def prato_listar():
        return PratoDAO.listar()

    @staticmethod
    def prato_excluir(id_prato):
        PratoDAO.excluir(id_prato)

    @staticmethod
    def prato_atualizar(id_prato, nome, descricao, preco):
        prato = Prato(id=id_prato, nome=nome, descricao=descricao, preco=preco)
        PratoDAO.atualizar(prato)

    # ===== PEDIDO =====
    @staticmethod
    def pedido_criar(id_mesa, id_garcom):
        pedido = Pedido(
            mesa=id_mesa,
            garcom=id_garcom,
            status="ABERTO",
            dataHora=datetime.now()
        )
        PedidoDAO.inserir(pedido)

    @staticmethod
    def pedido_listar():
        return PedidoDAO.listar()

    @staticmethod
    def pedido_atualizar_status(id_pedido, status):
        for p in PedidoDAO.listar():
            if p.get_id() == id_pedido:
                p.atualizarStatus(status)
                PedidoDAO.atualizar(p)

    @staticmethod
    def pedidos_do_dia():
        # Retorna apenas pedidos do dia aberto
        dia_atual = DiaDAO.dia_aberto()
        if not dia_atual:
            return []
        return PedidoDAO.listar_por_dia(dia_atual.get_id())

    @staticmethod
    def pedidos_do_dia_id(id_dia):
        return PedidoDAO.listar_por_dia(id_dia)

    # ===== ITEM PEDIDO =====
    @staticmethod
    def item_pedido_inserir(pedido, prato, quantidade):
        ItemPedidoDAO.inserir(ItemPedido(prato, quantidade, pedido))

    @staticmethod
    def item_pedido_listar(id_pedido):
        return ItemPedidoDAO.listar_por_pedido(id_pedido)

    @staticmethod
    def item_pedido_excluir(id_item):
        ItemPedidoDAO.excluir(id_item)

    # ===== DIA =====
    @staticmethod
    def dia_abrir():
        conn = Database.conectar()
        conn.execute("INSERT INTO dia (data, aberto) VALUES (date('now'), 1)")
        conn.commit()
        conn.close()

    @staticmethod
    def dia_fechar():
        conn = Database.conectar()
        conn.execute("UPDATE dia SET aberto = 0 WHERE aberto = 1")
        conn.commit()
        conn.close()

    @staticmethod
    def dia_aberto():
        conn = Database.conectar()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*), id FROM dia WHERE aberto = 1")
        resultado = cur.fetchone()
        conn.close()
        if resultado[0] > 0:
            return DiaDAO.buscar_por_id(resultado[1])
        return None

    @staticmethod
    def listar_dias():
        return DiaDAO.listar()
