import streamlit as st
import pandas as pd
import time
from view import View

class PedidoUI:

    @staticmethod
    def main():
        st.header("Pedidos")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["inserir pedido", "Adicionar Item", "Remover Item", "Listar Pedidos"]
        )
        with tab1: PedidoUI.inserir_pedido()
        with tab2: PedidoUI.adicionar_item()
        with tab3: PedidoUI.remover_item()
        with tab4: PedidoUI.listar_pedidos()

    # ===== inserir Pedido =====
    @staticmethod
    def inserir_pedido():
        mesas_ocupadas = [m for m in View.mesa_listar() if m.get_status() == "OCUPADA"]
        mesas_sem_pedido = [m for m in mesas_ocupadas if not View.pedido_por_mesa(m.get_id())]

        if not mesas_sem_pedido:
            st.warning("Nenhuma mesa disponível.")
            return

        mesa = st.selectbox(
            "Mesa",
            mesas_sem_pedido,
            format_func=lambda m: f"Mesa {m.get_id()}",
            key="mesa_inserir_pedido"
        )

        if st.button("inserir pedido", key="btn_inserir_pedido"):
            View.pedido_inserir(mesa.get_id(), st.session_state["usuario_id"])
            st.success("Pedido criado")
            time.sleep(1)
            st.rerun()

    # ===== Adicionar Item =====
    @staticmethod
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
            key="pedido_add_item"
        )

        prato = st.selectbox(
            "Prato",
            pratos,
            format_func=lambda p: p.get_nome(),
            key="prato_add_item"
        )

        qtd = st.number_input(
            "Quantidade",
            min_value=1,
            step=1,
            key="qtd_add_item"
        )

        if st.button("Adicionar item", key="btn_add_item"):
            View.item_pedido_inserir(pedido, prato, qtd)
            st.success("Item adicionado")
            time.sleep(1)
            st.rerun()

    # ===== Remover Item =====
    @staticmethod
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

        df = pd.DataFrame([{
            "ID": i.get_id(),
            "Prato": i.get_prato().get_nome(),
            "Quantidade": i.get_quantidade()
        } for i in itens])

        st.dataframe(df, hide_index=True)

        item = st.selectbox(
            "Item",
            itens,
            format_func=lambda i: f"{i.get_prato().get_nome()} ( {i.get_quantidade()})",
            key="item_unitario_remover"
        )

        if st.button("Remover 1 unidade", key="btn_remover_unit"):
            if item.get_quantidade() > 1:
                item.set_quantidade(item.get_quantidade() - 1)
                View.item_pedido_atualizar(item)
                st.success("1 unidade removida")
            else:
                View.item_pedido_excluir(item.get_id())
                st.success("Item removido")

            time.sleep(1)
            st.rerun()

    # ===== Listar / Enviar / Cancelar =====
    @staticmethod
    def listar_pedidos():
        pedidos = View.pedido_listar()
        if not pedidos:
            st.write("Nenhum pedido cadastrado.")
            return

        for p in pedidos:
            st.subheader(
                f"Pedido {p.get_id()} - Mesa {p.get_mesa()} - Status: {p.get_status()}"
            )

            itens = View.item_pedido_listar(p.get_id())
            total = 0
            dados = []

            for i in itens:
                subtotal = i.get_quantidade() * i.get_prato().get_preco()
                total += subtotal
                dados.append({
                    "Prato": i.get_prato().get_nome(),
                    "Quantidade": i.get_quantidade(),
                    "Subtotal": f"R$ {subtotal:.2f}"
                })

            if dados:
                st.dataframe(pd.DataFrame(dados), hide_index=True)
                st.write(f"**Total: R$ {total:.2f}**")
            else:
                st.write("Nenhum item neste pedido.")

            if p.get_status() == "ABERTO":
                if itens:
                    if st.button(f"Enviar Pedido {p.get_id()}", key=f"enviar_{p.get_id()}"):
                        View.pedido_atualizar_status(p.get_id(), "ENVIADO")
                        st.success("Pedido enviado para a cozinha")
                        st.rerun()
                else:
                    st.warning("Pedido sem itens não pode ser enviado.")

            if st.button(f"Cancelar Pedido {p.get_id()}", key=f"cancelar_{p.get_id()}"):
                for i in itens:
                    View.item_pedido_excluir(i.get_id())
                View.pedido_excluir(p.get_id())
                st.success("Pedido cancelado")
                time.sleep(1)
                st.rerun()
