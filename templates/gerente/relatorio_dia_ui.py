import streamlit as st
import pandas as pd
from view import View

class RelatorioDiaUI:

    def main():
        st.header("relatorio")

        dias = View.dia_listar()
        if not dias:
            st.write("Nenhum dia registrado.")
            return

        for dia in dias:
            st.subheader(f"Dia: {dia.get_data()}")

            pedidos = View.pedidos_do_dia_id(dia.get_id())
            if not pedidos:
                st.write("Nenhum pedido pago neste dia.")
                continue

            dados = []
            total_dia = 0
            pratos = {}

            for p in pedidos:
                itens = View.item_pedido_listar(p.get_id())
                total_pedido = 0

                for i in itens:
                    total_pedido += i.get_quantidade() * i.get_prato().get_preco()
                    pratos[i.get_prato().get_nome()] = pratos.get(i.get_prato().get_nome(), 0) + i.get_quantidade()

                total_dia += total_pedido

                dados.append({
                    "Pedido": p.get_id(),
                    "Mesa": p.get_mesa(),
                    "Total": f"R$ {total_pedido:.2f}"
                })

            st.dataframe(pd.DataFrame(dados), use_container_width=True)
            st.markdown(f"**Lucro do dia: R$ {total_dia:.2f}**")

            st.subheader("Pratos mais vendidos")
            st.dataframe(
                pd.DataFrame(
                    sorted(pratos.items(), key=lambda x: x[1], reverse=True),
                    columns=["Prato", "Quantidade"]
                ),
                use_container_width=True
            )
