#-*-coding:utf8;-*-
	
#arquivo responsavel por guardar definições

import csv

def nome():
    
    n = open('/sdcard/XhatbotX/bd/name.dat', 'r')
    name = n.readline()
    n.close()
    
    if name == '0':
        
        print('Olá meu nome é Joseph!\n')
        print('Qual é o seu?')
        nom = str(input('>>: '))
        
        if nom == '0':
            nom = 'default'
        
        k = open('/sdcard/XhatbotX/bd/name.dat', 'w')
        k.write(nom)
        
        print(' ')
        print(f'Prazer lhe conhecer {nom}!')
        
    else:
        print(f'Olá {name}!')
    
def openBd(cam):
    bd = []

    f = open(f'/sdcard/XhatbotX/bd/{cam}','r')

    leitor = csv.reader(f)

    for l in leitor:
        bd.append(l)
    
    f.close()
    return bd