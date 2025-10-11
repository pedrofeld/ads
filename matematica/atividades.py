"""
1. Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a
20. Em seguida, verifique se o número -1 está neste conjunto
"""

numeros = list(range(-10, 21))
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
print(350 in s)

"""
4. Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012,
323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que
armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário
está ou não neste conjunto para permitir ou proibir a entrada na residência
"""

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

v=(1210, 897, 1230, 1495, 799, 890, 1010)
v_desconto = [preco * 0.8 for preco in v]
print(v_desconto)

"""
6. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v utilizando o
Python.

"""

import numpy as np
u=np.array([[3, 4, 8]])
v=np.array([[10, 12, -1]])
w=u+v
print(w)


"""
7. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v utilizando o
Python
"""

u2=np.array([[3, 4, 8]])
v2=np.array([[10, 12, -1]])
w2=u2-v2
print(w2)

"""
8. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u.v utilizando o
Python.
"""

u3=np.array([[3, 4, 8]])
v3=np.array([[10, 12, -1]])
w3=u3*v3
print(w3)

"""
9.  Considere as matrizes
Utilize o Python para obter a matriz C=A+B.
"""

a = np.array([[3, 5, 9], [4, 2 ,-3], [1, 5, -5]])
b = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])
somaab = a + b
print(somaab)

"""
10. Considere as matrizes
Por meio do Python, obtenha a matriz C=A.B.
"""

C=np.matmul(a, b)
print(C)

"""
11.
"""

"""
12.
"""

"""
13.
"""

"""
14.
"""