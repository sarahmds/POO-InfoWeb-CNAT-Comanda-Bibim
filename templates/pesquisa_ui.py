import streamlit as st
import pandas as pd
from view import View

class PesquisaUI:

    def main():
        st.header("Pesquisar pratos")
        termo = st.text_input("Buscar prato")

        if termo.strip() == "":
            return

        resultado = []

        for p in View.prato_listar():
            if termo.lower() in p.get_nome().lower():
                resultado.append({
                    "Nome": p.get_nome(),
                    "Preço": p.get_preco()
                })

        if not resultado:
            st.write("Nenhum prato encontrado")
        else:
            st.dataframe(pd.DataFrame(resultado), hide_index=True)
