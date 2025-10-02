# Matemática Aplicada à Computação (Aula 1)

## Introdução

*Lógica matemática*, suas aplicações em
ciência da computação e exemplos práticos em *Python*.\
Foram estudados **proposições, operadores lógicos, tabelas-verdade,
propriedades e aplicações computacionais**.

## Principais Tópicos

### 1. Proposições

-   Proposição: enunciado que pode ser verdadeiro (V) ou falso (F).
-   Exemplos:
    -   "4 é par" (V)\
    -   "Paris é a capital da França" (V)\
    -   "4+1=10" (F)\
-   Nem toda frase é proposição (ex.: perguntas ou saudações).

*Princípios fundamentais:* 
1. Não contradição: uma proposição não pode
ser V e F ao mesmo tempo.\
2. Terceiro excluído: só pode ser V ou F.

### 2. Operadores Lógicos Simples

-   *Negação (\~p / p' / ¬p / NOT):* inverte o valor lógico.\
-   *Conjunção (p ∧ q / p . q / AND):* só é verdadeira se ambos forem V.\
-   *Disjunção (p ∨ q / p + q / OR):* verdadeira se pelo menos um for V.

Exemplo em Python:

 python
M = float(input("Média obtida: "))
if M >= 70:
    print("Aprovado")
else:
    print("Reprovado")


### 3. Operadores Lógicos Intermediários

-   *NAND:* negação da conjunção (\~(p ∧ q)).\
-   *NOR:* negação da disjunção (\~(p ∨ q)).\
-   *XOR:* disjunção exclusiva, verdadeira apenas quando p e q têm
    valores diferentes.

### 4. Operadores Lógicos Avançados

-   *Condicional (p → q):* "Se p, então q". É falsa somente se p=V e
    q=F.\
-   *Bicondicional (p ↔ q):* "p se e somente se q". Verdadeira quando
    ambos têm o mesmo valor lógico.

### 5. Propriedades Importantes da Lógica

As propriedades permitem simplificar e reescrever expressões lógicas sem
alterar seu valor.

#### 🔄 1. Dupla Negação

    ¬(¬p) ⇔ p

Negar duas vezes equivale a manter a proposição.\
Exemplo: "Não é verdade que não gosto de matemática" ⇔ "Gosto de
matemática".

#### 🔁 2. Idempotência

    p ∨ p ⇔ p
    p ∧ p ⇔ p

Repetir a mesma proposição não muda o resultado.

#### 🔃 3. Comutatividade

    p ∨ q ⇔ q ∨ p
    p ∧ q ⇔ q ∧ p

A ordem não altera o resultado.

#### 🔗 4. Associatividade

    (p ∨ q) ∨ r ⇔ p ∨ (q ∨ r)
    (p ∧ q) ∧ r ⇔ p ∧ (q ∧ r)

Agrupamento diferente, mesmo resultado.

#### 📦 5. Distributividade

    p ∧ (q ∨ r) ⇔ (p ∧ q) ∨ (p ∧ r)
    p ∨ (q ∧ r) ⇔ (p ∨ q) ∧ (p ∨ r)

Parecido com distributiva da álgebra.

#### ⚖️ 6. Leis de De Morgan

    ¬(p ∧ q) ⇔ (¬p ∨ ¬q)
    ¬(p ∨ q) ⇔ (¬p ∧ ¬q)

Negar uma conjunção vira disjunção, e vice-versa.

#### 🔄 7. Contrapositiva

    p → q ⇔ ¬q → ¬p

Uma condicional pode ser reescrita pela sua contrapositiva.\
Exemplo:\
- "Se João estudou, então passou na prova".\
- "Se João não passou na prova, então não estudou".

--

## Exercício Resolvido

### Enunciado

Sabendo que uma proposição é um conjunto de palavras ou símbolos que
retratam um pensamento de sentido completo e que pode ser classificado
como verdadeiro ou falso, determine o valor lógico das seguintes
proposições:

a)  7 \< 2\
b)  (3+2=8)'\
c)  50 \< 70 ∨ 4 \> -2\
d)  tg 45° = 1 ∧ sen 45° = 0,5\
e)  4 \< 10 ⊕ 5 ≤ 9\
f)  2 + 2 = 4 → 2 + 3 = 6\
g)  2³ = 8 ↔ 2² = 4

### Resolução e explicação

*a)* 7 \< 2 → Falso (7 não é menor que 2).\
*b)* (3+2=8)' → 3+2=8 é Falso, a negação é Verdadeiro.\
*c)* 50 \< 70 (V) ∨ 4 \> -2 (V) → Verdadeiro (pois pelo menos uma é
V).\
*d)* tg 45° = 1 (V) ∧ sen 45° = 0,5 (F) → Falso (ambas precisariam ser
V).\
*e)* 4 \< 10 (V) ⊕ 5 ≤ 9 (V) → Falso (XOR exige valores diferentes).\
*f)* 2+2=4 (V) → 2+3=6 (F) → Falso (condicional é falsa quando p=V e
q=F).\
*g)* 2³=8 (V) ↔ 2²=4 (V) → Verdadeiro (bicondicional é V quando ambos
têm mesmo valor lógico).

# Matemática Aplicada à Computação (Aula 2)

*Bases numéricas*, conversões e operações em sistemas digitais.

---

## 1. Introdução
- Importância das bases numéricas para a computação.
- Histórico: desde formas primitivas de contagem até a criação dos computadores modernos.
- Evolução: ábaco, calculadoras mecânicas, ENIAC e o uso de bits.

---

## 2. Conceitos de Bases Numéricas
- *Sistema decimal (base 10):* mais comum, utiliza algarismos de 0 a 9.
- *Outras bases:* binária (2), quinária (5), octal (8), hexadecimal (16), entre outras.
- Uso prático: horas (base 12), representação de caracteres (ASCII).

---

## 3. Base Binária
- Utiliza apenas *0 e 1*.
- *Bit:* menor unidade de informação digital.
- *Byte:* conjunto de 8 bits.
- Conversões:
  - *Binário → Decimal:* multiplicação por potências de 2 e soma.
  - *Decimal → Binário:* divisões sucessivas por 2, coletando restos.
- Aplicação direta em computadores e na álgebra de Boole.

---

## 4. Base Hexadecimal
- Base 16: dígitos *0 a 9* e letras *A a F*.
- Facilita a representação de números binários longos.
- Conversões:
  - *Hexadecimal → Decimal:* multiplicação por potências de 16 e soma.
  - *Decimal → Hexadecimal:* divisões sucessivas por 16.
- Exemplo: decimal 11868 corresponde a *2E5C* no hexadecimal.

---

## 5. Algoritmos de Conversão (Python)
- Funções nativas:
  - bin() → conversão para binário.
  - hex() → conversão para hexadecimal.
- Manipulação de strings para extrair apenas os valores.
- Criação de algoritmos próprios com laços (while) e operações matemáticas.

---

## 6. Aritmética Binária
- Regras semelhantes à soma decimal, mas com *1+1=10*.
- Limitações de armazenamento em bits (exemplo: overflow em sistemas de 8 bits).
- Representação de números negativos:
  - *Complemento de 1:* falha por ter duas representações para o zero.
  - *Complemento de 2:* método eficiente usado em computadores.
    - Exemplo: -4 em 8 bits → 11111100.

---

# 📘 Guia Simples de Conversões Numéricas

Formas de conversões mais comuns na computação
e como somar números binários.

## 🔢 1. Binário → Decimal
1. Escreva o número binário.
2. Cada posição vale uma potência de 2 (da direita para a esquerda: 2⁰, 2¹, 2²...).
3. Multiplique cada dígito pela potência correspondente e some tudo.

👉 Exemplo: *1101 (binário)*  
(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)  
= 8 + 4 + 0 + 1 = *13 (decimal)*

---

## 🔢 2. Decimal → Binário
1. Divida o número por 2.  
2. Anote o resto (0 ou 1).  
3. Continue dividindo até o quociente ser 0.  
4. O binário é a leitura dos restos de baixo para cima.

👉 Exemplo: *25 (decimal)*  
25 ÷ 2 = 12 resto 1  
12 ÷ 2 = 6 resto 0  
6 ÷ 2 = 3 resto 0  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

➡️ Binário = *11001*

---

## 🔢 3. Hexadecimal → Decimal
- Hex usa 0–9 e A–F (A=10, B=11, ..., F=15).  
- Cada posição vale uma potência de 16.  

👉 Exemplo: *2E (hexadecimal)*  
(2 × 16¹) + (E × 16⁰)  
(2 × 16) + (14 × 1) = 32 + 14 = *46 (decimal)*

---

## 🔢 4. Decimal → Hexadecimal
1. Divida o número por 16.  
2. Anote o resto (se 10→A, 11→B, ..., 15→F).  
3. Continue até o quociente ser 0.  
4. O hexadecimal é a leitura dos restos de baixo para cima.

👉 Exemplo: *118 (decimal)*  
118 ÷ 16 = 7 resto 6  
7 ÷ 16 = 0 resto 7  

➡️ Hexadecimal = *76*

---

## ➕ 5. Soma de Binários
Regras:  
- 0 + 0 = 0  
- 0 + 1 = 1  
- 1 + 0 = 1  
- 1 + 1 = 10 (fica 0 e vai 1 para a próxima soma)  

👉 Exemplo: *1011 + 1101*  

   1011
+  1101
  -----
 11000
  
Resultado: *11000 (binário) = 24 (decimal)*