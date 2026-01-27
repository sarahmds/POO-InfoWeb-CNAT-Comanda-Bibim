import sqlite3
from datetime import datetime

from database import Database

# ===== MODELS =====
from models.usuario import Usuario
from models.mesa import Mesa
from models.prato import Prato
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from models.dia import Dia

# ===== DAOs =====
from dao.usuario_dao import UsuarioDAO
from dao.mesa_dao import MesaDAO
from dao.prato_dao import PratoDAO
from dao.pedido_dao import PedidoDAO
from dao.itempedido_dao import ItemPedidoDAO
from dao.dia_dao import DiaDAO


class View:

    # ===== USUÁRIO =====
    @staticmethod
    def usuario_listar():
        return UsuarioDAO.listar()

    @staticmethod
    def usuario_inserir(nome, email, senha, perfil):
        try:
            UsuarioDAO.inserir(Usuario(nome, email, senha, perfil))
            return True, "Usuário cadastrado com sucesso"
        except sqlite3.IntegrityError:
            return False, "Usuário já existe"

    @staticmethod
    def usuario_atualizar(usuario):
        UsuarioDAO.atualizar(usuario)

    @staticmethod
    def usuario_excluir(id_usuario):
        UsuarioDAO.excluir(id_usuario)

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
    def usuario_inserir_gerente_padrao():
        Database.criar_tabelas()
        for u in UsuarioDAO.listar():
            if u.get_email() == "admin@admin.com":
                return
        UsuarioDAO.inserir(
            Usuario("admin", "admin@admin.com", "admin", "GERENTE")
        )

    # ===== MESA =====
    @staticmethod
    def mesa_listar():
        return MesaDAO.listar()

    @staticmethod
    def mesa_inserir(numero):
        MesaDAO.inserir(Mesa(numero))

    @staticmethod
    def mesa_atualizar(mesa):
        MesaDAO.atualizar(mesa)

    @staticmethod
    def mesa_excluir(id_mesa):
        MesaDAO.excluir(id_mesa)

    @staticmethod
    def mesa_liberar(id_mesa):
        mesa = next((m for m in MesaDAO.listar() if m.get_id() == id_mesa), None)
        if not mesa:
            return False

        pedidos = [p for p in PedidoDAO.listar() if p.get_mesa() == id_mesa]
        if pedidos and any(p.get_status() != "PAGO" for p in pedidos):
            return False

        mesa.liberar()
        MesaDAO.atualizar(mesa)
        return True

    # ===== PRATO =====
    @staticmethod
    def prato_listar():
        return PratoDAO.listar()

    @staticmethod
    def prato_inserir(nome, preco):
        PratoDAO.inserir(Prato(nome, preco))

    @staticmethod
    def prato_atualizar(prato):
        PratoDAO.atualizar(prato)

    @staticmethod
    def prato_excluir(id_prato):
        PratoDAO.excluir(id_prato)

    # ===== PEDIDO =====
    @staticmethod
    def pedido_listar():
        return PedidoDAO.listar()

    @staticmethod
    def pedido_inserir(id_mesa, id_garcom):
        pedido = Pedido(
            mesa=id_mesa,
            garcom=id_garcom,
            status="ABERTO",
            dataHora=datetime.now()
        )
        PedidoDAO.inserir(pedido)

    @staticmethod
    def pedido_atualizar(pedido):
        PedidoDAO.atualizar(pedido)

    @staticmethod
    def pedido_excluir(id_pedido):
        PedidoDAO.excluir(id_pedido)

    @staticmethod
    def pedido_por_mesa(id_mesa):
        for p in PedidoDAO.listar():
            if p.get_mesa() == id_mesa and p.get_status() != "PAGO":
                return p
        return None

    @staticmethod
    def pedido_atualizar_status(id_pedido, status):
        for p in PedidoDAO.listar():
            if p.get_id() == id_pedido:
                p.atualizarStatus(status)
                PedidoDAO.atualizar(p)
                return

    @staticmethod
    def pedido_registrar_pagamento(id_pedido):
        for p in PedidoDAO.listar():
            if p.get_id() == id_pedido:
                p.atualizarStatus("PAGO")
                PedidoDAO.atualizar(p)
                View.mesa_liberar(p.get_mesa())
                return

    # ===== ITEM PEDIDO =====
    @staticmethod
    def item_pedido_listar(id_pedido):
        return ItemPedidoDAO.listar_por_pedido(id_pedido)

    @staticmethod
    def item_pedido_inserir(item_pedido):
        ItemPedidoDAO.inserir(item_pedido)

    @staticmethod
    def item_pedido_atualizar(item_pedido):
        ItemPedidoDAO.atualizar(item_pedido)

    @staticmethod
    def item_pedido_excluir(id_item):
        ItemPedidoDAO.excluir(id_item)

    # ===== DIA =====
    @staticmethod
    def dia_listar():
        return DiaDAO.listar()

    @staticmethod
    def dia_inserir(dia):
        DiaDAO.inserir(dia)

    @staticmethod
    def dia_atualizar(dia):
        DiaDAO.atualizar(dia)

    @staticmethod
    def dia_excluir(id_dia):
        DiaDAO.excluir(id_dia)

    @staticmethod
    def dia_aberto():
        return DiaDAO.dia_aberto()

    @staticmethod
    def pedidos_do_dia():
        dia = DiaDAO.dia_aberto()
        if not dia:
            return []
        return PedidoDAO.listar_por_dia(dia.get_id())
