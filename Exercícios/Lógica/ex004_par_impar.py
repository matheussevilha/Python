"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = input('digite um número inteiro: ')

n_int = n.isdigit()         # verificando se é um valor inteiro

if n_int:                   # transformando em inteiro
    n = int(n)
    par = n%2 == 0
    impar = n%2 == 1

    if n_int and par:
        print('o número é par')
    elif n_int and impar:
        print('o número é ímpar')
else:
    print('não é um inteiro')
