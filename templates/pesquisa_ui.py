import streamlit as st
import pandas as pd
from view import View

class PesquisaUI:

    def main():
        st.header("Pesquisa Geral")
        termo = st.text_input("Buscar")

        if termo == "":
            return

        resultado = []

        for m in View.mesa_listar():
            if termo.lower() in str(m.get_numero()):
                resultado.append({"Tipo": "Mesa", "Valor": m.get_numero()})

        for p in View.prato_listar():
            if termo.lower() in p.get_nome().lower():
                resultado.append({"Tipo": "Prato", "Valor": p.get_nome()})

        for ped in View.pedido_listar():
            if termo in str(ped.get_id()):
                resultado.append({"Tipo": "Pedido", "Valor": ped.get_id()})

        if len(resultado) == 0:
            st.write("Nenhum resultado encontrado")
        else:
            st.dataframe(pd.DataFrame(resultado), hide_index=True)
