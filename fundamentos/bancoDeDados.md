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

---

# 📘 Resumo - Aula 2: Banco de Dados

## 📌 TEMA 1 – MODELO RELACIONAL (LÓGICO)

### ✅ Conceitos Fundamentais
- **Modelo relacional**: dados armazenados em *tabelas (relações)*.
- **Tupla** = linha da tabela.
- **Atributo** = coluna.
- **Domínio** = tipo e tamanho permitido do dado.
- **Chaves**:
  - **Primária**: identifica unicamente cada tupla.
  - **Estrangeira**: referencia chave primária de outra relação.
  - **Composta**: formada por mais de um atributo.
  - **Surrogate key**: ID artificial (ex: `id` autoincremento).

### 🧮 Álgebra Relacional
- Linguagem matemática para consultas no modelo relacional.
- **Operadores**:
  - **Seleção (σ)**: filtra tuplas (linhas).
  - **Projeção (π)**: filtra atributos (colunas).
  - **Atribuição (⇐)**: salva resultado em uma nova relação.

## 📌 TEMA 2 – NORMALIZAÇÃO

### 🔄 Objetivo
Evitar redundância, inconsistências e melhorar integridade.

### 🧩 Formas Normais (FN)
- **1FN**: eliminar grupos repetitivos; todos os dados devem ser atômicos.
- **2FN**: remover atributos que dependem *parcialmente* da chave composta.
- **3FN**: eliminar dependências *transitivas* (atributos derivados de outros não-chave).

### 🧪 Exemplos Clássicos de Anomalias
- Exclusão: perder dados ao remover uma tupla.
- Atualização: inconsistências em atualizações.
- Inserção: dificuldade em inserir dados parciais.

## 📌 TEMA 3 – MODELO FÍSICO

### 💾 Características
- Conversão do modelo lógico em **script SQL**.
- Considera limitações do **SGBD** (ex: MySQL, PostgreSQL).
- Criação de:
  - Tabelas
  - Chaves (PK, FK)
  - Índices, Gatilhos, Procedimentos

### 🧰 Ferramentas
- **DBDesigner**: gera script SQL automaticamente (usado no curso).
- **MySQL Workbench**: ferramenta gráfica para execução de queries.

## 📌 TEMA 4 – MODELAGEM DIMENSIONAL (para BI)

### 🧊 Conceito
- Utilizada em **Data Warehouses** e **Data Marts**.
- Permite múltiplas visões dos dados (multidimensional).

### 📈 Tipos de Tabelas
- **Fato**: contém dados quantitativos (ex: total de vendas).
- **Dimensão**: contém dados descritivos (ex: data, produto, região).

### 🌟 Modelos
- **Estrela (Star Schema)**: fato central com dimensões conectadas.
- **Floco de Neve (Snowflake)**: dimensões normalizadas.
- **Constelação (Fact Constellation)**: várias tabelas fato.

## 📌 TEMA 5 – SQL (Structured Query Language)

### 🧾 Histórico
- Criado pela IBM, padronizado pelo ANSI/ISO.

### ⚙️ Subdivisões
- **DDL**: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
- **DML**: `INSERT`, `UPDATE`, `DELETE`, `MERGE`
- **DQL**: `SELECT`
- **DCL**: `GRANT`, `REVOKE`
- **DTL**: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

### 🧑‍💻 Query e Script
- **Query**: comando SQL.
- **Script**: conjunto de queries.
- Comentários:
  - Linha única: `-- comentário`
  - Múltiplas linhas: `/* comentário */`

### 🧑‍🏫 Dialetos SQL
- **PL/SQL** – Oracle, MySQL
- **T-SQL** – Microsoft SQL Server
- **PL/pgSQL** – PostgreSQL
- **SQL/PL** – DB2 (IBM)

---

# 📘 Resumo - Aula 3: Banco de Dados

## Tipos de Dados em SQL (SQL Data Types)

### Categorias:
1. **Numéricos:** `int`, `float`, `decimal`, `bit`, etc.
2. **Strings (Cadeias de caracteres):**
   - Binários: `binary`, `varbinary`, `blob`
   - Não-binários: `char`, `varchar`, `text`
3. **Temporais:** `date`, `time`, `datetime`, `timestamp`, `year`

### Dicas Importantes:
- `varchar` usa menos espaço que `char` quando há campos pouco preenchidos.
- `float` e `double` não têm escala definida. `decimal` permite precisão e escala exatas.
- `timestamp` considera fuso horário; `datetime` não.

---

## Comandos SQL Essenciais

### Mostrar bancos e tabelas:
```sql
SHOW DATABASES;
USE nome_banco;
SHOW TABLES;
DESCRIBE nome_tabela;
```

### Criar banco e tabela:
```sql
CREATE DATABASE nome_banco;
CREATE TABLE nome_tabela (
  id INT,
  nome VARCHAR(100),
  PRIMARY KEY(id)
);
```

### Inserir dados:
```sql
INSERT INTO nome_tabela (col1, col2) VALUES (val1, val2);
```

### Consultar dados:
```sql
SELECT * FROM nome_tabela;
SELECT coluna1, coluna2 FROM nome_tabela;
SELECT * FROM nome_tabela WHERE coluna IS NULL;
SELECT * FROM nome_tabela ORDER BY coluna DESC;
```

### Excluir objetos:
```sql
DROP TABLE nome_tabela;
DROP DATABASE nome_banco;
```

---

## Chaves (Constraints)

### Chave Primária (PK):
```sql
id INT NOT NULL,
PRIMARY KEY(id)
```

### Chave Estrangeira (FK):
```sql
estado_id INT NOT NULL,
FOREIGN KEY (estado_id) REFERENCES estado(id)
  ON DELETE NO ACTION ON UPDATE NO ACTION
```

### Chave Única (UK):
```sql
cnh INT UNIQUE
```

### Chave Composta:
```sql
PRIMARY KEY(pedido_id, produto_id)
```

---

## Outras Restrições

- `NOT NULL`: impede valores nulos.
- `CHECK`: (não funciona no MySQL) restringe valores a uma lista.
- `DEFAULT`: valor padrão para a coluna.
```sql
estadoCivil CHAR(1) DEFAULT 'S'
```

---

## Comando ALTER TABLE

### Adicionar coluna:
```sql
ALTER TABLE nome_tabela ADD nova_coluna TIPO(TAM);
```

### Modificar estrutura:
```sql
ALTER TABLE nome_tabela MODIFY coluna TIPO(TAM);
```

### Renomear coluna:
```sql
ALTER TABLE nome_tabela CHANGE nome_antigo nome_novo TIPO(TAM);
```

### Excluir coluna:
```sql
ALTER TABLE nome_tabela DROP COLUMN nome_coluna;
```

### Adicionar FK depois:
```sql
ALTER TABLE produto ADD tipoProduto_id INT NOT NULL;
ALTER TABLE produto ADD CONSTRAINT fk_tipo
FOREIGN KEY (tipoProduto_id) REFERENCES tipoProduto(id);
```

---

## Propriedades Especiais

- `UNSIGNED`: impede números negativos.
- `ZEROFILL`: preenche com zeros à esquerda.
- `AUTO_INCREMENT`: incrementa automaticamente um valor inteiro na coluna PK.
```sql
id INT UNSIGNED ZEROFILL AUTO_INCREMENT PRIMARY KEY
```

---

# 📘 Resumo - Aula 4: Banco de Dados (SQL - DML e Consultas)

## 👨‍🏫 Professores
Ricardo Sonaglio Albano e Silvie Guedes Albano

---

## 1. 📥 Inclusão de Registros (INSERT)

- `INSERT INTO tabela (colunas) VALUES (valores);`
- Aspas simples para `CHAR` e `DATE`; números sem aspas.
- `NULL` pode ser usado em campos opcionais.
- `auto_increment`: não deve ser incluído.
- Pode inserir em colunas específicas se respeitar restrições.
- Subquery: `INSERT INTO cliente (nome, cidadeId) SELECT nomeFunc, cidadeId FROM funcionario;`
- Vários registros: `INSERT INTO tabela VALUES (1, 'A'), (2, 'B');`

### ⚠️ Erros comuns:
- Campo `NOT NULL` sem valor.
- PK duplicada.
- Número de colunas ≠ número de valores.
- FK sem correspondência na tabela pai.

---

## 2. ❌ DELETE e ✏️ UPDATE

### DELETE
```sql
DELETE FROM tabela WHERE condição;
```
- Sem `WHERE` = apaga tudo.
- `TRUNCATE TABLE` é mais rápido, mas não aciona triggers nem cascade.

### ON DELETE
- `NO ACTION`: impede exclusão se houver dependentes.
- `CASCADE`: apaga tudo relacionado automaticamente.

### UPDATE
```sql
UPDATE tabela SET coluna = valor WHERE condição;
```
- Use `WHERE` para evitar atualizar tudo.
- Pode usar `SET coluna = (SELECT ...)` para atualizar dinamicamente.
- `ON UPDATE CASCADE`: atualiza FKs automaticamente.

---

## 3. 🔍 Restrições e Filtros em Consultas

### 🧠 Operadores Lógicos
- `AND`, `OR`, `NOT`

### 🔢 Relacionais
- `=`, `<>`, `>`, `<`, `>=`, `<=`
- `IN`, `NOT IN`, `LIKE`, `BETWEEN`, `IS NULL`, `EXISTS`

### ➕ Aritméticos
- `+`, `-`, `*`, `/`  
  (Se `NULL` estiver envolvido, resultado é `NULL`)

### Exemplos:
```sql
SELECT * FROM cliente WHERE salario BETWEEN 5000 AND 8000;
SELECT * FROM cidade WHERE uf IS NOT NULL;
SELECT * FROM cliente WHERE nome LIKE '%Silva%';
SELECT nome, salario FROM cliente ORDER BY nome;
```

---

## 4. 🔗 JOINs (junções entre tabelas)

### INNER JOIN
```sql
SELECT c.nomeCidade, e.nomeEstado
FROM cidade c
INNER JOIN estado e ON c.estadoID = e.id;
```

### LEFT JOIN
- Traz tudo da esquerda, mesmo sem correspondência na direita.

### RIGHT JOIN
- Traz tudo da direita, mesmo sem correspondência na esquerda.

### FULL JOIN (não suportado no MySQL)
- Simulável com `UNION` de `LEFT` + `RIGHT` com `WHERE`.

### CROSS JOIN
- Produto cartesiano: combina todas as linhas entre duas tabelas.

### SELF JOIN
```sql
SELECT f.nomeFunc, g.nomeFunc AS gerente
FROM funcionario f
JOIN funcionario g ON f.gerente = g.matricula;
```

### JOIN com várias tabelas
```sql
SELECT f.nomeFunc, c.nomeCidade, e.nomeEstado
FROM funcionario f
JOIN cidade c ON f.cidadeId = c.id
JOIN estado e ON c.estadoID = e.id;
```

---

## 5. 🧰 Comandos Adicionais

### Alias (`AS`)
- Para colunas:
```sql
SELECT nomeFunc AS 'Funcionário', salarioFunc * 1.1 AS 'Novo Salário'
FROM funcionario;
```
- Para tabelas:
```sql
SELECT f.nomeFunc FROM funcionario f;
```

### LIMIT
```sql
SELECT * FROM tabela LIMIT 5;          -- Primeiras 5
SELECT * FROM tabela LIMIT 3, 2;       -- Pula 3, mostra 2
```

### DISTINCT
```sql
SELECT DISTINCT nome FROM cliente;
```
- Remove duplicatas no resultado.

### CASE
```sql
SELECT nomeFunc,
CASE
  WHEN sexoFunc = 'M' THEN 'Masculino'
  WHEN sexoFunc = 'F' THEN 'Feminino'
  ELSE 'Outro'
END AS Genero
FROM funcionario;
```

### UNION vs UNION ALL
```sql
-- UNION remove duplicadas
SELECT nome FROM cliente
UNION
SELECT nomeFunc FROM funcionario;

-- UNION ALL mantém todas
SELECT nome FROM cliente
UNION ALL
SELECT nomeFunc FROM funcionario;
```

---

## ✅ Boas Práticas

- Evite `SELECT *` → impacta desempenho.
- Use `WHERE` sempre em `DELETE` e `UPDATE`.
- Evite `INSERT` com dezenas de linhas de uma vez.
- Sempre teste subqueries antes de aplicá-las.