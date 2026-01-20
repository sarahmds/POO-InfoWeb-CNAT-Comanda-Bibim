import streamlit as st
import time
from view import View

class CozinhaUI:

    @staticmethod
    def main():
        st.header("Pedidos na Cozinha")
        pedidos = View.pedido_listar()

        # Filtra apenas pedidos enviados ou em preparo
        pedidos_cozinha = [
            p for p in pedidos if p.get_status() in ["ENVIADO", "EM PREPARO"]
        ]

        if not pedidos_cozinha:
            st.write("Nenhum pedido na cozinha")
            return

        st.write("### Itens dos Pedidos")

        pedidos_prontos = True  # Flag para verificar se todos os pedidos já estão prontos

        for p in pedidos_cozinha:
            st.subheader(f"Mesa {p.get_mesa()} - Status: {p.get_status()}")
            itens = View.item_pedido_listar(p.get_id())

            # Agrupa pratos por nome somando as quantidades
            pratos_agrupados = {}
            for i in itens:
                nome = i.get_prato().get_nome()
                if nome in pratos_agrupados:
                    pratos_agrupados[nome] += i.get_quantidade()
                else:
                    pratos_agrupados[nome] = i.get_quantidade()

            todos_prontos = True  # Flag para este pedido
            for prato, qtd_total in pratos_agrupados.items():
                st.write(f"**{prato}** - Quantidade: {qtd_total}")
                for unidade in range(qtd_total):
                    key_checkbox = f"{p.get_id()}_{prato}_{unidade}"
                    if key_checkbox not in st.session_state:
                        st.session_state[key_checkbox] = False

                    checked = st.checkbox(f"Unidade {unidade+1}", key=key_checkbox)
                    if not checked:
                        todos_prontos = False  # ainda há unidades não prontas

            # Atualiza status do pedido automaticamente
            if todos_prontos and p.get_status() != "PRONTO":
                # Contagem regressiva para simular "preparando"
                for i in range(3, 0, -1):
                    st.write(f"Atualizando status de Pedido {p.get_id()} para PRONTO em {i}...")
                    time.sleep(1)
                    st.experimental_rerun()
                View.pedido_atualizar_status(p.get_id(), "PRONTO")
                st.success(f"Pedido {p.get_id()} agora está PRONTO")

            if not todos_prontos:
                pedidos_prontos = False

        # Botão para enviar pedido como CONCLUÍDO
        if st.button("Enviar Pedido(s) para CONCLUÍDO"):
            if pedidos_prontos:
                for p in pedidos_cozinha:
                    if p.get_status() == "PRONTO":
                        View.pedido_atualizar_status(p.get_id(), "CONCLUÍDO")
                st.success("Todos os pedidos foram enviados como CONCLUÍDOS")
                st.rerun()
            else:
                st.warning("Ainda há pratos a serem preparados! Não é possível concluir o pedido.")
