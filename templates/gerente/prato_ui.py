import streamlit as st
import pandas as pd
import time
from view import View


class PratoUI:

    def main():
        st.header("Gerenciar Cardápio")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            PratoUI.listar()
        with tab2:
            PratoUI.inserir()
        with tab3:
            PratoUI.atualizar()
        with tab4:
            PratoUI.excluir()

    # ===== LISTAR =====
    def listar():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
        else:
            dados = []
            for p in pratos:
                dados.append({
                    "ID": p.get_id(),
                    "Nome": p.get_nome(),
                    "Descrição": p.get_descricao(),
                    "Preço": p.get_preco()
                })
            st.dataframe(pd.DataFrame(dados), hide_index=True)

    # ===== INSERIR =====
    def inserir():
        nome = st.text_input("Nome do prato")
        descricao = st.text_input("Descrição")
        preco = st.number_input("Preço", min_value=0.0, step=0.5, format="%.2f")

        if st.button("Inserir"):
            View.prato_inserir(nome, descricao, preco)
            st.success("Prato inserido com sucesso")
            time.sleep(1)
            st.rerun()

    # ===== ATUALIZAR =====
    def atualizar():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
            return

        p = st.selectbox("Prato para atualizar", pratos, format_func=lambda x: f"{x.get_nome()} (ID {x.get_id()})", key="prato_atualizar")

        nome = st.text_input("Nome do prato", p.get_nome(), key=f"nome_{p.get_id()}")
        descricao = st.text_input("Descrição", p.get_descricao(), key=f"descricao_{p.get_id()}")
        preco = st.number_input("Preço", min_value=0.0, step=0.5, value=p.get_preco(), format="%.2f", key=f"preco_{p.get_id()}")

        if st.button("Atualizar"):
            View.prato_atualizar(p.get_id(), nome, descricao, preco)
            st.success("Prato atualizado com sucesso")
            time.sleep(1)
            st.rerun()

    # ===== EXCLUIR =====
    def excluir():
        pratos = View.prato_listar()
        if len(pratos) == 0:
            st.write("Nenhum prato cadastrado")
            return

        p = st.selectbox("Prato para excluir", pratos, format_func=lambda x: f"{x.get_nome()} (ID {x.get_id()})", key="prato_excluir")

        if st.button("Excluir"):
            View.prato_excluir(p.get_id())
            st.success("Prato excluído com sucesso")
            time.sleep(1)
            st.rerun()
