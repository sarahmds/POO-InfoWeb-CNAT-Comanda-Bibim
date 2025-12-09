import streamlit as st
import time
import pandas as pd
from views import View

class ManterCardapioUI:
    def main():
        st.header("Gerenciar Cardápio (Pratos)")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCardapioUI.listar()
        with tab2: ManterCardapioUI.inserir()
        with tab3: ManterCardapioUI.atualizar()
        with tab4: ManterCardapioUI.excluir()

    def listar():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
            return
        rows = [p.to_json() if hasattr(p,"to_json") else p for p in pratos]
        st.dataframe(pd.DataFrame(rows), hide_index=True)

    def inserir():
        nome = st.text_input("Nome do prato")
        desc = st.text_area("Descrição")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        if st.button("Inserir"):
            View.prato_inserir(nome, desc, preco)
            st.success("Prato inserido")
            time.sleep(1)
            st.rerun()

    def atualizar():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
            return
        op = st.selectbox("Selecione prato", pratos)
        nome = st.text_input("Nome", op.get_nome() if hasattr(op,"get_nome") else op["nome"])
        desc = st.text_area("Descrição", op.get_descricao() if hasattr(op,"get_descricao") else op.get("descricao",""))
        preco = st.number_input("Preço", value=(op.get_preco() if hasattr(op,"get_preco") else op.get("preco",0.0)), format="%.2f")
        if st.button("Atualizar"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.prato_atualizar(id_, nome, desc, preco)
            st.success("Prato atualizado")
            time.sleep(1)
            st.rerun()

    def excluir():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
            return
        op = st.selectbox("Selecione prato para excluir", pratos)
        if st.button("Excluir"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.prato_excluir(id_)
            st.success("Prato excluído")
            time.sleep(1)
            st.rerun()
