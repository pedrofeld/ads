# Atividade prática 1

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

# Atividade prática 2

## Exercício 1

totalPedido = 0

while True:
    op = int(input("Qual item gostaria de comprar? "))
    qtd = int(input("Quantas unidades quer comprar? "))

    if (op == 1):
        tototalPedido = totalPedido + qtd * 5
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