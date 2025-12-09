import streamlit as st
import time
import pandas as pd
from views import View

class ManterMesaUI:
    def main():
        st.header("Gerenciar Mesas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Ocupar/Liberar"])
        with tab1: ManterMesaUI.listar()
        with tab2: ManterMesaUI.inserir()
        with tab3: ManterMesaUI.atualizar()
        with tab4: ManterMesaUI.ocupar_liberar()

    def listar():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return
        rows = [m.to_json() if hasattr(m,"to_json") else m for m in mesas]
        st.dataframe(pd.DataFrame(rows), hide_index=True)

    def inserir():
        numero = st.number_input("Número da mesa", min_value=1, step=1)
        if st.button("Inserir"):
            View.mesa_inserir(numero)
            st.success("Mesa inserida")
            time.sleep(1)
            st.rerun()

    def atualizar():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return
        op = st.selectbox("Selecione mesa", mesas)
        novo_num = st.number_input("Novo número", value=op.get_numero() if hasattr(op,"get_numero") else op["numero"], min_value=1, step=1)
        if st.button("Atualizar"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.mesa_atualizar(id_, novo_num)
            st.success("Mesa atualizada")
            time.sleep(1)
            st.rerun()

    def ocupar_liberar():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return
        op = st.selectbox("Selecione mesa", mesas)
        status = op.get_status() if hasattr(op,"get_status") else op.get("status")
        st.write(f"Status atual: {status}")
        if st.button("Ocupar"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.mesa_ocupar(id_)
            st.success("Mesa ocupada")
            time.sleep(1)
            st.rerun()
        if st.button("Liberar"):
            id_ = op.get_id() if hasattr(op,"get_id") else op["id"]
            View.mesa_liberar(id_)
            st.success("Mesa liberada")
            time.sleep(1)
            st.rerun()
