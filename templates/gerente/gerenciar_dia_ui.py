import streamlit as st
import pandas as pd
from view import View

class GerenciarDiaUI:

    def main():
        st.header("Gerenciar Dia")

        # Abrir / Fechar dia
        if not View.dia_aberto():
            if st.button("Abrir Dia"):
                View.dia_abrir()
                st.success("Dia aberto")
        else:
            st.success("Dia em andamento")
            if st.button("Fechar Dia"):
                View.dia_fechar()
                st.success("Dia fechado")

            # Mostrar histórico do dia
            st.subheader("Histórico de Pedidos do Dia")
            pedidos = View.pedidos_do_dia()
            if not pedidos:
                st.write("Nenhum pedido registrado hoje")
            else:
                # Montar tabela de pedidos
                dados = []
                total_lucro = 0
                pratos_quantidade = {}

                for p in pedidos:
                    itens = View.item_pedido_listar(p.get_id())
                    total_pedido = sum(i.get_quantidade() * i.get_prato().get_preco() for i in itens)
                    total_lucro += total_pedido

                    for i in itens:
                        nome_prato = i.get_prato().get_nome()
                        pratos_quantidade[nome_prato] = pratos_quantidade.get(nome_prato, 0) + i.get_quantidade()

                    dados.append({
                        "ID Pedido": p.get_id(),
                        "Mesa": p.get_mesa(),
                        "Garçom": p.get_garcom(),
                        "Itens": ", ".join([f"{i.get_prato().get_nome()} x{i.get_quantidade()}" for i in itens]),
                        "Total": f"R$ {total_pedido:.2f}"
                    })

                st.dataframe(pd.DataFrame(dados), use_container_width=True)

                st.subheader(f"Lucro total do dia: R$ {total_lucro:.2f}")

                # Pratos mais vendidos
                st.subheader("Pratos mais vendidos")
                if pratos_quantidade:
                    df_pratos = pd.DataFrame(
                        sorted(pratos_quantidade.items(), key=lambda x: x[1], reverse=True),
                        columns=["Prato", "Quantidade"]
                    )
                    st.dataframe(df_pratos, use_container_width=True)
