# Exercício 1:

n = input('digite um número inteiro: ')
try:
    n_int = int(n)
    if n_int % 2 == 0:
        print('é par')
    else:
        print('é ímpar')
except:
    print('é necessário ser um valor inteiro.')

# Exercício 2:

hora = input('(informe apenas as horas, sem os minutos. Ex: 11, 12..)\nQue horas são ? ')

try:
    hora_int = int(hora)
    if hora_int>0 and hora_int<12:
        print('bom dia')
    elif hora_int>11 and hora_int<18:
        print('boa tarde')
    elif hora_int > 24:
        print('Os dados foram digitados de maneira errada')
    else:
        print('boa noite')
except:
    print('Os dados foram digitados de maneira errada')

# Exercício 3:

nome = input('Digite seu primeiro nome: ')
try:
    nome_str = str(nome)
    if len(nome_str) <= 4:
        print('Seu nome é curto.')
    elif len(nome_str) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é grande.')
except:
    print('O nome não foi inserido corretamente.')


