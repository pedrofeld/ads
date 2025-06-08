# 📚 Resumo: Banco de Dados – Aula 1

## 🧠 Fundamentos

- **Dado ≠ Informação**:  
  - Dado é bruto (ex: "10"), informação é o dado interpretado (ex: "idade = 10").

- **Banco de Dados (BD)**:  
  - Local para armazenar dados inter-relacionados com acesso rápido, seguro e confiável.

---

## 🗂️ Modelos de Banco de Dados

1. **Hierárquico**: estrutura em árvore, relações pai-filho.
2. **Rede**: mais flexível, com múltiplas relações.
3. **Orientado a Objetos**: dados como objetos com métodos.
4. **Relacional**: dados em tabelas com chaves (mais comum).
5. **NoSQL (não-relacional)**: flexível, ideal para grandes volumes e dados semiestruturados.

---

## ⚙️ Sistema Gerenciador de Banco de Dados (SGBD)

- Software que faz a interface entre os dados e os usuários/aplicações.
- Exemplos: **MySQL**, **PostgreSQL**, **Oracle**, **SQL Server**.

### ✨ Funções principais:
- Controle de concorrência e acesso
- Garantia de integridade dos dados
- Backups e recuperação
- Eliminação de redundância e inconsistência

---

## 🛠️ Projeto de Banco de Dados

### 🔄 Etapas:
1. **Análise de requisitos**
2. **Modelo conceitual**: independente do SGBD
3. **Modelo lógico**: com chaves, tipos de dados e normalização
4. **Modelo físico**: implementação no SGBD

---

## 📊 Modelagem Conceitual – MER

- **Entidades**: objetos do mundo real (ex: Cliente, Produto).
- **Campos**: propriedades das entidades (ex: nome, idade).
- **Relacionamentos**: associação entre entidades (ex: Cliente realiza Pedido).

### Tipos de Entidades:
- **Fundamental**: independente (ex: Cliente)
- **Associativa**: vem de relacionamento N:N (ex: ItemPedido)
- **Fraca**: depende de outra entidade (ex: Dependente de Funcionário)

### Tipos de Campos:
- Obrigatório / Opcional
- Simples / Composto
- Monovalorado / Multivalorado
- Derivado (ex: idade)

---

## 🔑 Chaves

- **Primária (PK)**: identifica unicamente uma instância. Não pode repetir ou ser nula.
- **Estrangeira (FK)**: faz referência à chave primária de outra entidade.

---

## 🔁 Relacionamentos e Cardinalidade

- **1:1**: um para um
- **1:N**: um para muitos (FK no lado N)
- **N:N**: muitos para muitos → criar entidade associativa

### Cardinalidade mínima e máxima:
- Representa o número mínimo e máximo de instâncias em um relacionamento  
  - Exemplo: (1,1), (0,n)

---

## 🛒 Estudo de Caso: Sistema de Delivery

Entidades principais:
- Cliente
- Restaurante
- Pedido
- Produto
- Entregador
- Funcionário
- Cidade
- Estado

Relacionamentos aplicam:
- Regras de negócio
- Cardinalidades
- Chaves estrangeiras e associativas