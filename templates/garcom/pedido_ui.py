import streamlit as st
import pandas as pd
import time
from view import View

class PedidoUI:

    def main():
        st.header("Pedidos")
        tab1, tab2, tab3, tab4 = st.tabs(["Criar Pedido", "Adicionar Item", "Remover Item", "Listar Pedidos"])
        with tab1: PedidoUI.criar_pedido()
        with tab2: PedidoUI.adicionar_item()
        with tab3: PedidoUI.remover_item()
        with tab4: PedidoUI.listar_pedidos()

    # ===== Criar Pedido =====
    def criar_pedido():
        mesas_ocupadas = [m for m in View.mesa_listar() if m.get_status() == "OCUPADA"]
        mesas_sem_pedido = [m for m in mesas_ocupadas if not View.pedido_por_mesa(m.get_id())]

        if not mesas_sem_pedido:
            st.warning("Nenhuma mesa ocupada disponível para criar pedido.")
            return

        mesa = st.selectbox(
            "Mesa",
            mesas_sem_pedido,
            format_func=lambda m: f"Mesa {m.get_id()}",
            key="mesa_criar_pedido"
        )

        if st.button("Criar Pedido", key="btn_criar_pedido"):
            View.pedido_criar(mesa.get_id(), st.session_state["usuario_id"])
            st.success("Pedido criado")
            time.sleep(1)
            st.rerun()

    # ===== Adicionar Item =====
    def adicionar_item():
        pedidos = View.pedido_listar()
        pratos = View.prato_listar()

        if not pedidos or not pratos:
            st.warning("Nenhum pedido ou prato disponível.")
            return

        pedido = st.selectbox(
            "Pedido",
            pedidos,
            format_func=lambda p: f"Pedido {p.get_id()} (Mesa {p.get_mesa()})",
            key="pedido_adicionar_item"
        )
        prato = st.selectbox(
            "Prato",
            pratos,
            format_func=lambda p: p.get_nome(),
            key="prato_adicionar_item"
        )
        qtd = st.number_input("Quantidade", min_value=1, step=1, key="qtd_adicionar_item")

        if st.button("Adicionar", key="btn_adicionar_item"):
            View.item_pedido_inserir(pedido, prato, qtd)
            st.success("Item adicionado")
            time.sleep(1)
            st.rerun()

        if st.button("Enviar para Cozinha", key="btn_enviar_cozinha"):
            View.pedido_atualizar_status(pedido, "ENVIADO")
            st.success("Pedido enviado")

    # ===== Remover Item =====
    def remover_item():
        pedidos = View.pedido_listar()
        if not pedidos:
            st.warning("Nenhum pedido disponível.")
            return

        pedido = st.selectbox(
            "Pedido",
            pedidos,
            format_func=lambda p: f"Pedido {p.get_id()} (Mesa {p.get_mesa()})",
            key="pedido_remover_item"
        )
        itens = View.item_pedido_listar(pedido.get_id())

        if not itens:
            st.write("Nenhum item neste pedido.")
            return

        dados = []
        for i in itens:
            dados.append({
                "ID": i.get_id(),
                "Prato": i.get_prato().get_nome(),
                "Qtd": i.get_quantidade(),
                "Subtotal": f"R$ {i.get_quantidade() * i.get_prato().get_preco():.2f}"
            })
        st.dataframe(pd.DataFrame(dados), hide_index=True)

        id_item = st.selectbox("Item", [i.get_id() for i in itens], key="item_remover")
        if st.button("Remover Item", key="btn_remover_item"):
            View.item_pedido_excluir(id_item)
            st.success("Item removido")
            time.sleep(1)
            st.rerun()

    # ===== Listar Pedidos =====
    def listar_pedidos():
        pedidos = View.pedido_listar()
        if not pedidos:
            st.write("Nenhum pedido cadastrado.")
            return

        for p in pedidos:
            st.subheader(f"Pedido {p.get_id()} - Mesa {p.get_mesa()} - Status: {p.get_status()}")
            itens = View.item_pedido_listar(p.get_id())
            if not itens:
                st.write("Nenhum item neste pedido.")
                continue

            dados = []
            total = 0
            for i in itens:
                subtotal = i.get_quantidade() * i.get_prato().get_preco()
                total += subtotal
                dados.append({
                    "ID Item": i.get_id(),
                    "Prato": i.get_prato().get_nome(),
                    "Quantidade": i.get_quantidade(),
                    "Subtotal": f"R$ {subtotal:.2f}"
                })
            st.dataframe(pd.DataFrame(dados), hide_index=True)
            st.write(f"**Total do pedido: R$ {total:.2f}**")
