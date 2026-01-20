import streamlit as st
import pandas as pd
import time
from view import View


class MesaUI:

    def main():
        st.header("Gerenciar Mesas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Liberar/Ocupar", "Excluir"])
        with tab1:
            MesaUI.listar()
        with tab2:
            MesaUI.inserir()
        with tab3:
            MesaUI.status()
        with tab4:
            MesaUI.excluir()

    # ===== LISTAR =====
    def listar():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
        else:
            dados = []
            for m in mesas:
                dados.append({
                    "ID": m.get_id(),
                    "Status": m.get_status()
                })
            st.dataframe(pd.DataFrame(dados), hide_index=True)

    # ===== INSERIR =====
    def inserir():
        quantidade = st.number_input("Quantidade de mesas para adicionar", min_value=1, step=1)

        if st.button("Inserir Mesas"):
            for _ in range(quantidade):
                View.mesa_inserir("Mesa")  # O parâmetro não será usado
            st.success(f"{quantidade} mesa(s) adicionada(s) com sucesso")
            time.sleep(1)
            st.rerun()

    # ===== LIBERAR / OCUPAR =====
    def status():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return

        # Mostrar apenas ID no selectbox
        m = st.selectbox(
            "Mesa (ID)",
            mesas,
            format_func=lambda x: f"ID {x.get_id()} - {x.get_status()}"
        )

        if m.get_status() == "LIVRE":
            if st.button("Ocupar"):
                View.mesa_ocupar(m.get_id())
                st.success(f"Mesa ID {m.get_id()} ocupada")
                time.sleep(1)
                st.rerun()
        else:
            if st.button("Liberar"):
                liberou = View.mesa_liberar(m.get_id())  # Agora retorna True/False
                if liberou:
                    st.success(f"Mesa ID {m.get_id()} liberada")
                # Se não liberou, a função já mostra o aviso dentro do View
                time.sleep(1)
                st.rerun()

    # ===== EXCLUIR =====
    def excluir():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa cadastrada")
            return

        m = st.selectbox(
            "Mesa para excluir (ID)",
            mesas,
            format_func=lambda x: f"ID {x.get_id()} - {x.get_status()}",
            key="mesa_excluir"
        )
        
        if st.button("Excluir Mesa"):
            excluiu = View.mesa_excluir(m.get_id())
            if excluiu:
                st.success(f"Mesa ID {m.get_id()} excluída com sucesso")
            time.sleep(1)
            st.rerun()
