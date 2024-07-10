# input
primeiro_valor = input('digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

# verificação dos valores
...

# conversão dos tipos de dados 
primeiro_valor_float = float(primeiro_valor)
segundo_valor_float = float(segundo_valor)

# comparação entre os valores
primeiro_maior = primeiro_valor_float > segundo_valor_float
ambos_iguais = primeiro_valor_float == segundo_valor_float

# imprimindo com condicionais
if primeiro_maior:
    print(f'o {primeiro_valor_float=:.2f} é maior do que o {segundo_valor_float=:.2f}')
elif ambos_iguais:
    print('ambos os valores são iguais')
else:
    print(f'o{segundo_valor_float=:.2f}, é maior do que {primeiro_valor_float=:.2f}')

