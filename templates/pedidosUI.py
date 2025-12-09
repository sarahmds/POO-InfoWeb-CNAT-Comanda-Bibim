import streamlit as st
import time
import pandas as pd
from views import View

class PedidosUI:
    def main():
        st.header("Pedidos (Garçom)")
        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] not in ["garcom","gerente"]:
            st.warning("Apenas garçom ou gerente pode acessar esta tela.")
            return

        tab1, tab2, tab3 = st.tabs(["Criar Pedido", "Adicionar Item / Enviar", "Listar por Mesa"])
        with tab1: PedidosUI.criar_pedido()
        with tab2: PedidosUI.adicionar_item_enviar()
        with tab3: PedidosUI.listar_por_mesa()

    def criar_pedido():
        mesas = View.mesa_listar()
        if len(mesas) == 0:
            st.write("Nenhuma mesa")
            return
        mesa = st.selectbox("Selecione a mesa", mesas)
        obs = st.text_area("Observações (opcional)")
        if st.button("Criar pedido"):
            mesa_id = mesa.get_id() if hasattr(mesa,"get_id") else mesa["id"]
            garcom_id = st.session_state["usuario_id"]
            pedido = View.pedido_criar(mesa_id, garcom_id, obs)
            st.success("Pedido criado")
            st.write(pedido)
            time.sleep(1)
            st.rerun()

    def adicionar_item_enviar():
        pedidos = View.pedido_listar_abertos()  
        pratos = View.prato_listar()
        if len(pedidos) == 0:
            st.write("Nenhum pedido disponível para editar")
            return
        pedido = st.selectbox("Selecione pedido", pedidos)
        prato = st.selectbox("Selecione prato", pratos)
        qtd = st.number_input("Quantidade", min_value=1, value=1, step=1)
        if st.button("Adicionar item"):
            pedido_id = pedido.get_id() if hasattr(pedido,"get_id") else pedido["id"]
            prato_id = prato.get_id() if hasattr(prato,"get_id") else prato["id"]
            View.pedido_adicionar_item(pedido_id, prato_id, qtd)
            st.success("Item adicionado")
            time.sleep(1)
            st.rerun()
        if st.button("Enviar para cozinha"):
            pid = pedido.get_id() if hasattr(pedido,"get_id") else pedido["id"]
            View.pedido_enviar_cozinha(pid)
            st.success("Pedido enviado para cozinha")
            time.sleep(1)
            st.rerun()

    def listar_por_mesa():
        mesas = View.mesa_listar()
        mesa = st.selectbox("Selecione mesa", mesas)
        mesa_id = mesa.get_id() if hasattr(mesa,"get_id") else mesa["id"]
        pedidos = View.pedido_listar_por_mesa(mesa_id)
        if len(pedidos) == 0:
            st.write("Nenhum pedido nessa mesa")
            return
        rows = [p.to_json() if hasattr(p,"to_json") else p for p in pedidos]
        st.dataframe(pd.DataFrame(rows), hide_index=True)
