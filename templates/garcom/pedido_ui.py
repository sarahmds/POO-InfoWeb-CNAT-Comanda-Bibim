import streamlit as st
import pandas as pd
import time
from view import View


class PedidoUI:

    @staticmethod
    def main():
        st.header("Gerenciamento de Pedidos")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Criar Pedido", "Adicionar Item", "Remover Item", "Consultar Pedidos"]
        )

        with tab1:
            PedidoUI.inserir_pedido()
        with tab2:
            PedidoUI.adicionar_item()
        with tab3:
            PedidoUI.remover_item()
        with tab4:
            PedidoUI.listar_pedidos()

    # ===== Criar Pedido =====
    @staticmethod
    def inserir_pedido():
        mesas_ocupadas = [m for m in View.mesa_listar() if m.get_status() == "OCUPADA"]
        mesas_sem_pedido = [m for m in mesas_ocupadas if not View.pedido_por_mesa(m.get_id())]

        if not mesas_sem_pedido:
            st.warning("Não há mesas ocupadas sem pedido aberto.")
            return

        mesa = st.selectbox(
            "Selecione a mesa",
            mesas_sem_pedido,
            format_func=lambda m: f"Mesa {m.get_id()}",
            key="mesa_inserir_pedido"
        )

        if st.button("Criar pedido"):
            View.pedido_inserir(mesa.get_id(), st.session_state["usuario_id"])
            st.success("Pedido criado com sucesso.")
            time.sleep(1)
            st.rerun()

    # ===== Adicionar Item =====
    @staticmethod
    def adicionar_item():
        pedidos = [p for p in View.pedido_listar() if p.get_status() != "PAGO"]
        pratos = View.prato_listar()

        if not pedidos:
            st.warning("Não existem pedidos disponíveis.")
            return

        if not pratos:
            st.warning("Não existem pratos cadastrados.")
            return

        pedido = st.selectbox(
            "Selecione o pedido",
            pedidos,
            format_func=lambda p: f"Pedido {p.get_id()} (Mesa {p.get_mesa()})",
            key="pedido_add_item"
        )

        prato = st.selectbox(
            "Selecione o prato",
            pratos,
            format_func=lambda p: p.get_nome(),
            key="prato_add_item"
        )

        qtd = st.number_input(
            "Quantidade",
            min_value=1,
            step=1
        )

        if st.button("Adicionar item"):
            View.item_pedido_inserir(pedido, prato, qtd)
            st.success("Item adicionado ao pedido.")
            time.sleep(1)
            st.rerun()

    # ===== Remover Item =====
    @staticmethod
    def remover_item():
        pedidos = [p for p in View.pedido_listar() if p.get_status() != "PAGO"]

        if not pedidos:
            st.warning("Não há pedidos disponíveis.")
            return

        pedido = st.selectbox(
            "Selecione o pedido",
            pedidos,
            format_func=lambda p: f"Pedido {p.get_id()} (Mesa {p.get_mesa()})",
            key="pedido_remover_item"
        )

        itens = View.item_pedido_listar(pedido.get_id())

        if not itens:
            st.info("Este pedido não possui itens.")
            return

        df = pd.DataFrame([{
            "ID": i.get_id(),
            "Prato": i.get_prato().get_nome(),
            "Quantidade": i.get_quantidade()
        } for i in itens])

        st.dataframe(df, hide_index=True)

        item = st.selectbox(
            "Selecione o item",
            itens,
            format_func=lambda i: f"{i.get_prato().get_nome()} (Qtd: {i.get_quantidade()})"
        )

        if st.button("Remover 1 unidade"):
            if item.get_quantidade() > 1:
                item.set_quantidade(item.get_quantidade() - 1)
                View.item_pedido_atualizar(item)
                st.success("Uma unidade removida.")
            else:
                View.item_pedido_excluir(item.get_id())
                st.success("Item removido do pedido.")

            time.sleep(1)
            st.rerun()

    # ===== Consultar / Enviar / Cancelar =====
    @staticmethod
    def listar_pedidos():
        pedidos = [p for p in View.pedido_listar() if p.get_status() != "PAGO"]

        if not pedidos:
            st.info("Nenhum pedido em aberto ou enviado.")
            return

        for p in pedidos:
            st.subheader(
                f"Pedido {p.get_id()} | Mesa {p.get_mesa()} | Status: {p.get_status()}"
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
                st.markdown(f"**Total: R$ {total:.2f}**")
            else:
                st.info("Pedido sem itens.")

            # ===== Enviar Pedido =====
            if p.get_status() == "ABERTO":
                if itens:
                    if st.button(
                        f"Enviar pedido {p.get_id()} para a cozinha",
                        key=f"enviar_{p.get_id()}"
                    ):
                        View.pedido_atualizar_status(p.get_id(), "ENVIADO")
                        st.success("Pedido enviado para a cozinha.")
                        st.rerun()
                else:
                    st.warning("Não é possível enviar pedido sem itens.")

            # ===== Cancelar Pedido =====
            if p.get_status() == "ABERTO":
                if st.button(
                    f"Cancelar pedido {p.get_id()}",
                    key=f"cancelar_{p.get_id()}"
                ):
                    for i in itens:
                        View.item_pedido_excluir(i.get_id())
                    View.pedido_excluir(p.get_id())
                    st.success("Pedido cancelado com sucesso.")
                    time.sleep(1)
                    st.rerun()
