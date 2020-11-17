from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import*

#Atualiza a posição dos soldados na tela, pelo caminho 1
def atualizainimigo(lista, c1):
    for i in lista:
        print(i.x, i.y)
        if(not i.collided(c1['p1'])):
            i.x -= 0.2
            i.direction = 'esquerda'
        elif(not i.collided(c1['p2'])):
            i.y -= 0.2
            i.direction = 'cima'
        elif(not i.collided(c1['p3'])):
            i.x -= 0.2
            i.direction = 'esquerda'
        elif(not i.collided(c1['p4'])):
            i.y += 0.2
            i.direction = 'baixo'




#Desenha os inimigos da lista se ainda não chegaram ao fim
def desenhainimigos(lista, svdirecao, vidas):
    for i in lista:
        if(i.y + i.height < 0):
            lista.remove(i)
            vidas -= 1
        elif(i.direction == 'esquerda'):
            svdirecao['esquerda'].x = i.x
            svdirecao['esquerda'].y = i.y
            svdirecao['esquerda'].draw()
        elif(i.direction == 'direita'):
            svdirecao['direita'].x = i.x
            svdirecao['direita'].y = i.y
            svdirecao['direita'].draw()
        elif (i.direction == 'cima'):
            svdirecao['cima'].x = i.x
            svdirecao['cima'].y = i.y
            svdirecao['cima'].draw()
        else:
            svdirecao['baixo'].x = i.x
            svdirecao['baixo'].y = i.y
            svdirecao['baixo'].draw()


def jogo(dificuldade):

    #Inicialização da janela e background estático
    janela = Window(1024, 640)
    background = GameImage("background2.jpg")
    janela.set_title("Stolen Crown")

    #Inicialização do teclado e do mouse
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    #Inicicialização de variáveis importantes
    vidas = 10
    cronometro = 0
    qtddeinimigos = 0
    listadesoldados = []

    # Inicializa os soldados verdes
    svdireita = Sprite("soldadoverdedireita.png", 1)
    svesquerda = Sprite("soldadoverdeesquerda.png", 1)
    svcima = Sprite("soldadoverdecima.png", 1)
    svbaixo = Sprite("soldadoverdebaixo.png", 1)

    # Dicionário com a direção dos soldados verdes
    svdirecao = {'direita': svdireita, 'esquerda': svesquerda, 'cima': svcima, 'baixo': svbaixo}

    # Inicializa pontos de mudança
    p1 = GameObject()
    p1.x = 672
    p1.y = 160
    p1.width = 5
    p1.height = 5
    p2 = GameObject()
    p2.x = 672
    p2.y = 96
    p2.width = 5
    p2.height = 5
    p3 = GameObject()
    p3.x = 480
    p3.y = 96
    p3.width = 5
    p3.height = 5
    p4 = GameObject()
    p4.x = 480
    p4.y = 224
    p4.width = 5
    p4.height = 5
    p5 = GameObject()
    p5.x = 288
    p5.y = 224
    p5.width = 10
    p5.height = 10
    p6 = GameObject()
    p6.x = 288
    p6.y = 160
    p6.width = 10
    p6.height = 10
    p7 = GameObject()
    p7.x = 96
    p7.y = 160
    p7.width = 10
    p7.height = 10


    # Dicionário do caminho 1
    caminho1 = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6, 'p7': p7}

    #GameLoop
    while(not teclado.key_pressed("esc")):

        #Atualização do cronômetro
        cronometro += janela.delta_time()

        #Criação da lista de soldados do caminho 1
        if(cronometro >= 1.2 and qtddeinimigos < 10):
            cronometro = 0
            soldadoverde = Sprite("soldadoverdeesquerda.png",1)
            soldadoverde.y = 160
            soldadoverde.x = 1024
            soldadoverde.direction = 'esquerda'
            listadesoldados.append(soldadoverde)
            qtddeinimigos += 1

        #Atualização da posição dos inimigos
        atualizainimigo(listadesoldados, caminho1)

        #Desenho na tela
        background.draw()
        desenhainimigos(listadesoldados, svdirecao, vidas)
        janela.update()
    #Retorna 0 para voltar ao menu no caso ESC
    return 0