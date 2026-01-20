import streamlit as st
import pandas as pd
from view import View

class PedidosMesaUI:

    @staticmethod
    def main():
        st.header("Pedidos por Mesa")

        mesas = View.mesa_listar()
        if not mesas:
            st.write("Nenhuma mesa cadastrada")
            return

        mesa = st.selectbox(
            "Mesa",
            mesas,
            format_func=lambda m: f"Mesa {m.get_id()}",
            key="mesa_pedidos"
        )

        pedidos = View.pedido_listar()
        pedidos_mesa = [p for p in pedidos if p.get_mesa() == mesa.get_id()]

        if not pedidos_mesa:
            st.write("Nenhum pedido pendente para esta mesa")
            return

        for p in pedidos_mesa:
            st.subheader(f"Pedido {p.get_id()}")
            st.write(f"Status: {p.get_status()}")
            st.write(f"Data/Hora: {p.get_dataHora()}")

            itens = View.item_pedido_listar(p.get_id())
            total = 0
            dados = []

            for i in itens:
                subtotal = i.get_quantidade() * i.get_prato().get_preco()
                total += subtotal
                dados.append({
                    "Prato": i.get_prato().get_nome(),
                    "Qtd": i.get_quantidade(),
                    "Subtotal": f"R$ {subtotal:.2f}"
                })

            st.dataframe(pd.DataFrame(dados), hide_index=True)
            st.write(f"Total: R$ {total:.2f}")

            if p.get_status() == "CONCLUÍDO":
                if st.button(
                    f"Registrar Pagamento {p.get_id()}",
                    key=f"pagar_{p.get_id()}"
                ):
                    View.pedido_registrar_pagamento(p.get_id())
                    st.success("Pagamento registrado. Mesa liberada.")
                    st.rerun()
