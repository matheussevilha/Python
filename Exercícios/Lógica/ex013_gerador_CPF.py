import random

nove_numeros = ''
for n in range(9):
    nove_numeros += str(random.randint(0,9))

soma = 0
multiplicador = 10
for i in range(9):
    soma += int(nove_numeros[i])*multiplicador
    multiplicador -= 1

digito_1 = str((soma*10)%11) if (soma*10)%11 < 10 else str(0)

dez_numeros = nove_numeros + digito_1

soma_10 = 0
multiplicador = 11
for i in range(10):
    soma_10 += int(dez_numeros[i])*multiplicador
    multiplicador -= 1

digito_2 = str((soma_10*10)%11) if (soma_10*10)%11 < 10 else str(0)

CPF = dez_numeros + digito_2

print(CPF)