def multiplicacao (args):
    args = list(args)
    total = 1
    i = 0
    while i < len(args):
        total = total * args[i]
        i += 1
    return total


lista = [1,2,3,4,5]

print(multiplicacao(lista))
