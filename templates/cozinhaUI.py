import streamlit as st
import time
import pandas as pd
from views import View

class CozinhaUI:
    def main():
        st.header("Cozinha (Chef)")
        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] != "chef":
            st.warning("Apenas chef pode acessar esta tela.")
            return

        pedidos = View.pedido_listar_cozinha()  
        if len(pedidos) == 0:
            st.write("Nenhum pedido para preparar")
            return

        for p in pedidos:
            itens = View.itempedido_listar_por_pedido(p.get_id() if hasattr(p,"get_id") else p["id"])
            st.subheader(f"Pedido {p.get_id() if hasattr(p,'get_id') else p['id']} - Mesa {p.get_mesa() if hasattr(p,'get_mesa') else p.get('mesa')}")
            st.write("Itens:")
            df = []
            for it in itens:
                df.append(it.to_json() if hasattr(it,"to_json") else it)
            st.dataframe(df, hide_index=True)
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Marcar em preparo - {p.get_id() if hasattr(p,'get_id') else p['id']}"):
                    View.pedido_atualizar_status(p.get_id() if hasattr(p,'get_id') else p['id'], "em_preparo")
                    st.success("Status atualizado para em preparo")
                    time.sleep(0.5)
                    st.rerun()
            with col2:
                if st.button(f"Finalizar - {p.get_id() if hasattr(p,'get_id') else p['id']}"):
                    View.pedido_atualizar_status(p.get_id() if hasattr(p,'get_id') else p['id'], "concluido")
                    st.success("Pedido concluído")
                    time.sleep(0.5)
                    st.rerun()
