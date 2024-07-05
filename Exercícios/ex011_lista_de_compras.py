import os
import time
"""Programa Lista de compras"""

lista_de_compras = []
# adicionando itens na lista
while True:
    os.system('cls')
    produto = input('Digite o produto que deseja comprar:')
    lista_de_compras.append(produto)

    # verificando se existem mais itens para adicionar
    # verificando a resposta - tratamento de erros:
    while True:
        continuar = input('Deseja inserir mais um produto? [s]im; [n]ão\n->').lower()
        if continuar.startswith('s') or continuar.startswith('n'):
            break
        else:
            print('Digite "s" ou "n"!')
            continue   
    if continuar.startswith('s'):
        continue
    else:
        break   
# alteração da lista
while True:
    os.system('cls')
    for indice, item in enumerate(lista_de_compras, start=1):
        print(indice,item)
    opcoes = input('Opções:\n[1] Excluir item\n[2] Alterar item\n[3] Adicionar item\n[4] Salvar lista\n->')
    # Excluir Item
    if opcoes == '1':
        opcoes = int(opcoes)
        while True:
            item_excluido = input('Qual item deseja excluir? (Digite apenas o número ao lado do item)\n->')
            try: 
                del lista_de_compras[int(item_excluido) - 1]
                break
            except:
                print('O número do item foi digitado incorretamente!')
    
    # Alterando Item
    elif opcoes == '2':
        opcoes = int(opcoes)
        while True:
            item_alterado = input('Qual item deseja alterar? (Digite apenas o número ao lado do item)\n->')
            try: 
                lista_de_compras[int(item_alterado) - 1] = input('O que deseja colocar no lugar?\n->')
                break
            except:
                print('O número do item foi digitado incorretamente!')

    # Adicionar Item
    elif opcoes == '3':
        valor_adicionado = input("O que deseja adicionar?\n->")
        lista_de_compras.append(valor_adicionado)
    
    # Salvando Lista
    elif opcoes == '4':
        os.system('cls')
        print('Lista:')
        for indice, item in enumerate(lista_de_compras, start=1):
            print(f'{indice}.{item}')
        break
    
    # Tratando Erros:
    else:
        print('A opção foi digitada incorretamente!')
        time.sleep(2)
        