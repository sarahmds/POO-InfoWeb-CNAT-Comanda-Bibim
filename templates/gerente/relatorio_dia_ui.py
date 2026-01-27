import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from view import View

class RelatorioUI:

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

        # ===== Gráfico de Lucro Diário =====
        st.divider()
        st.subheader("Lucro total por dia")

        dados_grafico = View.lucro_por_dia()
        if not dados_grafico:
            st.write("Nenhum dado para o gráfico.")
            return

        df = pd.DataFrame(dados_grafico)
        df["data"] = pd.to_datetime(df["data"])
        df = df.sort_values("data")

        fig, ax = plt.subplots()
        ax.plot(df["data"], df["lucro"], drawstyle="steps-post", marker="o")
        ax.set_xlabel("Dia")
        ax.set_ylabel("Lucro (R$)")
        ax.set_title("Lucro diário")
        st.pyplot(fig)
