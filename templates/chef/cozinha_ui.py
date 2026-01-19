import streamlit as st
import pandas as pd
import time
from view import View

class CozinhaUI:

    def main():
        st.header("Pedidos na Cozinha")
        pedidos = View.pedido_listar()

        pedidos_cozinha = [
            p for p in pedidos if p.get_status() in ["ENVIADO", "EM PREPARO"]
        ]

        if len(pedidos_cozinha) == 0:
            st.write("Nenhum pedido na cozinha")
            return

        dados = []
        for p in pedidos_cozinha:
            dados.append({
                "ID": p.get_id(),
                "Mesa": p.get_mesa(),
                "Status": p.get_status()
            })

        st.dataframe(pd.DataFrame(dados), hide_index=True)

        pedido = st.selectbox("Pedido", pedidos_cozinha)

        novo_status = st.selectbox(
            "Atualizar status",
            ["EM PREPARO", "PRONTO"]
        )

        if st.button("Atualizar"):
            View.pedido_atualizar_status(pedido.get_id(), novo_status)
            st.success("Status atualizado")
            st.rerun()
