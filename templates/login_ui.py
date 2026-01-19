import streamlit as st
from view import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")

        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            u = View.usuario_autenticar(email, senha)

            if u is not None:
                st.session_state["usuario_id"] = u["id"]
                st.session_state["usuario_nome"] = u["nome"]
                st.session_state["usuario_perfil"] = u["perfil"]
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")
