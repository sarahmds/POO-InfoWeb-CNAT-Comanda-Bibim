from datetime import datetime

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
    def usuario_listar():
        return UsuarioDAO.listar()

    # ===== MESA =====
    @staticmethod
    def mesa_listar():
        return MesaDAO.listar()

    @staticmethod
    def mesa_liberar(id_mesa):
        mesa = next(
            (m for m in MesaDAO.listar() if m.get_id() == id_mesa),
            None
        )
        if not mesa:
            return False

        pedidos = [
            p for p in PedidoDAO.listar()
            if p.get_mesa() == id_mesa
        ]

        if pedidos and any(p.get_status() != "PAGO" for p in pedidos):
            return False

        mesa.liberar()
        MesaDAO.atualizar(mesa)
        return True

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
        return [
            p for p in PedidoDAO.listar()
            if p.get_status() != "PAGO"
        ]

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

    @staticmethod
    def pedido_por_mesa(id_mesa):
        """
        Retorna um pedido ativo da mesa (não pago).
        Impede criar mais de um pedido por mesa.
        """
        for p in PedidoDAO.listar():
            if p.get_mesa() == id_mesa and p.get_status() != "PAGO":
                return p
        return None

    # ===== ITEM PEDIDO =====
    @staticmethod
    def item_pedido_listar(id_pedido):
        return ItemPedidoDAO.listar_por_pedido(id_pedido)

    # ===== PRATO =====
    @staticmethod
    def prato_listar():
        return PratoDAO.listar()

    # ===== DIA =====
    @staticmethod
    def listar_dias():
        return DiaDAO.listar()

    @staticmethod
    def dia_aberto():
        return DiaDAO.dia_aberto()

    @staticmethod
    def pedidos_do_dia():
        dia = DiaDAO.dia_aberto()
        if not dia:
            return []
        return PedidoDAO.listar_por_dia(dia.get_id())

    @staticmethod
    def pedidos_do_dia_id(id_dia):
        return [
            p for p in PedidoDAO.listar_por_dia(id_dia)
            if p.get_status() == "PAGO"
        ]
