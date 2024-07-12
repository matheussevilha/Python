def par_impar (numero: int) -> str:
    string = f'{numero}: é par.' if (numero % 2 == 0) else f'{numero}: é ímpar.'
    return string

print(par_impar(3))
