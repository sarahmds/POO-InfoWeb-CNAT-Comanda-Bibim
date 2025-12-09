import streamlit as st
import pandas as pd
from views import View

class RelatorioUI:
    def main():
        st.header("Relatório do Dia")
        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] != "gerente":
            st.warning("Apenas gerente pode ver o relatório")
            return

        resumo = View.relatorio_do_dia() 
        if not resumo:
            st.write("Nenhum dado para hoje")
            return

        st.subheader("Vendas Totais")
        st.write(f"Total: R$ {resumo.get('vendas_totais',0):.2f}")
        st.subheader("Pedidos")
        st.dataframe(pd.DataFrame([p.to_json() if hasattr(p,"to_json") else p for p in resumo.get("pedidos",[])]), hide_index=True)
        st.subheader("Itens vendidos")
        st.dataframe(pd.DataFrame(resumo.get("itens_vendidos",[])), hide_index=True)
