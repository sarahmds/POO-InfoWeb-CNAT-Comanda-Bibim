# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :------: |
| 27/11/25 | 1.0 | Versão inicial | Gabriel Carrilho da Silva, Sarah Medeiros dos Santos, Emilly Yasmim Batista da Conceição |


## 1. Objetivo do projeto

Implementação de um sistema web para gerenciamento de mesas, pedidos e cardápio de um restaurante, permitindo controle eficiente das operações por gerente, garçom e chef. O sistema utilizará SQLite para persistência dos dados.


## 2. Descrição do problema

|    |    |
| -- | -- |
| **Problema** | Falta de organização no controle de mesas, pedidos e preparo. |
| **Afeta** | Gerentes, garçons e chefs. |
| **Impacta** | Atrasos, erros, baixa eficiência e dificuldade no acompanhamento do fluxo de trabalho. |
| **Solução** | Desenvolvimento de um sistema integrado para gerenciar mesas, pedidos, cardápio e preparo, com armazenamento em SQLite. |


## 3. Descrição dos usuários

| Nome | Descrição | Responsabilidade |
| :--: | :-------: | :--------------: |
| **Gerente** | administrador geral do sistema | cadastrar usuários, gerenciar cardápio, gerenciar mesas e visualizar relatórios |
| **Garçom** | funcionário responsável pelo atendimento | gerenciar ocupação das mesas, Gerenciar pedidoss e enviá-los à cozinha |
| **Chef** | responsável pelo preparo dos pratos | visualizar pedidos enviados, atualizar status e finalizar preparo |


## 4. Descrição do ambiente dos usuários

O sistema será acessado via navegador em dispositivos do restaurante, como computadores, tablets ou celulares.  
O banco de dados SQLite armazenará informações de mesas, usuários, pratos, pedidos e itens.


## 5. Principais necessidades dos usuários


### 1. Gerente
- Cadastro de usuários
- Login
- gerenciar dia
- Gerenciar mesas
- Gerenciar cardápio 
- Consultar mesas
- perquisar pratos
- Relatório do dia 
### 2. Garçom
- Login
- Consultar mesas  
- Ocupar e liberar mesas
- Gerenciar pedidos
- Adicionar itens ao pedido
- Enviar pedido para cozinha
- Listar pedidos por mesa
- perquisar pratos

### 3. Chef
- Login
- Listar pedidos na cozinha
-  Atualizar status do pedido

## 6. Alternativas concorrentes

1. **Consumer**
   - gerenciamento de mesas, pedidos, cardápio  
   - emissão fiscal integrada  
   - solução robusta para estabelecimentos maiores  

2. **Colibri**
   - controle de mesas e pedidos  
   - PDV integrado  
   - geração de relatórios operacionais  


## 7. Requisitos Funcionais

| Código | Nome| Descrição| Prioridade|
|-------|---------------------------|------------------------------------------------------------|------------|
| RF01  | Cadastro de usuários| Registrar usuários com perfis (gerente, garçom, chef)| alta|
| RF02  | Login| Autenticação e controle de acesso| alta|
| RF03  | Gerenciar dia| Abrir e fechar o dia no sistema| alta|
| RF04  | Gerenciar mesas| Criar, editar, listar e excluir mesas| alta|
| RF05  | Gerenciar cardápio| Criar, editar, listar e excluir pratos| alta|
| RF06  | Consultar mesas| Visualizar lista e status das mesas| alta|
| RF07  | Ocupar e liberar mesas| Alterar status da mesa (livre/ocupada)| alta|
| RF08  | Gerenciar pedidos| Registrar pedido vinculado à mesa| alta|
| RF09  | Adicionar itens ao pedido| Inserir pratos em pedido existente| alta|
| RF10  | Enviar pedido para cozinha| Alterar status do pedido para “enviado”| alta|
| RF11  | Listar pedidos na cozinha | Exibir pedidos pendentes para preparo| alta|
| RF12  | Atualizar status do pedido| Atualizar status (em preparo/concluído)| alta|
| RF13  | Listar pedidos por mesa| Exibir pedidos de uma mesa específica| média|
| RF14  | perquisar pratos| Buscar mesas, pratos ou pedidos| média|
| RF15  | Relatório do dia| Exibir gráficos de vendas| alta|


## 8. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| RNF01 | Performance | Páginas devem carregar em até 2 segundos | desempenho | essencial |
| RNF02 | Usabilidade | Interface simples e intuitiva | usabilidade | essencial |
| RNF03 | Portabilidade | Acesso via qualquer navegador | técnica | importante |
| RNF04 | Persistência | Utilização do SQLite para armazenamento | técnica | essencial |
