# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :------: |
| 27/11/25 | 1.0 | Versão inicial | Gabriel Carrilho da Silva, Sarah Medeiros dos Santos, Emilly Yasmim Batista da Conceição |

---

## 1. Objetivo do projeto

Implementação de um sistema web para gerenciamento de mesas, pedidos e cardápio de um restaurante, permitindo controle eficiente das operações por gerente, garçom e chef. O sistema utilizará SQLite para persistência dos dados.

---

## 2. Descrição do problema

|    |    |
| -- | -- |
| **Problema** | Falta de organização no controle de mesas, pedidos e preparo. |
| **Afeta** | Gerentes, garçons e chefs. |
| **Impacta** | Atrasos, erros, baixa eficiência e dificuldade no acompanhamento do fluxo de trabalho. |
| **Solução** | Desenvolvimento de um sistema integrado para gerenciar mesas, pedidos, cardápio e preparo, com armazenamento em SQLite. |

---

## 3. Descrição dos usuários

| Nome | Descrição | Responsabilidade |
| :--: | :-------: | :--------------: |
| **Gerente** | administrador geral do sistema | cadastrar usuários, gerenciar cardápio, gerenciar mesas e visualizar relatórios |
| **Garçom** | funcionário responsável pelo atendimento | gerenciar ocupação das mesas, criar pedidos e enviá-los à cozinha |
| **Chef** | responsável pelo preparo dos pratos | visualizar pedidos enviados, atualizar status e finalizar preparo |

---

## 4. Descrição do ambiente dos usuários

O sistema será acessado via navegador em dispositivos do restaurante, como computadores, tablets ou celulares.  
O banco de dados SQLite armazenará informações de mesas, usuários, pratos, pedidos e itens.

---

## 5. Principais necessidades dos usuários

1. **Gerente**
   - cadastrar usuários  
   - gerenciar mesas  
   - gerenciar cardápio  
   - consultar mesas e cardápio  
   - realizar pesquisas  
   - visualizar gráficos e relatatórios  

2. **Garçom**
   - consultar mesas  
   - ocupar e liberar mesas  
   - criar pedidos  
   - adicionar itens a pedidos  
   - enviar pedidos para cozinha  
   - listar pedidos por mesa  

3. **Chef**
   - visualizar pedidos enviados  
   - atualizar status de preparo  
   - finalizar pedidos  

---

## 6. Alternativas concorrentes

1. **Consumer**
   - gerenciamento de mesas, pedidos, cardápio  
   - emissão fiscal integrada  
   - solução robusta para estabelecimentos maiores  

2. **Colibri**
   - controle de mesas e pedidos  
   - PDV integrado  
   - geração de relatórios operacionais  

---

## 7. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :--: | :-------: | :--------: |
| RF01 | Cadastro de usuários | Registrar usuários com perfis específicos (gerente/garçom/chef) | alta |
| RF02 | Login | Autenticação com perfil e controle de acesso | alta |
| RF03 | Gerenciar mesas | Criar, editar, listar e excluir mesas | alta |
| RF04 | Gerenciar pratos | Criar, editar, listar e excluir pratos | alta |
| RF05 | Consulta de mesas | Visualizar mesas e status (livre/ocupada) | alta |
| RF06 | Ocupação de mesa | Marcar ou liberar mesas | alta |
| RF07 | Criar pedido | Criar pedido vinculado a uma mesa | alta |
| RF08 | Adicionar itens ao pedido | Inserir pratos no pedido existente | alta |
| RF09 | Envio para cozinha | Pedido muda para status “enviado” | alta |
| RF10 | Pedidos da cozinha | Listar pedidos pendentes para preparo | alta |
| RF11 | Atualizar status | Alterar status conforme preparo | alta |
| RF12 | Listar pedidos por mesa | Exibir pedidos em aberto de uma mesa | média |
| RF13 | Pesquisa parcial | Busca de mesas, pratos ou pedidos | média |
| RF14 | Relatórios | Exibir gráficos e estatísticas | média |
| RF15 | Persistência | Registrar e recuperar dados via SQLite | alta |

---

## 8. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| RNF01 | Performance | Páginas devem carregar em até 2 segundos | desempenho | essencial |
| RNF02 | Usabilidade | Interface simples e intuitiva | usabilidade | essencial |
| RNF03 | Portabilidade | Acesso via qualquer navegador | técnica | importante |
| RNF04 | Persistência | Utilização do SQLite para armazenamento | técnica | essencial |
