import streamlit as st
import pandas as pd
from view import View

class PedidosMesaUI:

    def main():
        st.header("Pedidos por Mesa")

        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return

        mesa = st.selectbox("Mesa", mesas)
        pedidos = View.pedido_listar()

        pedidos_mesa = [p for p in pedidos if p.get_mesa() == mesa.get_id()]

        if len(pedidos_mesa) == 0:
            st.write("Nenhum pedido para esta mesa")
            return

        dados = []
        for p in pedidos_mesa:
            dados.append({
                "Pedido": p.get_id(),
                "Status": p.get_status(),
                "Data/Hora": p.get_dataHora()
            })

        st.dataframe(pd.DataFrame(dados), hide_index=True)
