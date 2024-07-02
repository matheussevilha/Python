"""Cálculadora simples: Realiza uma operação entre dois números."""

Operação = True

while Operação: 
    # Dados necessários
    numero_1 = input('Digite o primeiro número:')
    numero_2 = input('Digite o segundo número:')
    operador = input('Qual operação deseja realizar("+","-","*","/")?')

    # Tratamento de erros
        # Váriavel de controle
    verificação = True
        # 1 número
    if not numero_1.isnumeric():
        print('O primeiro número foi digitado incorretamente.')
        verificação = False
        # 2 número
    if not numero_2.isnumeric():
        print('O segundo número foi digitado incorretamente')
        verificação = False
        # Operadores
    operadores_validos = '+-*/'
    if operador not in operadores_validos:
        print("O operador foi digitado incorretamente")
        verificação = False
    if len(operador) > 1:
        print("O operador foi digitado incorretamente")
        verificação = False
        
    # Conta
    # Caso tenha errado na digitação:
    if verificação is False:
        r1 = input('Deseja digitar novamente?[s]im/[n]ão\n')
        if r1.lower().startswith('s'):
            continue
        else:
            break
    # Caso todos valores tenham sido digitados corretamente
    else:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        if operador == '*':
            resultado = numero_1*numero_2
        elif operador == '+':
            resultado = numero_1+numero_2
        elif operador == '-':
            resultado = numero_1-numero_2
        else:
            resultado = numero_1/numero_2
        
        print(f'{resultado=}')
        r2 = input('Deseja digitar novamente?[s]im/[n]ão\n')
        if r2.lower().startswith('s'):
            continue
        else:
            break
