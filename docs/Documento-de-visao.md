# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :-----: |
| 25/11/25 | 1.0 | Versão inicial | Gabriel Carrilho da Silva, Sarah Medeiros dos Santos, Emilly Yasmim Batista da Conceição |
| | | | |

## 1. Objetivo do projeto

Desenvolver um sistema para gerenciar mesas, pedidos e cardápio de um restaurante, permitindo controle eficiente das operações por gerente, garçom e chef.

## 2. Descrição do problema

|    |    |
| -- | -- |
| **Problema** | Falta de organização no controle de mesas, pedidos e preparo dos pratos. |
| **Afeta** | Gerentes, garçons e chefs responsáveis pelo atendimento e operação do restaurante. |
| **Impacta** | Gera atrasos, erros nos pedidos, dificuldades de gestão e baixa eficiência no fluxo de trabalho. |
| **Solução** | Implementar um sistema que gerencia mesas, pedidos e cardápio, com funções específicas para cada perfil e persistência em banco de dados. |

## 3. Descrição dos usuários

| Nome | Descrição | Responsabilidade |
| :--: | :-------: | :--------------: |
| **Gerente** | Usuário com maior nível de acesso, responsável pela administração geral do sistema. | Gerenciar mesas, cardápio, relatórios e manter os registros atualizados. |
| **Garçom** | Responsável pelo atendimento direto às mesas e criação dos pedidos. | Registrar ocupação, criar pedidos, adicionar itens e enviar à cozinha. |
| **Chef de Cozinha** | Usuário que recebe e prepara os pedidos enviados. | Visualizar pedidos pendentes, atualizar status e indicar quando estão prontos. |

## 4. Descrição do ambiente dos usuários

Os usuários utilizarão o sistema em um ambiente de restaurante, acessando a aplicação por meio de computadores ou dispositivos móveis conectados à rede local.  
O acesso será realizado via interface web desenvolvida em Streamlit, permitindo navegação simples e adequada ao fluxo de trabalho de cada perfil (gerente, garçom e chef).  
O banco de dados utilizado será (a adicionar...), armazenando registros de mesas, pedidos, pratos e usuários.

## 5. Principais necessidades dos usuários

1. Consultar Mesas  
2. Registrar Mesas  
3. Consultar cardápio  
4. Registrar pratos do cardápio  
5. Criar pedidos  
6. Adicionar pratos ao pedido  
7. Enviar pedidos para a cozinha  
8. Atualizar e visualizar status dos pedidos  

## 6. Alternativas concorrentes

**Consumer**  
Sistema amplamente utilizado em restaurantes no Brasil, oferecendo gerenciamento de mesas, pedidos, cardápio, delivery, estoque e emissão fiscal.

**Colibri**  
Plataforma consolidada no setor de food service, permitindo controle de mesas, pedidos, PDV, envio para cozinha, delivery e relatórios de gestão.

## 7. Regras de Negócio

| ID | Regra | Descrição |
| :-: | :--- | :--------- |
| RN01 | Cadastro de Mesas | Apenas o gerente pode criar, editar e excluir mesas. |
| RN02 | Cadastro de Pratos | Apenas o gerente pode criar, editar e excluir pratos do cardápio. |
| RN03 | Ocupação de Mesas | Apenas o garçom pode marcar mesa como ocupada ou liberar mesa. |
| RN04 | Criação de Pedido | Um pedido só pode ser criado se a mesa estiver ocupada. |
| RN05 | Itens do Pedido | Itens só podem ser adicionados a pedidos com status “aberto”. |
| RN06 | Envio para Cozinha | Somente o garçom pode enviar um pedido para a cozinha, alterando seu status para “enviado”. |
| RN07 | Preparação do Pedido | Apenas o chef pode alterar o status de “em preparo” para “pronto”. |
| RN08 | Consulta por Perfil | Cada usuário só visualiza telas e funções permitidas pelo seu perfil. |
| RN09 | Relatórios | Apenas o gerente pode acessar e gerar gráficos de desempenho. |
| RN10 | Integridade de Dados | Não é permitido excluir mesas, pratos ou pedidos que estejam vinculados a outros registros. |
| RN11 | Persistência | Todas as operações (CRUD) devem ser registradas no banco SQLite. |

## 8. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :-- | :--------- | :--------: |
| RF01 | Cadastro de Usuário | Permitir registrar usuários com perfil de gerente, garçom ou chef. | Alta |
| RF02 | Login | Permitir autenticação de usuários com validação de perfil. | Alta |
| RF03 | Cadastro de Mesas | Permitir ao gerente criar, editar, listar e excluir mesas. | Alta |
| RF04 | Cadastro de Pratos | Permitir ao gerente criar, editar, listar e excluir pratos do cardápio. | Alta |
| RF05 | Consulta de Mesas | Permitir visualizar mesas e seus status (livre/ocupada). | Alta |
| RF06 | Ocupação de Mesa | Permitir ao garçom marcar mesa como ocupada ou liberar mesa. | Alta |
| RF07 | Criar Pedido | Permitir ao garçom criar pedidos vinculados a uma mesa. | Alta |
| RF08 | Adicionar Itens ao Pedido | Permitir adicionar pratos a um pedido aberto. | Alta |
| RF09 | Enviar Pedido para Cozinha | Permitir ao garçom alterar o status do pedido para “enviado”. | Alta |
| RF10 | Listar Pedidos da Cozinha | Permitir ao chef visualizar pedidos enviados. | Alta |
| RF11 | Atualizar Status do Pedido | Permitir ao chef alterar status para “em preparo” e “pronto”. | Alta |
| RF12 | Listar Pedidos por Mesa | Permitir visualizar pedidos em aberto de uma mesa específica. | Média |
| RF13 | Busca Parcial | Permitir buscar mesas ou pratos por nome ou número parcial. | Média |
| RF14 | Relatórios/Gráficos | Permitir ao gerente gerar gráficos (mesas mais usadas, pratos mais pedidos etc.). | Média |
| RF15 | Persistência | Registrar todos os dados no banco SQLite com operações CRUD. | Alta |

## 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :-- | :--------- | :-------: | :-----------: |
| RNF01 | Performance | O sistema deve carregar telas em até 2 segundos. | Desempenho | Essencial |
| RNF02 | Usabilidade | A interface deve ser simples e adequada para uso rápido em restaurante. | Usabilidade | Essencial |
| RNF03 | Segurança | Senhas devem ser armazenadas de forma segura. | Segurança | Essencial |
| RNF04 | Disponibilidade | O sistema deve funcionar sem interrupções durante o horário de operação. | Operacional | Essencial |
| RNF05 | Portabilidade | Deve rodar em computadores e dispositivos móveis via navegador. | Técnica | Importante |
| RNF06 | Persistência | Todos os dados devem ser salvos no banco SQLite. | Técnica | Essencial |
| RNF07 | Integridade | Não deve permitir operações que quebrem relações entre entidades. | Segurança | Essencial |
