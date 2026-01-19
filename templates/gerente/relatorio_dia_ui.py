import streamlit as st
import pandas as pd
from view import View

class RelatorioDiaUI:

    def main():
        st.header("Relatório de Todos os Dias")

        # Obter todos os dias registrados
        dias = View.listar_dias()
        if not dias:
            st.write("Nenhum dia registrado ainda.")
            return

        for dia in dias:
            st.subheader(f"Dia: {dia.get_data()}")
            st.write(f"Aberto: {'Sim' if dia.get_aberto() else 'Não'}")

            # Pedidos do dia
            pedidos = View.pedidos_do_dia_id(dia.get_id())
            if not pedidos:
                st.write("Nenhum pedido registrado neste dia.")
                continue

            # Preparar tabela de pedidos
            dados_pedidos = []
            total_dia = 0
            pratos_quantidade = {}

            for p in pedidos:
                itens = View.item_pedido_listar(p.get_id())
                total_pedido = sum(i.get_quantidade() * i.get_prato().get_preco() for i in itens)
                total_dia += total_pedido

                for i in itens:
                    nome_prato = i.get_prato().get_nome()
                    pratos_quantidade[nome_prato] = pratos_quantidade.get(nome_prato, 0) + i.get_quantidade()

                dados_pedidos.append({
                    "ID Pedido": p.get_id(),
                    "Mesa": p.get_mesa(),
                    "Garçom": p.get_garcom(),
                    "Itens": ", ".join([f"{i.get_prato().get_nome()} x{i.get_quantidade()}" for i in itens]),
                    "Total Pedido (R$)": f"{total_pedido:.2f}"
                })

            st.subheader("Pedidos do dia")
            df_pedidos = pd.DataFrame(dados_pedidos)
            st.dataframe(df_pedidos, use_container_width=True)

            st.markdown(f"**Lucro do dia:** R$ {total_dia:.2f}")

            # Preparar ranking de pratos
            if pratos_quantidade:
                st.subheader("Pratos mais vendidos")
                df_pratos = pd.DataFrame(
                    sorted(pratos_quantidade.items(), key=lambda x: x[1], reverse=True),
                    columns=["Prato", "Quantidade"]
                )
                st.dataframe(df_pratos, use_container_width=True)
