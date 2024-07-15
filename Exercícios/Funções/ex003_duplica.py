def multiplicador (n_vezes):
    def quantidade_de_vezes(numero):
        return numero * n_vezes
    return quantidade_de_vezes

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

for i in [1,2,3,4,5]:
    print(duplicar(i))
