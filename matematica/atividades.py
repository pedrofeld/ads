print("-----Aula prática 04-----")

"""
1. Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a
20. Em seguida, verifique se o número -1 está neste conjunto
"""

numeros = list(range(-10, 21))
print("Atividade 1:")
print(-1 in numeros)

# ou

# print(-1 in range(-10, 21))

# ou

# import numpy as np
# C=np.linspace(-10, 20, 31)
# print(C)
# -1 in C


"""
2. Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a
20. Em seguida, verifique se o número -11 está neste conjunto.
"""
print("Atividade 2:")
print(-11 in numeros)

"""
3. No conjunto a seguir são apresentados os valores dos salários mínimos de 1995
a 2022 dispostos em ordem cronológica.
S={100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}
Verifique, por meio do Python, se o valor R$ 350,00 está neste conjunto.
"""

s={100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}
print("Atividade 3:")
print(350 in s)

"""
4. Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012,
323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que
armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário
está ou não neste conjunto para permitir ou proibir a entrada na residência
"""

print("Atividade 4:")
senhasExistentes = {452012, 323233, 787910, 528917, 683524}
senhaDigitada = int(input("Digite sua senha: "))
if senhaDigitada in senhasExistentes:
    print("Acesso permitido")
else:
    print("Acesso negado")

"""
5. O vetor v contém os preços de venda de algumas mercadorias:
v=(1210, 897, 1230, 1495, 799, 890, 1010)
A loja está com uma promoção onde é dado um desconto de 20% em todas as
mercadorias. Por meio do Python, obtenha o vetor que contém os preços destas
mercadorias com o desconto.

"""

vetor=(1210, 897, 1230, 1495, 799, 890, 1010)
v_desconto = [preco * 0.8 for preco in vetor]
print("Atividade 5:")
print(v_desconto)

"""
6. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v utilizando o
Python.

"""

import numpy as np
u=np.array([[3, 4, 8]])
v=np.array([[10, 12, -1]])
w=u+v
print("Atividade 6:")
print(w)


"""
7. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v utilizando o
Python
"""

u2=np.array([[3, 4, 8]])
v2=np.array([[10, 12, -1]])
w2=u2-v2
print("Atividade 7:")
print(w2)

"""
8. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u.v utilizando o
Python.
"""

u3=np.array([[3, 4, 8]])
v3=np.array([[10, 12, -1]])
w3=np.inner(u3, v3)
print("Atividade 8:")
print(w3)

"""
9.  Considere as matrizes
Utilize o Python para obter a matriz C=A+B.
"""

a = np.array([[3, 5, 9], [4, 2 ,-3], [1, 5, -5]])
b = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])
somaab = a + b
print("Atividade 9:")
print(somaab)

"""
10. Considere as matrizes
Por meio do Python, obtenha a matriz C=A.B.
"""

c=np.matmul(a, b)
print("Atividade 10:")
print(c)

"""
11. Construa o gráfico da função y=x^3-2x^2+12x-1 no intervalo [-3, 4]
"""

import matplotlib.pyplot as plt

x = np.linspace(-3, 4, 100)
y = x**3 - 2*x**2 + 12*x - 1
plt.plot(x, y)
plt.title("Atv. 11 - Gráfico da função y=x^3-2x^2+12x-1")
plt.show()

"""
12. Quais são as coordenadas do vértice da função f(x)=-2x^2+21x-8?
"""

a0 = -2
b0 = 21
c0 = -8
xv = -b0/(2*a0)
delta = b0**2 - 4*a0*c0
yv = -delta/(4*a0)
print(f"Atv. 12 - Vértice: ({xv}, {yv})")

"""
13. Uma empresa produz carregadores para um determinado modelo de telefone
celular e precisa obter a função que relaciona o lucro mensal com o preço de venda
dos carregadores. Os custos fixos mensais da empresa correspondem a R$
47.500,00. Para um preço de venda de R$ 12,00 por unidade, o lucro mensal
corresponde a R$ 22.000,00. Quando cada carregador é vendido por R$ 20,00, o
lucro mensal é de R$ 20.450,00. Obtenha o polinômio interpolador que relaciona o
lucro y com o preço de venda x.
"""

from scipy.interpolate import *

custosFixos = -47500 # é negativo porque é um custo
precoCelular = 12
lucroCelular = 22000
precoCarregador = 20
lucroCarregador = 20450

x1 = [precoCelular, precoCarregador, 0] # [12, 20, 0] (0 é o custo fixo)
y2 = [lucroCelular, lucroCarregador, custosFixos] # [22000, 20450, -47500]

p = lagrange(x1, y2)
print(f"Atv. 13 - Polinômio: {p}")

"""
14. Obtenha a soma 7+8 módulo 12.
"""

a1 = 7
b1 = 8
m = 12
soma = (a1 + b1) % m
print(f"Atv 14 - Soma: {soma}")

print("-----Aula prática 05-----")

"""
1. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Qual foi a duração média de cada episódio?
"""

print("Atividade 1:")
import pandas as pd
episodios={'Episódios': [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}
p = pd.DataFrame(episodios)
media = p['Episódios'].mean()
print(media)

"""
2. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Qual foi a moda?
"""
print("Atividade 2:")
moda = p['Episódios'].mode()
print(moda)

"""
3. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Qual foi a mediana?
"""

print("Atividade 3:")
mediana = p['Episódios'].median()
print(mediana)

"""
4. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
Obtenha o desvio padrão por meio do Python.
"""

print("Atividade 4:")
duracao={'Duração':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32]}
d=pd.DataFrame(duracao)
desviopadrao=d['Duração'].std()
print(f'Desvio padrão: {desviopadrao}')

"""
5. Utilizando a fórmula de Slovin e o Python, qual é o tamanho da amostra
referente a uma população de 200.000 dados considerando uma margem de erro de
4%?
"""
print("Atividade 5:")
from math import ceil
N=200000
e=0.04
ne=ceil(N/(1+N*e**2))
print(f'Tamanho da amostra: {ne}')

print("-----Aula prática 06----")

"""
1. Um dos primeiros algoritmos destinados à criptografia de mensagens foi a Cifra
de César. É um algoritmo simples baseado na substituição de letras por outras a
partir de uma troca de posições. Utilizando uma troca pela letra que está quatro
posições à frente, temos que a letra “a” é substituída pela letra “e”, a letra “b” é
substituída pela letra “f” e assim por diante. Considerando a mensagem “MAIS
AMOR”, por meio do Python, qual é a respectiva forma criptografada utilizando a
Cifra de César com a substituição descrita acima?
"""

print("Atividade 1:")
from string import ascii_uppercase
a=list(ascii_uppercase)
mensagem=input('Digite a mensagem: ')
mensagem=mensagem.upper()
mc=""
for l in mensagem:
    i=ord(l)-65
    if l in a:
        mc+=a[(i+3)%26]
    else:
        l
print(f'Mensagem criptografada: {mc}')

"""
2. Um dos primeiros algoritmos destinados à criptografia de mensagens foi a Cifra
de César. É um algoritmo simples baseado na substituição de letras por outras a
partir de uma troca de posições. Utilizando uma troca pela letra que está quatro
posições à frente, temos que a letra “a” é substituída pela letra “e”, a letra “b” é
substituída pela letra “f” e assim por diante. Considerando a mensagem
criptografada “IRXIRHMQIRXS”, qual é a mensagem original utilizando a Cifra de
César com a substituição descrita acima?
"""

print("Atividade 2:")
from string import ascii_uppercase
a=list(ascii_uppercase)
mensagem=input('Digite a mensagem: ')
mensagem=mensagem.upper()
mc=""
for l in mensagem:
    i=ord(l)-65
    if l in a:
        mc+=a[(i-3)%26]
    else:
        l
print(f'Mensagem criptografada: {mc}')

"""
3. Na criptografia RSA (Rivest-Shamir-Adleman), as letras são substituídas por
números de dois dígitos. O Python possui uma biblioteca destinada à criptografia
RSA. Considerando a palavra “mensagem”, qual é a respectiva forma criptografada?
"""

print("Atividade 3:")
import rsa
chavepublica,chaveprivada=rsa.newkeys(512)
mensagemrsa=input('Digite a mensagem: ')
mensagemrsacripto=rsa.encrypt(mensagemrsa.encode(),chavepublica)
print("Mensagem original:", mensagemrsa)
print("Mensagem criptografada:", mensagemrsacripto)