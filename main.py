#-*-coding:utf8;-*-
#projeto feito por: Charles "Evaristo"
#canal: Conta Secundaria 

#libs

import csv
import utils
from utils import comands
from utils import defs
from time import sleep
from random import randint
from os import system

#definições basicas

caminho = '/sdcard/XhatbotX/bd/'

def line():
    print('-'*25)

def qbrl():
    print('')

def limp():
    limpv = "system('clear')"
    eval(limpv)

#lendo o banco de dados csv
#e botando numa lista

bd = []

f = open(f'{caminho}bd.dat','r')

leitor = csv.reader(f)

for l in leitor:
    bd.append(l)
    
f.close()

# boas vindas

limp()
utils.defs.nome()


# o programa em si

while True:
    
    user = str(input('>>: ')).lower()
    
    #comandos basicos do chat
    
    if user == '':
        qbrl()
        print(';-;')
        qbrl()
        continue
    
    elif 'sai' in user or 'flw' in user:
        print('Ok, flws aewww..')
        break
    
    elif 'comandos' in user:
        print("""Os comandos que eu posuo são:
            	
 Sair
 Mostrar comandos
 jogar
 piada
 hora
            	
Só esses porque meu programador não fez o resto ;-;""")
        continue
    
    #comandos mais elaborados
    #ficam no utils
    
    else:
        r = utils.comands.comand(user)
        
        if r == 1:
            pass
        else:
            continue
    
    #se não for um comando
    #verifica se esta no banco de dados
    
    i = 0
    
    for bjo in bd:
        
        if user in bjo:
            pass
        else:
            i = i + 1


    if i == len(bd):
        
        #se não estiver no bd ele ira perguntar
        
        print('não entendi ;-;')
        sleep(1)
        
        qbrl()
        print('Pode me ensinar isso? (S/N)')
        ens = str(input('>>> ')).lower()
        
        if 's' in ens:
            
            
            print(f'Me diga uma resposta para "{user}" ;-;')
            resp = str(input('>: '))
        
            k = open(f'{caminho}bd.dat', 'a')
            writer = csv.writer(k)
        
            junt = [user, resp]
            writer.writerow(junt)
        
            k.close()
        else:
            qbrl()
            print('Ok então ;---;')
            qbrl()
            sleep(1)
            print('Se você deseja ver os comandos digite "mostrar comandos".')
            
    #se estiver no banco ele vai dar a resposta
    
    else:
        
        for obj in bd:
            
            if obj[0] in user:
                print(obj[1])
            else:
                pass