import random
import math
import os
import time

salas = []
mapa = []
player = "X"
op = 1
tamanho = 1

def Menu():
    global tamanho
    global op
    print("\n-----  GAY's ADVENTURES -----\n")
    op = int(input("Preparado para aventura?\n\n0 - sair  1 - jogar  2 - como jogar\n"))
    if(op==1):
        dificuldade = int(input("\nEscolha o dificuldade inicial da dungeon:\n\n1 - facil  2 - medio  3 - dificil\n"))
        if(dificuldade==1):
            tamanho = 3
        elif(dificuldade==2):
            tamanho = 5
        elif(dificuldade==3):
            tamanho = 7
    elif(op==2):
        print("O jogo consiste em se mover pela Dungeon e ganhar pontos dados pela salas andadas. As salas possuem pontos variados, normalmente salas mais dificis darão mais pontos. Para avançar para o proximo andar da Dungeon deve encontrar a sala com maior pontos.0")
        aux = input("Voltar para o menu ->\n")
        Menu()



def GerarMapa(tamanho):
    global salas
    global mapa
    global player
    
    for i in range(tamanho):
        linha = []
        l = []
        for j in range(tamanho):
            l.append(0)
            linha.append(random.randint(1,9))
        mapa.append(l)
        salas.append(linha)
    posicao = math.ceil((tamanho/2)-1)
    mapa[posicao][posicao] = player
    salas[posicao][posicao] = 0

def MostrarMapa():

    os.system('cls') or None

    print("\n----- MAP -----")
    for i in range(tamanho):
        print(mapa[i])    
    print("---------------\n")

def Mover():
    global mapa
    global salas
    global player
    global tamanho
    tamanho = len(mapa)
    for i in range(tamanho):
        for j in range(tamanho):
            if(mapa[i][j]=="X"):
                x = j
                y = i
    direcao = int(input("\nQual direção?\n\n1 - NORTE  2 - SUL  3 - LESTE  4 - OESTE\n"))
    if(direcao==1):
        if(y>0):
            mapa[y-1][x] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
    elif(direcao==2):
        if(y+1<tamanho):
            mapa[y+1][x] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
        
    elif(direcao==3):
        if(x+1<tamanho):
            mapa[y][x+1] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
        
        
    elif(direcao==4):
        if(x>0):
            mapa[y][x-1] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
    
        
        



Menu()
GerarMapa(tamanho)

while(op!=0):
    MostrarMapa()    
    op = int(input("O que quer fazer?\n\n0 - encerrar  1 - mover\n"))
    if(op==1):        
        Mover()
    else:
        print(...)

print("\nGAME OVER\n")