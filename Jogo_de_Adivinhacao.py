from random import randint
computador = randint (0, 20)
print('Tenho um desafio para você, entre um número de 0 a 20, em qual estou pensando')
print('Será que você consegue descobrir? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
            acertou = True
    else:
        if jogador < computador:
            print('Maior... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print ('Acertou com {} tentativas, parabéns!'.format(palpites))