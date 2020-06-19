from random import randint
from time import sleep

def jokenpo():
    
    comp=randint(0, 2)
    print('-='*11)
    print('Bora jogar Pedra, Papel ou Tesoura!')
    sleep(0.9)
    print("""
Regras:
pedra=0
papel=1
tesoura=2
    """)
    sleep(0.5)
    
    jog = int(3)
    while jog >= 3:
        try:
            print('Qual você escolhe?')
            jog=int(input('>>: '))
        except:
            print('Escolha uma opção!\n')
    print(' ')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
    print(' ')
    if comp == 0:
        if jog == 0:
            print('Empate!')
            print('Os dois jogaram pedra.')
        elif jog == 1:
            print('O jogador ganhou!')
            print('O jogador jogou papel e o computador jogou pedra.')
        elif jog == 2:
            print('O computador ganhou!')
            print('O computador jogou pedra e o jogador jogou tesoura.')
    elif comp == 1:
        if jog == 0:
            print('O computador ganhou!')
            print('O computador jogou papel e o jogador jogou pedra.')
        elif jog == 1:
            print('Empate!')
            print('Os dois jogaram papel')
        elif jog == 2:
            print('O jogador ganhou')
            print('O jogador jogou tesoura e o computador jogou papel.')
    elif comp == 2:
        if jog == 0:
            print('O jogador ganhou!')
            print('O jogador jogou pedra e o computador jogou tesoura.')
        elif jog == 1:
            print('O computador ganhou!')
            print('O computafor jogou tesoura e o jogador jogou papel.')
        elif jog == 2:
            print('Empate!')
            print('Os dois jogaram tesoura')
    print(' ')
    print('Obrigado por jogar :)')
    print('-='*11)