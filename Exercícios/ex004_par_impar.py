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

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""