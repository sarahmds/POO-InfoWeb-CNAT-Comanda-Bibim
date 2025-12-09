import streamlit as st
import time
import pandas as pd
from views import View

class CadastroUsuarioUI:
    def main():
        st.header("Gerenciar Usuários (Acesso: Gerente)")
        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] != "gerente":
            st.warning("Apenas gerente pode acessar esta tela.")
            return

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: CadastroUsuarioUI.listar()
        with tab2: CadastroUsuarioUI.inserir()
        with tab3: CadastroUsuarioUI.atualizar()
        with tab4: CadastroUsuarioUI.excluir()

    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
            return
        rows = [u.to_json() if hasattr(u, "to_json") else u for u in usuarios]
        df = pd.DataFrame(rows)
        st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        perfil = st.selectbox("Perfil", ["gerente", "garcom", "chef"])
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, senha, perfil)
            st.success("Usuário inserido")
            time.sleep(1)
            st.rerun()

    def atualizar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
            return
        op = st.selectbox("Escolha usuário para atualizar", usuarios)
        nome = st.text_input("Nome", op.get_nome() if hasattr(op, "get_nome") else op["nome"])
        email = st.text_input("E-mail", op.get_email() if hasattr(op, "get_email") else op["email"])
        senha = st.text_input("Senha (deixe em branco para manter)", type="password")
        perfil = st.selectbox("Perfil", ["gerente","garcom","chef"], index=["gerente","garcom","chef"].index(op.get_perfil() if hasattr(op,"get_perfil") else (op.get("perfil") if isinstance(op, dict) else "garcom")))
        if st.button("Atualizar"):
            id_ = op.get_id() if hasattr(op, "get_id") else op["id"]
            View.usuario_atualizar(id_, nome, email, senha if senha != "" else None, perfil)
            st.success("Usuário atualizado")
            time.sleep(1)
            st.rerun()

    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
            return
        op = st.selectbox("Escolha usuário para excluir", usuarios)
        if st.button("Excluir"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.usuario_excluir(id_)
            st.success("Usuário excluído")
            time.sleep(1)
            st.rerun()
