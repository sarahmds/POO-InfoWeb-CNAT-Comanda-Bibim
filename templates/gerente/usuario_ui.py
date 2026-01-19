import streamlit as st
import pandas as pd
import time
from view import View


class UsuarioUI:

    def main():
        st.header("Cadastro de Usuários")
        # Ordem alterada: Listar primeiro
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Excluir", "Atualizar"])

        with tab1:
            UsuarioUI.listar()
        with tab2:
            UsuarioUI.cadastrar()
        with tab3:
            UsuarioUI.excluir()
        with tab4:
            UsuarioUI.atualizar()

    # ===== LISTAR =====
    def listar():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.write("Nenhum usuário cadastrado")
            return

        st.subheader("Usuários cadastrados")

        # Criando DataFrame para tabela
        data = {
            "ID": [u.get_id() for u in usuarios],
            "Nome": [u.get_nome() for u in usuarios],
            "Email": [u.get_email() for u in usuarios],
            "Perfil": [u.get_perfil() for u in usuarios]
        }
        df = pd.DataFrame(data)

        # Exibir tabela bonita
        st.dataframe(df, use_container_width=True)

    # ===== CADASTRAR =====
    def cadastrar():
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        perfil = st.selectbox(
            "Perfil",
            ["GERENTE", "GARCOM", "CHEFE"],
            key="perfil_cadastrar"
        )

        if st.button("Cadastrar"):
            try:
                View.usuario_inserir(nome, email, senha, perfil)
                st.success("Usuário cadastrado com sucesso")
                time.sleep(1)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    # ===== EXCLUIR =====
    def excluir():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.write("Nenhum usuário cadastrado")
            return

        usuario = st.selectbox(
            "Usuário",
            usuarios,
            key="usuario_excluir"
        )

        if st.button("Excluir"):
            View.usuario_excluir(usuario.get_id())
            st.success("Usuário excluído")
            time.sleep(1)
            st.rerun()

    # ===== ATUALIZAR =====
    def atualizar():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.write("Nenhum usuário cadastrado")
            return

        usuario = st.selectbox(
            "Usuário",
            usuarios,
            key="usuario_atualizar"
        )

        nome = st.text_input("Nome", usuario.get_nome(), key=f"nome_{usuario.get_id()}")
        email = st.text_input("Email", usuario.get_email(), key=f"email_{usuario.get_id()}")
        senha = st.text_input("Senha", usuario.get_senha(), type="password", key=f"senha_{usuario.get_id()}")

        perfil = st.selectbox(
            "Perfil",
            ["GERENTE", "GARCOM", "CHEFE"],
            index=["GERENTE", "GARCOM", "CHEFE"].index(usuario.get_perfil()),
            key=f"perfil_{usuario.get_id()}"
        )

        if st.button("Atualizar"):
            try:
                # Atualizar de verdade usando View
                View.usuario_atualizar(usuario.get_id(), nome, email, senha, perfil)
                st.success("Usuário atualizado")
                time.sleep(1)
                st.rerun()
            except ValueError as e:
                st.error(str(e))
