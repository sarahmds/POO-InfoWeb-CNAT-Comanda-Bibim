import streamlit as st
import time
from views import View

class GerenciarDiaUI:
    def main():
        st.header("Gerenciar Dia")
        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] != "gerente":
            st.warning("Apenas gerente pode abrir/fechar o dia.")
            return
        status = View.gerenciar_dia_status()  
        st.write(f"Status atual do dia: **{status}**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Abrir dia"):
                View.gerenciar_dia_abrir()
                st.success("Dia aberto")
                time.sleep(1)
                st.rerun()
        with col2:
            if st.button("Fechar dia"):
                View.gerenciar_dia_fechar()
                st.success("Dia fechado")
                time.sleep(1)
                st.rerun()
