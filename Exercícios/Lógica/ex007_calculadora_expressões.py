"""Desenvolvendo uma calculadora de expressões matemáticas com limitações para operadores"""

# funções:

# verificação
def verify(x:int, y:str) -> bool:
    valores_validos = '0123456789()+-*/'
    valido = None
    while x < len(y):
        if y[x] not in valores_validos:
            valido = False
            break
        else:
            valido = True
        x +=1
    return valido

# operadores
def operadores (x:int, y:str):
    operadores = []
    operadores_index = []
    operadores_validos = '+-/*'
    while x<len(y):
        if y[x] in operadores_validos:
            operadores_index.append(x)
            operadores.append((y[x]))
        x += 1
    return operadores_index, operadores

# parenteses
def parenteses (x:int, y:str):
    parenteses = []
    parenteses_index = []
    while x<len(y):
        p = y[x]
        if p =='(' or p == ')':
            parenteses_index.append(x)
            parenteses.append(y[x])
        x += 1
    return parenteses, parenteses_index

# numeros
def numeros (x: int, y:str):
    numeros = []
    numeros_index = []      
    while x < len(conta):
        if conta[x].isdigit():
            numeros_index.append(x)
            numeros.append(conta[x])
        x += 1
    return numeros_index,numeros

operacao = True

while operacao:
    conta = input("Digite a conta:")
    vcontrol = 0
    flag1 = None

    if verify(vcontrol,conta):
        operadores(vcontrol, conta)
        parenteses(vcontrol, conta)
        numeros(vcontrol, conta)
        print(operadores(vcontrol, conta),parenteses(vcontrol, conta),numeros(vcontrol, conta) )
        print(conta, eval(conta),sep='\n')
    else:
        print('Os valores foram digitados incorretamente.') 
        flag1 = True   
        continue
    # continuação   
    if flag1:
        r1 = input('Deseja digitar novamente?([s]im [n]ão):')
        r1 = r1.lower().startswith("s")
        if r1 is not True:
            operacao = False
    else:
        r2 = input('Deseja continuar?([s]im [n]ão):')
        r2 = r2.lower().startswith("s")
        if r2 is not True:
            break   
   