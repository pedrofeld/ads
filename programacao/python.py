# Aula prática 1

## Exercício 1

from functools import total_ordering

preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preço do produto é {preco}. Desconto de {percentual}%')
print(f'Valor calculado de desconto: {desconto}. Valor final do produto: {final}')

## Exercício 2

km = int(input('Quantos km foram percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))

totalAluguel = (km * 0.15) + (dias * 60)

print(f'O valor total a ser pago é R${totalAluguel}')

## Exercício 3

frase = input('Digite uma frase:')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)]

print(frase2[-2:])

# Aula prática 2

## Exercício 1

totalPedido = 0

while True:
    op = int(input("Qual item gostaria de comprar? "))
    qtd = int(input("Quantas unidades quer comprar? "))

    if (op == 1):
        totalPedido = totalPedido + qtd * 5
    elif (op == 2):
        totalPedido = totalPedido + qtd * 7
    elif (op == 3):
        totalPedido = totalPedido + qtd * 4
    elif (op == 4):
        totalPedido = totalPedido + qtd * 6
    elif (op == 5):
        break
    else:
        print("Produto inválido. Selecione outro.")

print(f"O total a ser gasto neste pedido é de R${totalPedido}")

## Exercício 2

valor = int(input("Digite o valor em R$ : "))

while True:
    if valor >= 100:
        cont100 = valor // 100 # o // significa que o sistema só vai pegar o número inteiro da divisão e deconsiderar o resto
        valor = valor - cont100 * 100
        print(f"Cédulas de 100: {cont100}")
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print(f"Cédulas de 50: {cont50}")
        if not valor:
            break

    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f"Cédulas de 20: {cont20}")
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print(f"Cédulas de 10: {cont10}")
        if not valor:
            break

    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print(f"Cédulas de 5: {cont5}")
        if not valor:
            break

    if valor >= 1:
        cont1 = valor
        print(f"Cédulas de 1: {cont1}")
        break

## Exercício 3

qtdPessoas = 0
somaIdades = 0
valorTotal = 0

while True:
    idade = int(input("Informe a idade: "))

    if idade == 0:
        break

    if idade < 3:
        print("Ingresso gratuito!")
    elif idade <= 12:
        print("O ingresso custa R$15,00")
        valorTotal += 15
    else:
        print("O ingresso custa R$30,00")
        valorTotal += 30

    qtdPessoas += 1
    somaIdades += idade

if qtdPessoas > 0:
    mediaIdades = somaIdades / qtdPessoas
    print(f"Valor total: R${valorTotal}. Média de idades: {mediaIdades}")
else:
    print("Não foi possível prosseguir")

# Aula teórica 5

## Exercício 1

def borda(s1):
    tam = len(s1)
    # só imprime caso exista algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')

## Exercício 2

def valida_string(pergunta, min, max):
    s2 = input(pergunta)
    tam = len(s2)
    while ((tam < min) or (tam > max)):
        s2 = input(pergunta)
        tam = len(s2)
    return s2

x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string {}. \n Dado válido. Encerrando o programa...'.format(x))

## Exercício 3

while True:
    try:
        x = int(input('Digite um número: '))
        break
    except ValueError:
        print('Número inválido, tente novamente')

## Exercício 4

i = 0

while True:
    try:
        nome = input('Digite seu nome: ')
        ind = int(input('Digite um índice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Nome inválido, o dado inserido precisa ser uma string')
    except IndexError:
        print('índice inválido, o dado inserido precisa ser um número existente')
    finally:
        print(f'Tentativa [i]')
        i += 1

## Exercício 5

res = lambda x: x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3, 5))

calc = lambda a, b: (a + 5) * b
print(calc(5, 10))

# Aula prática 4

## Exercício 1

def valida_int(pergunta, min, max)
    x = int(input(pergunta))
    while((x < min) or (x > max))
        x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula a fatorial de um número.
    :para num: numero recebido, precisa ser maior que 0
    :return: valor retornado, resultado da fatorial
    """

    fat = 1
    if num = 0:
        return fat
    for i in range (1, num + 1, 1):
        fat *= 1
    return fat

x = valida_int('Digite um valor para calcular a fatorial: ', 0 , 9999)
print(f'{x}! = {fatorial(x)}')
help(fatorial)