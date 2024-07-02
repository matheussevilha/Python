nome = 'Estudo Python'
controle = 0

while controle < len(nome):
    if controle == 0:
        string_nova = '*'+ nome[controle]+'*'
    elif controle == 6:
        string_nova += ' *'
        controle += 1
        continue
    else:
        string_nova += nome[controle]+'*'
    controle += 1

print(string_nova)
