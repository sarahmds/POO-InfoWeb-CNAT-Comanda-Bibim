# POO-InfoWeb-CNAT-Comanda-Bibim
Repositório referente ao trabalho de poo 4-Bimestre




 Visão geral do sistema (Restaurante / Mesas / Pedidos)
 Perfis de Usuário

Gerente

Garçom

Chef de Cozinha

 Entidades do Model
1. Usuário

Atributos:

id

nome

login

senha

perfil (gerente / garçom / chef)

2. Mesa

Atributos:

id

número

capacidade (opcional)

status (livre / ocupada)

Relacionamento:

Uma mesa → vários pedidos (1:N)

3. Prato

Atributos:

id

nome

preço

categoria (entrada, prato principal, sobremesa...)

descrição (opcional)

4. Pedido

Atributos:

id

mesa_id (FK)

garcom_id (FK)

status (aberto / enviado à cozinha / pronto)

Relacionamento:

Um pedido → vários itens de pedido (1:N)

5. ItemPedido

Atributos:

id

pedido_id (FK)

prato_id (FK)

quantidade

🔗 Associações (como o professor exige)

Mesa 1 → N Pedido

Pedido 1 → N ItemPedido

Prato 1 → N ItemPedido

Ou seja: tem várias relações 1:N, como exigido no projeto.

Operações por perfil (View)
Gerente

Registrar mesas (CRUD)

Registrar pratos do cardápio (CRUD)

Buscar mesa / prato por nome parcial

Gerar gráfico (ex: pratos mais pedidos, mesas mais usadas)

Chef de Cozinha

Ver lista de pedidos enviados para cozinha

Alterar status: “em preparo” → “pronto”

Listar pedidos por status

 Garçom

Registrar mesa ocupada / liberar mesa

Criar pedido associado a mesa

Adicionar itens (pratos) ao pedido

Enviar pedido para cozinha

Listar pedidos em aberto daquela mesa

 Interface (Streamlit)

Menu lateral exibido conforme o perfil:

Gerente:

Cadastrar Mesas

Cadastrar Pratos

Visualizar Cardápio

Relatórios (gráficos)

Garçom:

Ocupação de Mesas

Criar Pedido

Adicionar Prato ao Pedido

Enviar pedido à cozinha

Chef:

Lista de Pedidos Pendentes

Atualizar Status do Pedido

 DAO – Persistência (Sqlite)

Cada entidade terá:

inserir

listar

listar_id

atualizar

excluir

Com chaves estrangeiras:

pedido.mesa_id

pedido.garcom_id

itempedido.pedido_id

itempedido.prato_id

 Operação com Gráfico (requisito obrigatório)

Sugestões:

Quantidade de pedidos por mesa

Pratos mais pedidos

Faturamento por prato

Pedidos por garçom

O gráfico mais simples é o de barras usando st.bar_chart.
