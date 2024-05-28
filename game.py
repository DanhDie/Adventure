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

inventario = ["Pocao de cura", "Escudo", "Bussola de escadas", "Bussola de desafios", "Bussola de tesouros"]
pontos = 0
tipo=0
#Variáveis de classe
classe = ""
vida = 0
vidamax = 0
dt = 0
escudo = 0
esquiva = 0
modificador = 0 
dadoMaximo=8
inteligencia = 0

#Variáveis de combate
vidaInimigo = 0 
dtInimigo = 0
danoInimigo = 0
modificadorInimigo=0
#Menu

def ApagarCs():
    os.system('cls') or None

def RodarDado(lados,modificador):
    numero = random.randint(1,lados)+modificador
    return numero

def Menu():
    global tamanho
    global dificuldade
    global op
    global vida, dt, esquiva, modificador, inteligencia, vidamax
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
            vidamax=50
            vida = vidamax-10
            dt=12
            modificador=4
            inventario.append("Espada")
        elif(classe==2):
            vidamax=30
            vida = vidamax
            dt=16
            esquiva = 4
            inventario.append("Adaga")
        elif(classe==3):
            vidamax=25
            vida = vidamax
            dt=14
            inteligencia = 4
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
           
def ProximoAndar():
    global tamanho
    tamanho+=1
    ApagarCs()
    GerarMapa(tamanho)
    print("PARABENS!!!\nAchou uma escada e desce para o proximo andar...")
    MostrarMapa()
    time.sleep(3)


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

#Sessao de inventario e itens
def MostrarInventario():
    global inventario
    print("\nVocê possui:",)
    for i in range(len(inventario)):
        print(i,"-",inventario[i])
    y = int(input("\n1 - sair  2 - Usar item\n"))
    if(y==2):
        aux = int(input("\nDigite o numero do item que deseja usar ->\n"))
        if(aux!=''):
            if(aux>len(inventario) or aux<0):
                MostrarInventario()
            else:
                UsarItem(aux)
def UsarItem(item):
    global inventario
    match inventario[item]:
        case "Pocao de cura":
            PocaoVida(item)
        case "Escudo":
            Escudo(item)
        case "Bussola de desafios":
            RevelarDes(item)
        case "Bussola de tesouros":
            RevelarTes(item)
        case "Bussola de escadas":
            RevelarEsc(item)
        case _:
            print("Nada a se fazer...")

def PocaoVida(id):
    global vida, vidamax,inventario
    if(vidamax==vida):
        ApagarCs()
        print("\nA vida está cheia!\n")
        time.sleep(3)
    else:
        cura=RodarDado(10,5)
        vida += cura
        if(vida>vidamax):
            vida = vidamax
        inventario.pop(id)
        ApagarCs()
        print("\nCurou", cura, "Pontos de vida!1\n")
        time.sleep(3)

def Escudo(id):
    global dt, escudo
    if(escudo>0):
        ApagarCs()
        print("Escudo ja equipado!")
        time.sleep(3)
    else:
        ApagarCs()
        print("Escudo foi equipado!")
        print("\n+2 de armadura ")
        dt+=2
        time.sleep(3)
        escudo+=1
    
def RevelarEsc(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==9):
                mapa[i][j]=9
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam as escadas no seu andar...")
    print("Procure pelos NOVES")
    time.sleep(3)

def RevelarTes(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==7):
                mapa[i][j]=7
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam os tesouros no seu andar...")
    print("Procure pelos SETES")
    time.sleep(3)

def RevelarDes(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==4):
                mapa[i][j]=4
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam os desafios no seu andar...")
    print("Procure pelos QUATROS")
    time.sleep(3)

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

#Nova seção de funções para combate
def RolandoDados(vidaAtacado, dtAtacado, dadoMaximo, modificador, dif):
    global vida, vidaInimigo

    dado=random.randint(1,20)
    print("\nRolando dado de ataque...")
    time.sleep(1)
    print("Dado: %d!"%(dado))
    input("\nEnter para continuar ->\n")

    if(dado==20):
        print("\nDano crítico!")

        dado=random.randint(1,dadoMaximo)
        print("%d de dano no primeiro ataque!"%(dado))
        vidaAtacado=vidaAtacado-dado
        dado=random.randint(1,danoInimigo)
        print("%d de dano no segundo ataque!"%(dado))
        time.sleep(2)

        return vidaAtacado-dado
        
    elif(dado>=dtAtacado):
        dado=random.randint(1,dadoMaximo)+modificador
        print("Rolando dado de dano...")
        time.sleep(1)
        print("%d de dano!"%(dado))

        return vidaAtacado-dado
    
    elif(dado==1):
        print("\nDesastre!")
        dado=random.randint(1,8)+modificador
        time.sleep(1)
        print("%d de dano em si mesmo!"%(dado))
        if(dif==0):
            vida=vida-dado
        elif(dif==1):
            vidaInimigo=vidaInimigo-dado
        
        return
        
    else:
        print("\nErrou o ataque.")
        time.sleep(2)

def AtaqueInimigo():
    global vida, dt, danoInimigo, modificadorInimigo, vidaInimigo
    ApagarCs()
#Outro exemplo de ASCII art super duper importante para imersão do jogador
    print("---------------------------------------------------------------------------------------------------")
    print("""                     ______
                  .-"      "-.
                 /            \
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------`""")
    print("---------------------------------------------------------------------------------------------------")
    time.sleep(1)

    print("\nO inimigo tenta te atacar...")
    vida=RolandoDados(vida, dt, danoInimigo, modificadorInimigo, 1)

    input("\nEnter para continuar ->\n")

def Atacar():
    global vidaInimigo, dtInimigo, dadoMaximo, modificador

    vidaInimigo=RolandoDados(vidaInimigo, dtInimigo, dadoMaximo, modificador, 0)

    input("\nEnter para continuar ->\n")

def Fugir():
    global classe, esquiva
    print("\nVocê tenta fugir...")

    destreza=random.randint(1,20)+esquiva
    print("\nVocê tirou %d!"%(destreza))

    destrezaInimigo=random.randint(1,20)
    print("\nRolando dados do inimigo...")
    time.sleep(1)
    print("\nO inimigo tirou %d!"%(destrezaInimigo))

    if(destreza>destrezaInimigo):
        print("\nVocê escapa da batalha!")
        vidaInimigo=0
    else:
        print("\nParece que você não foi rápido o suficiente...")
        time.sleep(2)
        AtaqueInimigo()

    input("\nEnter para continuar ->\n")
    return vidaInimigo

def CriarInimigo():
    global vidaInimigo, dtInimigo, danoInimigo, modificadorInimigo

    vidaInimigo=random.randint(4,6)*random.randint(1,3)
    dtInimigo=random.randint(10,12)+random.randint(1,3)
    danoInimigo=random.randint(1,3)+5
    modificadorInimigo=random.randint(0,1)
    
def MenuCombate():
    global vidaInimigo, dtInimigo, vida, classe
    ApagarCs()

#ASCII art super importante para a imersão do jogo
#A primeiro é uma espada
    if(classe==1):
        print("---------------------------------------------------------------------------------------------------")
        print(""" _          /~~>________________________________________
/ \////////|   \..................................~~~~~---_
\_/\\\\\\\\|   /__________________________________-----~~~
            \__>""")
        print("\nDano máximo: 12")
#Essa segunda é uma adaga
    if(classe==2):
        print("---------------------------------------------------------------------------------------------------")
        print(""" ,-.  ,                     , ,.......____
(   ` |    @                | |               ...---...___
 `-.  |,-. , .-.-. :-..-. .-| |                           ..--..__
.   ) |  | | | | | |  | | | | |                                   .-._
 `-'  '  ' ' ' ' ' '  `-' `-` `---------------------------------------`""")
        print("---------------------------------------------------------------------------------------------------")
        print("\nDano máximo: 8")
#E aqui a gente tem..... É meio que o simbolo dos médico, mas virou um cajado. Tem um parecido no Genshin, shhhhhh
    if(classe==3):
        print("---------------------------------------------------------------------------------------------------")
        print(""" _____  _  _____
(___  \( )/  ___)
  (___ | | ___)
   /")`| |'("\
  | |  | |  | |
   \ \_| |_/ /
    `._!' _.'
      / .'\
     | / | |
      \|/ /
       /.<
      (| |)
       | '
       | |
       `-'""")
        print("\nDano máximo: 8")
        
    print("Vida:",vida)
    print("---------------------------------------------------------------------------------------------------")

    op=int(input("\nO que você deseja fazer?\n1 - Atacar  2 - Fugir \n"))
    if(op==1):
        Atacar(vidaInimigo, dtInimigo)
    elif(op==2):
        vidaInimigo=Fugir()
    else:
        print(...)

def Combate():
    global vidaInimigo, dtInimigo, vida
    print("Você entrou em uma batalha! É seu turno, se prepare\n")
    input("\nEnter para continuar ->\n")
    
    while True:
        MenuCombate()

        if not (vidaInimigo>0):
            break

        print("É a vez do inimigo")
        time.sleep(2)
        AtaqueInimigo()

        if(vida<=0):
            return 0
        
    print("\nVocê venceu a batalha!")
    exp=0
    if(dtInimigo>12):
        exp+=35
    else:
        exp+=20
    
    print("Você recebeu %e pontos!"%(exp))
    AddPontos(exp)
    input("\nEnter para continuar ->\n")

#Armadilhas
def Armadilha():
    global vida, dt, vidaInimigo, dtInimigo, danoInimigo, modificadorInimigo, dadoMaximo, modificador
    print("\nUm baú feito de madeira, com extremidades reforçadas a aço e uma fechadura enferrujada, aparece diante de você")
    op=int(input("\nO que deseja fazer?\n1 - Abrir o baú 2 - Atacar 3 - Sair"))

    if(op==1):
        print("O baú revela.... UM MÍMICO, ele te ataca de surpresa")
        vida=RolandoDados(vida, dt, danoInimigo, modificadorInimigo, 1)

        if(vida<=0):
            return 0
        
        input("\nEnter para continuar ->\n")
        Combate()
    if(op==2):
        print("Sua intuição estava correta, era um MÍMICO!")
        vidaInimigo=RolandoDados(vidaInimigo, dtInimigo, dadoMaximo, modificador, 0)
        input("\nEnter para continuar ->\n")
        Combate()
    

Menu()
GerarMapa(tamanho)

while(op!=0 and vida>0):
    for i in range(tamanho):
        for j in range(tamanho):
            if(mapa[i][j]=="X"):
                x = j
                y = i
    ApagarCs()
    MostrarPontos()
    MostrarMapa()

    if(salas[y][x]==9):
        PontoSala()
        ProximoAndar()
        

    if(salas[y][x]==8):
        PontoSala()
        CriarInimigo()
        op=Combate()
        salas[y][x]=1

    if(salas[y][x]==7):
        PontoSala()
        CriarInimigo()
        op=Armadilha()
        salas[y][x]=1

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