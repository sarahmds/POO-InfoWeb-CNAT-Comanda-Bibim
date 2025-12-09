import streamlit as st
import pandas as pd
from views import View

class PesquisaUI:
    def main():
        st.header("Pesquisa Geral")
        termo = st.text_input("Pesquisar (mesas / pratos / pedidos)")
        if st.button("Pesquisar"):
            resultados = View.pesquisa_geral(termo) 
            if not resultados:
                st.write("Nenhum resultado")
                return
            if "mesas" in resultados:
                st.subheader("Mesas")
                st.dataframe([m.to_json() if hasattr(m,"to_json") else m for m in resultados["mesas"]], hide_index=True)
            if "pratos" in resultados:
                st.subheader("Pratos")
                st.dataframe([p.to_json() if hasattr(p,"to_json") else p for p in resultados["pratos"]], hide_index=True)
            if "pedidos" in resultados:
                st.subheader("Pedidos")
                st.dataframe([p.to_json() if hasattr(p,"to_json") else p for p in resultados["pedidos"]], hide_index=True)
