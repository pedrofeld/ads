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