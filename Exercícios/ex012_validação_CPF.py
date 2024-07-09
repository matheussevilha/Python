# Extraindo somente os números
CPF_usuario = input('Informe seu CPF:')
verificacao = True

if CPF_usuario[1]*len(CPF_usuario) == CPF_usuario:
    verificacao=False

    
if verificacao:
    numeros = []
    for digito in CPF_usuario:
        if digito.isnumeric():
            numeros.append(int(digito))
# Cálculo do primeiro dígito do CPF
    # Armazenando os valores colocados como dígito antes da verificação 
    digito_1 = numeros[9]
    digito_2 = numeros[10]

    # Removendo os dois digitos não verificados da lista
    for i in range(2):
        numeros.pop(-1)

    # Multiplicação regressiva
    numeros_multiplicados = []
    multiplicador = 10
    for i in range(9):
        numeros_multiplicados.append(numeros[i] * multiplicador)
        multiplicador -= 1

    # Soma dos valores multiplicados
    soma_9_primeiros = 0
    for i in range(9):
        soma_9_primeiros += int(numeros_multiplicados[i])

    # Multiplicar soma por 10
    soma_9_primeiros_10 = 10*soma_9_primeiros

    # Resto da divisão por 11
    resto_11 = soma_9_primeiros_10 % 11

    # Primeiro digito
    primeiro_digito = resto_11 if resto_11 < 10 else 0
    print(f'O primeiro digito é {primeiro_digito}')
    numeros.append(primeiro_digito)

    # Cálculo do segundo dígito do CPF

    # Multiplicação regressiva
    numeros_multiplicados_2 = []
    multiplicador = 11
    for i in range(10):
        numeros_multiplicados_2.append(numeros[i] * multiplicador)
        multiplicador -= 1

    # Soma dos valores multiplicados
    soma_10_primeiros = 0
    for i in range(10):
        soma_10_primeiros += int(numeros_multiplicados_2[i])

    # Multiplicar soma por 10
    soma_10_primeiros_10 = 10*soma_10_primeiros

    # Resto da divisão por 11
    resto_11_2 = soma_10_primeiros_10 % 11

    # Segundo digito
    Segundo_digito = resto_11_2 if resto_11_2 < 10 else 0
    print(f'O segundo digito é {Segundo_digito}')
    numeros.append(Segundo_digito)

    # Formatando CPF
    CPF_verificado_str = ''
    for n in numeros:
        CPF_verificado_str += str(n)

    # Usuário
    CPF_usuario = CPF_verificado_str[:3]+'.'+CPF_verificado_str[3:6]+'.'+CPF_verificado_str[6:9]+'-'+ str(digito_1)+str(digito_2)

    # Digitos verificados
    CPF_verificado = CPF_verificado_str[:3]+'.'+CPF_verificado_str[3:6]+'.'+CPF_verificado_str[6:9]+'-'+ CPF_verificado_str[9:11]

    # Verificação
    if CPF_usuario == CPF_verificado:
        print(f'{CPF_usuario} é válido.')
    else:
        print(f'{CPF_usuario} é inválido.')
else:
    print(f'{CPF_usuario} é inválido.')