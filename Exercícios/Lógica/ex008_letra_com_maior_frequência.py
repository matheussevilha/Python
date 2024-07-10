frase = 'hoje estou estudando python para melhorar meu conhecimento em tecnologia'

i = 0
maior_frequência = 0
letra_maior_frequência = ''
while i < len(frase):
    letra_atual = frase[i]    
    contagem = frase.count(letra_atual)
    if contagem > maior_frequência:
        maior_frequência = contagem
        letra_maior_frequência = letra_atual
    i += 1

print(letra_maior_frequência)


