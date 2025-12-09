import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            u = View.usuario_autenticar(email, senha) 
            if u is not None:
                st.session_state["usuario_tipo"] = u["perfil"]
                st.session_state["usuario_id"] = u["id"]
                st.session_state["usuario_nome"] = u["nome"]
                st.success(f"Bem-vindo(a), {u['nome']} ({u['perfil']})")
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")
