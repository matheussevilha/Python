import os

# Introdução ao jogo
print('This is a guessing game. One player will type a secret word, and the other will have to guess it.\nThe game has two phases, one for each player. If you guess, you win.\n')

# Recebendo dados do usuário
jogador_1 = input('player 1 - type your nickname:')
jogador_2 = input('player 2 - type your nickname:')

 # Script do jogo
def script_jogo(player1,player2):
    verify = True
    while verify:
        # Recebendo a palavra secreta
        print('\n** Digite apenas letras **\n** Não digite espaços **\n')
        palavra_secreta = input(f"{player1} - type the secret word (don't show to {player2}):").lower()
        palavra_secreta_vazia = '_' * len(palavra_secreta)
        # Verificação/ Tratamento dos erros
        if not palavra_secreta.isalpha():
            print('The word was typed with numbers, spaces or special caracteres.')
        # Saindo do laço de repetição
        else:
            verify = False

    # Verificando o número de letras não repetidas
    letras_nrepetidas = ''
    for p in range(0,len(palavra_secreta)):
        letra = palavra_secreta[p]
        if letra in letras_nrepetidas:
            continue
        else:
            letras_nrepetidas += letra
    
    # Definindo o número máximo de tentativas
    tentativas_maxima = len(letras_nrepetidas)*2
    tentativas = 0

    # Game
    while True:
        # Limpando o terminal
        os.system('cls')
        print(f'{tentativas=}\n{tentativas_maxima=}')
        if tentativas < tentativas_maxima:
            # Exibindo a palavra com espaços vazios
            print(f"secret word:{palavra_secreta_vazia}")
            # Recebendo a letra 
            letra = input(f"{player2} - type a letter:").lower()
            # Verificando o input
            if len(letra)>1:
                print('você digitou mais que uma letra.')
                continue
            if not letra.isalpha():
                print('você não digitou uma letra.')
                continue
            tentativas += 1
            # Verificando se a letra está na palavra
            for p in range(0,len(palavra_secreta)):
                if letra == palavra_secreta[p]:
                    palavra_secreta_vazia = palavra_secreta_vazia[0:p] + letra + palavra_secreta_vazia[p+1:len(palavra_secreta_vazia)]
            
            # Encerrando o laço 
            if palavra_secreta_vazia == palavra_secreta:
                print(palavra_secreta)
                print(f"Congratulations,{player2}, you guessed the word!\nAttempts:{tentativas}")
                break
        else:
            print("Derrota!\nVocê atingiu o número máximo de tentativas!")
            break

# Iniciando o jogo
script_jogo(jogador_1,jogador_2)
print(f'\n----- Now is {jogador_1}\'s turn -----\n')
script_jogo(jogador_2,jogador_1)