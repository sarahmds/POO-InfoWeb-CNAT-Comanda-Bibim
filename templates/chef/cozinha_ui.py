import streamlit as st
from view import View

class CozinhaUI:

    @staticmethod
    def main():
        st.header("Pedidos na Cozinha")

        pedidos = View.pedido_listar()
        pedidos_cozinha = [p for p in pedidos if p.get_status() in ["ENVIADO", "EM PREPARO", "PRONTO"]]

        if not pedidos_cozinha:
            st.write("Nenhum pedido na cozinha")
            return

        for p in pedidos_cozinha:
            st.subheader(f"Mesa {p.get_mesa()} - Pedido {p.get_id()} - Status: {p.get_status()}")

            itens = View.item_pedido_listar(p.get_id())
            if not itens:
                st.write("Pedido sem itens.")
                continue

            # Controle de preparo por unidade
            todas_unidades_prontas = True

            for i in itens:
                st.markdown(f"**{i.get_prato().get_nome()}**")

                for u in range(i.get_quantidade()):
                    key = f"pedido_{p.get_id()}_item_{i.get_id()}_u_{u}"

                    if key not in st.session_state:
                        st.session_state[key] = False

                    pronto = st.checkbox(f"Unidade {u + 1}", key=key)
                    if not pronto:
                        todas_unidades_prontas = False

            # Botão para marcar pedido como PRONTO
            if p.get_status() in ["ENVIADO", "EM PREPARO"]:
                if todas_unidades_prontas:
                    if st.button(f"Marcar Pedido {p.get_id()} como PRONTO", key=f"pronto_{p.get_id()}"):
                        View.pedido_atualizar_status(p.get_id(), "PRONTO")
                        st.success("Pedido marcado como PRONTO")
                        st.rerun()
                else:
                    st.warning("Ainda há unidades não preparadas.")

            # Botão para enviar pedido preparado
            if p.get_status() == "PRONTO":
                if st.button(f"Enviar Pedido {p.get_id()} Preparado", key=f"enviar_{p.get_id()}"):
                    View.pedido_atualizar_status(p.get_id(), "CONCLUÍDO")
                    st.success("Pedido enviado como CONCLUÍDO")
                    st.rerun()
