#-*-coding:utf8;-*-
	
#arquivo responsavel por
#tratar a maioria dos comandos
#que não estão no banco ou no
#arquivo principal.

import time
from random import randint

import utils
from utils import defs
import etc
from etc import jokenposcript

def comand(user):
    if 'hora' in user:
        
        print(f'São umas {time.strftime("%I:%M %p")} horas ai')
        
    elif 'piada' in user:
        
        
        piada = utils.defs.openBd('jokes.dat')
        
        r = randint(1, 5)
        
        print(' ')
        
        if r == 1:
        
            print(piada[0][0])
            time.sleep(3)
            print(' ')
            print(piada[0][1])
            
        elif r == 2:
            
            print(piada[1][0])
            time.sleep(3)
            print(' ')
            print(piada[1][1])
        
        elif r == 3:
            
            print(piada[2][0])
            time.sleep(3)
            print(' ')
            print(piada[2][1])
        
        elif r == 4:
            
            print(piada[3][0])
            time.sleep(3)
            print(' ')
            print(piada[3][1])
        
        elif r == 5:
            
            print(piada[4][0])
            time.sleep(3)
            print(' ')
            print(piada[4][1])
    
    elif 'jogar' in user or 'jokenpo' in user:
        etc.jokenposcript.jokenpo()
    
    else:
        return 1