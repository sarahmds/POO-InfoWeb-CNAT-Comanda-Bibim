from models.usuario import Usuario
from models.mesa import Mesa
from models.prato import Prato
from models.pedido import Pedido
from models.itempedido import ItemPedido

from dao_sql.usuariodao import UsuarioDAO
from dao_sql.mesadao import MesaDAO
from dao_sql.pratodao import PratoDAO
from dao_sql.pedidodao import PedidoDAO
from dao_sql.itempedidodao import ItemPedidoDAO

from datetime import datetime


class View:

    #  USUÁRIO 

    def usuario_criar_admin():
        for u in View.usuario_listar():
            if u.get_email() == "admin":
                return
        View.usuario_inserir("Administrador", "admin", "0000-0000", "admin")

    def usuario_autenticar(email, senha):
        for u in View.usuario_listar():
            if u.get_email() == email and u.get_senha() == senha:
                return {"id": u.get_id(), "nome": u.get_nome(), "perfil": "usuario"}
        return None

    def usuario_inserir(nome, email, fone, senha):
        usuario = Usuario(0, nome, email, fone, senha)
        UsuarioDAO.inserir(usuario)

    def usuario_listar():
        lista = UsuarioDAO.listar()
        lista.sort(key=lambda u: u.get_nome())
        return lista

    def usuario_listar_id(id):
        return UsuarioDAO.listar_id(id)

    def usuario_atualizar(id, nome, email, fone, senha):
        usuario = Usuario(id, nome, email, fone, senha)
        UsuarioDAO.atualizar(usuario)

    def usuario_excluir(id):
        usuario = Usuario(id, "", "", "", "")
        UsuarioDAO.excluir(usuario)

    #  PRATO (CARDÁPIO) 

    def prato_inserir(nome, categoria, preco):
        p = Prato(0, nome, categoria, preco)
        PratoDAO.inserir(p)

    def prato_listar():
        lista = PratoDAO.listar()
        lista.sort(key=lambda p: p.get_nome())
        return lista

    def prato_listar_id(id):
        return PratoDAO.listar_id(id)

    def prato_atualizar(id, nome, categoria, preco):
        p = Prato(id, nome, categoria, preco)
        PratoDAO.atualizar(p)

    def prato_excluir(id):
        p = Prato(id, "", "", 0)
        PratoDAO.excluir(p)

    #  MESA 

    def mesa_inserir(numero, lugares, situacao):
        m = Mesa(0, numero, lugares, situacao)
        MesaDAO.inserir(m)

    def mesa_listar():
        lista = MesaDAO.listar()
        lista.sort(key=lambda m: m.get_numero())
        return lista

    def mesa_listar_id(id):
        return MesaDAO.listar_id(id)

    def mesa_atualizar(id, numero, lugares, situacao):
        m = Mesa(id, numero, lugares, situacao)
        MesaDAO.atualizar(m)

    def mesa_excluir(id):
        m = Mesa(id, 0, 0, "")
        MesaDAO.excluir(m)

    #  PEDIDO 

    def pedido_inserir(id_usuario, id_mesa):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        total = 0
        estado = "aberto"

        p = Pedido(0, data, total, estado, id_usuario, id_mesa)
        PedidoDAO.inserir(p)

    def pedido_listar():
        lista = PedidoDAO.listar()
        lista.sort(key=lambda p: p.get_id())
        return lista

    def pedido_listar_id(id):
        return PedidoDAO.listar_id(id)

    def pedido_atualizar_estado(id, novo_estado):
        pedido = PedidoDAO.listar_id(id)
        if pedido:
            pedido.set_estado(novo_estado)
            PedidoDAO.atualizar(pedido)

    # ITEM DO PEDIDO

    def item_inserir(id_pedido, id_prato, qtd):
        prato = PratoDAO.listar_id(id_prato)
        subtotal = prato.get_preco() * qtd

        i = ItemPedido(0, id_pedido, id_prato, qtd, subtotal)
        ItemPedidoDAO.inserir(i)

        pedido = PedidoDAO.listar_id(id_pedido)
        pedido.set_total(pedido.get_total() + subtotal)
        PedidoDAO.atualizar(pedido)

    def item_listar_pedido(id_pedido):
        return ItemPedidoDAO.listar_por_pedido(id_pedido)

    def item_excluir(id_item):
        item = ItemPedidoDAO.listar_id(id_item)
        if item:
            pedido = PedidoDAO.listar_id(item.get_id_pedido())
            pedido.set_total(pedido.get_total() - item.get_subtotal())
            PedidoDAO.atualizar(pedido)
            ItemPedidoDAO.excluir(item)
