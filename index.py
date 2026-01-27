import streamlit as st
from view import View

from templates.login_ui import LoginUI

from templates.gerente.usuario_ui import UsuarioUI
from templates.gerente.mesa_ui import MesaUI
from templates.gerente.prato_ui import PratoUI
from templates.gerente.gerenciar_dia_ui import GerenciarDiaUI
from templates.gerente.relatorio_dia_ui import RelatorioDiaUI

from templates.garcom.pedido_ui import PedidoUI
from templates.garcom.pedidos_mesa_ui import PedidosMesaUI

from templates.chef.cozinha_ui import CozinhaUI
from templates.pesquisa_ui import PesquisaUI


class IndexUI:

    # -------- MENUS --------

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Login"])
        if op == "Login":
            LoginUI.main()

    def menu_gerente():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Usuários",
                "Mesas",
                "Cardápio",
                "Gerenciar Dia",
                "relatorio",
                "Pesquisa"
            ]
        )
        if op == "Usuários": UsuarioUI.main()
        if op == "Mesas": MesaUI.main()
        if op == "Cardápio": PratoUI.main()
        if op == "Gerenciar Dia": GerenciarDiaUI.main()
        if op == "relatorio": RelatorioDiaUI.main()
        if op == "Pesquisa": PesquisaUI.main()

    def menu_garcom():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Consultar Mesas",
                "Gerenciar pedidos",
                "Pedidos por Mesa",
                "Pesquisa"
            ]
        )
        if op == "Consultar Mesas": MesaUI.main()
        if op == "Gerenciar pedidos": PedidoUI.main()
        if op == "Pedidos por Mesa": PedidosMesaUI.main()
        if op == "Pesquisa": PesquisaUI.main()

    def menu_chef():
        op = st.sidebar.selectbox(
            "Menu",
            ["Pedidos na Cozinha"]
        )
        if op == "Pedidos na Cozinha":
            CozinhaUI.main()

    # -------- CONTROLE --------

    def sair():
        if st.sidebar.button("Sair"):
            st.session_state.clear()
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write(
                f"Bem-vindo(a), {st.session_state['usuario_nome']}"
            )

            perfil = st.session_state["usuario_perfil"]

            if perfil == "GERENTE":
                IndexUI.menu_gerente()
            elif perfil == "GARCOM":
                IndexUI.menu_garcom()
            elif perfil == "CHEFE":
                IndexUI.menu_chef()

            IndexUI.sair()

    def main():
        View.usuario_inserir_gerente_padrao()
        IndexUI.sidebar()


#UsuarioUI.main()
IndexUI.main()

