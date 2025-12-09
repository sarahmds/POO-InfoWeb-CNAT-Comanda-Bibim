import streamlit as st

from dao_sql.database import Database, criar_gerente_padrao

from templates.loginUI import LoginUI
from templates.cadastroUsuarioUI import CadastroUsuarioUI
from templates.manterMesaUI import ManterMesaUI
from templates.manterCardapioUI import ManterCardapioUI
from templates.pedidosUI import PedidosUI
from templates.cozinhaUI import CozinhaUI
from templates.pesquisaUI import PesquisaUI
from templates.gerenciarDiaUI import GerenciarDiaUI
from templates.relatorioUI import RelatorioUI
from views import View

Database.abrir()
Database.criar_tabelas()
criar_gerente_padrao()


class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar"])
        if op == "Entrar":
            LoginUI.main()

    def menu_gerente():
        op = st.sidebar.selectbox("Menu", [
            "Gerenciar Usuários",
            "Gerenciar Mesas",
            "Gerenciar Cardápio",
            "Pedidos (Garçom)",
            "Cozinha (Chef)",
            "Pesquisa Geral",
            "Gerenciar Dia",
            "Relatório do Dia"
        ])

        if op == "Gerenciar Usuários": CadastroUsuarioUI.main()
        if op == "Gerenciar Mesas": ManterMesaUI.main()
        if op == "Gerenciar Cardápio": ManterCardapioUI.main()
        if op == "Pedidos (Garçom)": PedidosUI.main()
        if op == "Cozinha (Chef)": CozinhaUI.main()
        if op == "Pesquisa Geral": PesquisaUI.main()
        if op == "Gerenciar Dia": GerenciarDiaUI.main()
        if op == "Relatório do Dia": RelatorioUI.main()

    def menu_garcom():
        op = st.sidebar.selectbox("Menu", ["Pedidos"])
        if op == "Pedidos":
            PedidosUI.main()

    def menu_chef():
        op = st.sidebar.selectbox("Menu", ["Cozinha"])
        if op == "Cozinha":
            CozinhaUI.main()

    def sair():
        if st.sidebar.button("Sair"):
            for k in ["usuario_id", "usuario_tipo", "usuario_nome"]:
                st.session_state.pop(k, None)
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()

        else:
            nome = st.session_state.get("usuario_nome", "")
            tipo = st.session_state.get("usuario_tipo", "")

            st.sidebar.write(f"Bem-vindo(a), {nome} ({tipo})")

            if tipo == "gerente":
                IndexUI.menu_gerente()
            elif tipo == "garcom":
                IndexUI.menu_garcom()
            elif tipo == "chef":
                IndexUI.menu_chef()
            else:
                st.sidebar.write("Perfil desconhecido")

            IndexUI.sair()

    def main():
        IndexUI.sidebar()


IndexUI.main()
