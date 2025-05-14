# 📘 Resumo dos Comandos Python Utilizados

## 📥 `input()`
Pede ao usuário para digitar alguma coisa. Sempre retorna uma **string** (texto).

```python
nome = input("Digite seu nome: ")
```

---

## 📤 `print()`
Exibe algo na tela.

```python
print("Olá, mundo!")
```

---

## 🔢 `int()` e `float()`
Convertem strings para **número inteiro** (`int`) ou **número com casas decimais** (`float`).

```python
idade = int("25")     # vira número 25
preco = float("9.99") # vira número 9.99
```

---

## ➗ `//` (Divisão inteira)
É a **divisão inteira**. Retorna só o número inteiro da divisão, sem o resto.

```python
10 // 3  # resultado: 3
```

---

## 🧠 `if`, `elif`, `else`
Usado para tomar decisões com base em condições.

```python
if idade < 3:
    print("Ingresso grátis")
elif idade <= 12:
    print("Ingresso R$15")
else:
    print("Ingresso R$30")
```

- `if`: testa a primeira condição.
- `elif`: testa outra condição, caso o `if` falhe.
- `else`: executa se nenhuma das anteriores for verdadeira.

---

## 🔁 Estruturas de Repetição

### 📏 `for`
Usado para iterar sobre uma sequência (como uma lista ou string).

```python
for i in range(5):
    print(i)  # resultado: 0, 1, 2, 3, 4
```

- `range(n)`: gera uma sequência de números de 0 até n-1.

---

### 🔄 `while`
Executa um bloco de código enquanto a condição for verdadeira.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # resultado: 0, 1, 2, 3, 4
```

---

## ⚙️ Funções

### `def`
Define uma função que pode ser chamada posteriormente.

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))  # resultado: Olá, Maria!
```

---

## 📊 Tuplas
Estruturas de dados imutáveis. São criadas com parênteses.

```python
tupla = (1, 2, 3)
print(tupla[0])  # resultado: 1
```

---

## 📋 Listas
Estruturas de dados mutáveis. Criadas com colchetes.

```python
lista = [1, 2, 3]
lista.append(4)  # adiciona 4
print(lista)     # resultado: [1, 2, 3, 4]
```

---

## 🔤 Strings
Sequências de caracteres. Várias operações podem ser realizadas.

```python
texto = "Python"
print(texto.upper())  # resultado: PYTHON
```

### Métodos de Strings
- `lower()`: converte todos os caracteres para minúsculas.
- `upper()`: converte todos os caracteres para maiúsculas.
- `startswith()`: verifica se a string começa com o prefixo especificado.
- `find()`: retorna o índice da primeira ocorrência de uma substring.
- `replace()`: substitui uma substring por outra.

```python
texto = "Olá, Mundo!"
print(texto.lower())          # resultado: olá, mundo!
print(texto.startswith("Olá")) # resultado: True
print(texto.find("Mundo"))     # resultado: 5
print(texto.replace("Mundo", "Python")) # resultado: Olá, Python!
```

---

## 📚 Dicionários
Estruturas de dados que armazenam pares chave-valor.

```python
dicionario = {"nome": "Pedro", "idade": 25}
print(dicionario["nome"])  # resultado: Pedro
```

---

## 📦 Importação de Bibliotecas
Permite usar funções de bibliotecas externas.

```python
import math

print(math.sqrt(16))  # resultado: 4.0
```