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

## 🔁 `while`, `True`, `break`
Controlam **laços de repetição**:

```python
while True:
    idade = int(input("Digite a idade: "))
    if idade == 0:
        break
```

- `while`: repete enquanto a condição for verdadeira.
- `True`: valor booleano sempre verdadeiro → loop infinito.
- `break`: **interrompe** o loop imediatamente.

---

## 📏 `len()`
Retorna o **tamanho** de uma string (ou lista).

```python
len("Pedro")  # resultado: 5
```

---

## ✅ `Truthy` e ❌ `Falsey`
São **valores considerados verdadeiros ou falsos** em uma condição.

| Valor                   | É considerado... |
|-------------------------|------------------|
| `0`, `""`, `None`, `[]` | ❌ **Falsey**     |
| Qualquer outro valor    | ✅ **Truthy**     |

Exemplo:

```python
if not valor:  # entra aqui se valor for 0 (Falsey)
    break
```