import random
import math
import os
import time 

salas = []
mapa = []
player = "X"
op = 1
tamanho = 1
dificuldade = 0
#Variáveis de combate
dado = 0
vida = 0
dt = 0
exp=0
classe = ""
inventario = []
pontos = 0

#Menu

def ApagarCs():
    os.system('cls') or None

def Menu():
    global tamanho
    global dificuldade
    global op
    global vida, dt
    ApagarCs()
    print("\n-----  GAY's ADVENTURES -----\n")
    op = int(input("Preparado para aventura?\n\n0 - sair  1 - jogar  2 - como jogar\n"))
    if(op==1):
        ApagarCs()
        dificuldade = int(input("\nEscolha o dificuldade inicial da dungeon:\n\n1 - facil  2 - medio  3 - dificil\n"))
        if(dificuldade==1):
            tamanho = 3
        elif(dificuldade==2):
            tamanho = 5
        elif(dificuldade==3):
            tamanho = 7
        
        ApagarCs()
        classe = int(input("\nEscolha sua classe \n\n1 - Barbaro (+DANO +VIDA)  2 - Ladino (+ESQUIVA +TESOUROS)  3 - Feiticeiro (+INTELIGENCIA +MAGIA)\n"))
        if(classe==1):
            vida=50
            dt=12
            inventario.append("Espada")
        elif(classe==2):
            vida=30
            dt=16
            inventario.append("Adaga")
        elif(classe==3):
            vida=25
            dt=14
            inventario.append("Cajado")
        
        

    elif(op==2):
        ApagarCs()
        print("O jogo consiste em se mover pela Dungeon e ganhar pontos dados pela salas andadas. As salas possuem pontos variados, normalmente salas mais dificis darão mais pontos. Para avançar para o proximo andar da Dungeon deve encontrar a sala com maior pontos.0")
        aux = input("Voltar para o menu ->\n")
        Menu()

def GerarMapa(tamanho):
    global salas
    global mapa
    global player
    salas = []
    mapa = []
    
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

    saida=0
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==9):
                saida=1
    if(saida==0):
        GerarMapa(tamanho)
           

def MostrarMapa():   

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
    PontoSala()
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

#Nova seção de funções para combate
def AtaqueInimigo():
    global dificuldade
    global vida, dt

    if(dificuldade==1):
        print("\nO inimigo tenta te atacar...")
        dado=random.randint(1,20)

        print("\nRolando dado de ataque...")
        time.sleep(1)
        print("O inimigo tirou %d!"%(dado))

        if(dado>=dt):
            print("\nEle acerta!")
            dado=random.randint(1,4)
            time.sleep(1)
            print("Você toma %d de dano!"%(dado))

            vida=vida-dado
            time.sleep(2)
        else:
            print("\nEle erra!")
            time.sleep(2)

    elif(dificuldade==2):
        print("\nO inimigo tenta te atacar...")
        dado=random.randint(1,20)

        print("\nRolando dado de ataque...")
        time.sleep(1)
        print("O inimigo tirou %d!"%(dado))

        if(dado>=dt):
            print("\nEle acerta!")
            dado=random.randint(1,6)
            time.sleep(1)
            print("Você toma %d de dano!"%(dado))

            vida=vida-dado
            time.sleep(2)
        else:
            print("\nEle erra!")
            time.sleep(2)

    elif(dificuldade==3):
        print("\nO inimigo tenta te atacar...")
        dado=random.randint(1,20)

        print("\nRolando dado de ataque...")
        time.sleep(2)
        print("O inimigo tirou %d!"%(dado))

        if(dado>=dt):
            print("\nEle acerta!")
            dado=random.randint(1,8)
            time.sleep(2)
            print("Você toma %d de dano!"%(dado))

            vida=vida-dado
            time.sleep(2)
        else:
            print("\nEle erra!")
            time.sleep(2)

def Atacar(vidaInimigo, dtInimigo):
    global dado
    global exp
    global vida

    dado=random.randint(1,20)
    print("\nRolando dado de ataque...")
    time.sleep(1)
    print("Você tirou %d!"%(dado))
    
    if(dado>=dtInimigo):
        if(dado==20):
            print("\nDano crítico! Você ganhou!")
            vidaInimigo=0
            time.sleep(2)
            return vidaInimigo
        
        input("\nPressione enter para dar o dano\n")

        dado=random.randint(1,8)
        print("Rolando dado de dano...")
        time.sleep(2)
        print("Você tirou %d!"%(dado))
        time.sleep(2)

        vidaInimigo=vidaInimigo-dado
        return vidaInimigo
    elif(dado==1):
        print("\nDesastre! Você acertou a si mesmo")
        dado=random.randint(1,8)
        vida=vida-dado
        time.sleep(2)
        
    else:
        print("\nVocê errou o ataque.")
        time.sleep(2)

def Fugir():
    print("\nVocê tenta fugir...")
    input("Faça um teste de desestreza, aperte enter")

    destreza=random.randint(1,20)
    print("\nVocê tirou %d!"%(destreza))
    destrezaInimigo=random.randint(1,20)
    print("O inimigo tirou %d!"%(destrezaInimigo))

    if(destreza>destrezaInimigo):
        print("\nVocê escapa da batalha.")
        vidaInimigo=0
        time.sleep(2)
        return vidaInimigo
    else:
        print("\nParece que você não foi rápido o suficiente...")
        time.sleep(2)
        AtaqueInimigo()

def CriarInimigo():
    global dificuldade
    global vidaInimigo, dtInimigo

    if(dificuldade==1):
            vidaInimigo=random.randint(8,10)
            dtInimigo=random.randint(10,12)
    elif(dificuldade==2):
        vidaInimigo=random.randint(10,12)
        dtInimigo=random.randint(12,14)
    elif(dificuldade==3):
        vidaInimigo=random.randint(12,16)
        dtInimigo=random.randint(14,16)

#Sessao de inventario e itens
def MostrarInventario():
    global inventario
    print("\nVocê possui:",)
    for i in range(len(inventario)):
        print(i,"-",inventario[i])
    aux = input("\nEnter para retornar ->\n")

#Estatiticas

def MostrarEstatisticas():
    global dt,vida
    os.system('cls') or None

    print("\n--- STATUS ---")
    print("   HP =",vida)
    print("  ARMOR =",dt)    
    print("--------------\n")

    aux = input("\nEnter para retornar ->\n")

#Pontuacao

def MostrarPontos():
    global pontos
    print("  -- SCORE --")
    print("      ",pontos,"  ")
    print("  -----------")

def AddPontos(pt):
    #pt = quatidade de pontos a ser atribuido
    global pontos
    pontos += pt

def PontoSala():
    global salas
    AddPontos(salas[y][x])

Menu()
GerarMapa(tamanho)

while(op!=0):
#Nova seção para combate
    for i in range(tamanho):
        for j in range(tamanho):
            if(mapa[i][j]=="X"):
                x = j
                y = i
    ApagarCs()
    MostrarPontos()
    MostrarMapa()

    if(salas[y][x]==2):
        print("Você entrou em uma batalha! Você ataca primeiro, se prepare\n")

        CriarInimigo()

        rodada=1
        while(vidaInimigo>0):
            if(rodada>1):
                print("\nÉ a vez do inimigo!")
                AtaqueInimigo()


            op=int(input("O que você deseja fazer?\n1 - Atacar  2 - Fugir\n"))
            if(op==1):
                Atacar(vidaInimigo, dtInimigo)
            elif(op==2):
                vidaInimigo=Fugir()
            else:
                print(...)

            rodada=rodada+1
        
        print("\nVocê venceu a batalha!")
        if(dificuldade==1):
            print("Você recebe 20 pontos de experiência")
            exp=exp+20
        elif(dificuldade==2):
            print("Você recebe 35 pontos de experiência")
            exp=exp+35
        elif(dificuldade==3):
            print("Você recebe 50 pontos de experiência")
            exp=exp+50
#

    else:    
        op = int(input("O que quer fazer?\n\n0 - Encerrar  1 - Mover  2 - Inventario  3 - Status\n"))
        if(op==1):    
            Mover()
        if(op==2):    
            MostrarInventario()
        if(op==3):    
            MostrarEstatisticas()
        else:
            print(...)

print("\nGAME OVER\n")