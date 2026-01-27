import streamlit as st
import pandas as pd
import plotly.express as px
from view import View

class RelatorioDiaUI:

    @staticmethod
    def main():
        st.header("Relatório do Dia")

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
                    "Total (R$)": f"{total_pedido:.2f}"
                })

            # Tabela de pedidos do dia
            st.dataframe(pd.DataFrame(dados), use_container_width=True)
            st.markdown(f"**Lucro do dia: R$ {total_dia:.2f}**")

            # Tabela de pratos mais vendidos
            st.subheader("Pratos mais vendidos")
            df_pratos = pd.DataFrame(
                sorted(pratos.items(), key=lambda x: x[1], reverse=True),
                columns=["Prato", "Quantidade"]
            )
            st.dataframe(df_pratos, use_container_width=True)

        # ===== Gráfico de Lucro Diário em Pizza =====
        st.divider()
        st.subheader("Lucro total por dia")

        dados_grafico = View.lucro_por_dia()
        if not dados_grafico:
            st.write("Nenhum dado para o gráfico.")
        else:
            df = pd.DataFrame(dados_grafico)
            df["data"] = pd.to_datetime(df["data"])
            df = df.sort_values("data")

            # Gráfico de pizza com cada dia como fatia
            fig = px.pie(
                df,
                values="lucro",
                names=df["data"].dt.strftime("%d/%m/%Y"),  # cada dia como fatia
                hover_data=["lucro"],
                title="Lucro diário",
            )

            # Ajustes visuais
            fig.update_traces(
                textinfo="percent+label",  # mostra percentual e o dia
                hovertemplate="Dia: %{label}<br>Lucro: R$ %{value:.2f}<extra></extra>"
            )
            fig.update_layout(showlegend=True)

            st.plotly_chart(fig, use_container_width=True)
