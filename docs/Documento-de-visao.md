# Documento de Visão

## Histórico de Revisões
| Data | Versão | Descrição | Autores |
| :--: | :----: | --------- | :------ |
| 27/11/25 | 1.0 | Versão inicial | Gabriel Carrilho da Silva, Sarah Medeiros dos Santos, Emilly Yasmim Batista da Conceição |

## 1. Objetivo do projeto
Sistema para gerenciar mesas, pedidos e cardápio, permitindo controle eficiente por gerente, garçom e chef.


## 2. Descrição do problema
| Item | Descrição |
|------|-----------|
| Problema | Falta de organização no controle de mesas, pedidos e preparo. |
| Afeta | Gerentes, garçons e chefs. |
| Impacta | Atrasos, erros, baixa eficiência. |
| Solução | Sistema com gerenciamento de mesas, pedidos e cardápio integrado ao SQLite. |

## 3. Usuários e Funcionalidades

### Gerente
Responsabilidades: administração geral.  
Funcionalidades:  
- Cadastro de usuários  
- gerenciar mesas  
- gerenciar pratos  
- Consulta de mesas  
- Consulta de cardápio  
- Pesquisar por (mesas/pratos/pedidos)  
- visualizar gráfico

### Garçom
Responsabilidades: atendimento ao cliente.  
Funcionalidades:  
- Consultar mesas  
- Ocupação e liberação de mesa  
- Criar pedidos vinculados à mesa  
- Adicionar itens ao pedido  
- Enviar pedido para o chef  
- Listar pedidos em aberto por mesa  

### Chef
Responsabilidades: preparo dos pratos.  
Funcionalidades:  
- Visualizar pedidos enviados  
- Atualizar status do preparo  
- Finalizar pedidos  


## 4. Ambiente dos usuários
Sistema web em Streamlit, acessado em dispositivos do restaurante.  
SQLite armazenará mesas, usuários, pratos, pedidos e itens.


## 5. Principais necessidades dos usuários
1. Consultar mesas  
2. Registrar mesas  
3. Consultar cardápio  
4. Registrar pratos  
5. Criar e gerenciar pedidos  
6. Enviar pedidos para cozinha  
7. Atualizar status de preparo  
8. Gerar relatórios com gráficos  

## 6. Alternativas concorrentes
Consumer: mesas, pedidos, cardápio e emissão fiscal.  
Colibri: controle de mesas, pedidos, PDV e relatórios.


## 7. Requisitos Funcionais
| Código | Requisito | Descrição | Prioridade | Usuário |
| :----: | -------- | --------- | :--------: | :------ |
| RF01 | Cadastro de Usuário | Registrar usuários com perfis. | Alta | Gerente |
| RF02 | Login | Autenticação com perfil. | Alta | Todos |
| RF03 | gerenciar Mesas | Criar, editar, listar, excluir mesas. | Alta | Gerente |
| RF04 | gerenciar Pratos | Criar, editar, listar, excluir pratos. | Alta | Gerente |
| RF05 | Consulta Mesas | Visualizar mesas e status. | Alta | Gerente, Garçom |
| RF06 | Ocupação de Mesa | Marcar/liberar mesa. | Alta | Garçom |
| RF07 | Criar Pedido | Pedido vinculado à mesa. | Alta | Garçom |
| RF08 | Adicionar Itens | Inserir pratos no pedido. | Alta | Garçom |
| RF09 | Envio para Cozinha | Pedido muda para “enviado”. | Alta | Garçom |
| RF10 | Pedidos da Cozinha | Visualizar pendentes. | Alta | Chef |
| RF11 | Atualizar Status | Atualizar preparo. | Alta | Chef |
| RF12 | Lista por Mesa | Ver pedidos em aberto. | Média | Garçom |
| RF13 | Pesquisa Parcial | Buscar mesas ou pratos. | Média | Gerente |
| RF14 | Relatórios | Exibir gráficos. | Média | Gerente |
| RF15 | Persistência | Registro no SQLite. | Alta | Todos |


## 8. Requisitos Não-funcionais
| Código | Nome | Descrição | Categoria | Classificação |
| :----: | ---- | --------- | --------- | :-----------: |
| RNF01 | Performance | Páginas carregam em até 2s. | Desempenho | Essencial |
| RNF02 | Usabilidade | Interface simples. | Usabilidade | Essencial |
| RNF03 | Portabilidade | Acesso via navegador. | Técnica | Importante |
| RNF04 | Persistência | Uso de SQLite. | Técnica | Essencial |
