# exercicio para o cálculo do imc
nome = input('digite seu nome:')
altura = float(input('digite sua altura em metros:'))
peso = int(input('digite seu peso em kg:'))

# cálculo do imc
imc = peso/ (altura**2) 

# print
print('nome:', nome, '\naltura:', altura, '\npeso:',peso,'\nimc:', imc )

# formatação
print(f'nome:{nome}\naltura:{altura:.2f}\npeso:{peso}\nimc:{imc:.2f}')
