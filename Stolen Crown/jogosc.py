from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import*

# Verifica se o inimigo colidiu com as linhas de subida ou descida
def colidiu(x, c1):
    if (x.collided(c1['p1'])):
        x.direction = 'cima'
        return 0, -0.2
    elif (x.collided(c1['p2'])):
        x.direction = 'baixo'
        return 0, 0.2
    elif (x.collided(c1['p3'])):
        x.direction = 'cima'
        return 0, -0.2
    elif (x.collided(c1['p4'])):
        x.direction = 'cima'
        return 0, -0.2
    else:
        x.direction = 'esquerda'
        return -0.2, 0

# Atualiza a posição dos soldados na tela, pelo caminho 1
def atualizainimigo(lista1, lista2, c1, c2):
    for i in lista1:
        andax, anday = colidiu(i, c1)
        i.move_x(andax)
        i.move_y(anday)
    for i in lista2:
        andax, anday = colidiu(i, c2)
        i.move_x(andax)
        i.move_y(anday)


# Desenha os inimigos da lista se ainda não chegaram ao fim
def desenhainimigos(lista1, lista2, direcao):
    cont = 0
    for i in lista1:
        if(i.y + i.height < 0):
            lista1.remove(i)
            cont += 1
        elif(i.direction == 'esquerda'):
            direcao['esquerda'].x = i.x
            direcao['esquerda'].y = i.y
            direcao['esquerda'].draw()
        elif (i.direction == 'cima'):
            direcao['cima'].x = i.x
            direcao['cima'].y = i.y
            direcao['cima'].draw()
        else:
            direcao['baixo'].x = i.x
            direcao['baixo'].y = i.y
            direcao['baixo'].draw()

    for i in lista2:
        if(i.y + i.height < 0):
            lista2.remove(i)
            cont += 1
        elif(i.direction == 'esquerda'):
            direcao['esquerda'].x = i.x
            direcao['esquerda'].y = i.y
            direcao['esquerda'].draw()
        elif (i.direction == 'cima'):
            direcao['cima'].x = i.x
            direcao['cima'].y = i.y
            direcao['cima'].draw()
        else:
            direcao['baixo'].x = i.x
            direcao['baixo'].y = i.y
            direcao['baixo'].draw()
    return cont

def FASE(dicio):
    # Inicialização da janela e background estático
    janela = Window(1024, 640)
    background = GameImage("Imagens/Jogo/background2.jpg")
    janela.set_title("Stolen Crown")

    # Inicialização do teclado e do mouse
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    # Inicicialização de variáveis importantes
    vidas = 10
    cronometro = 0
    qtddeinimigos = 0
    wavest = 0
    wavessv = 0
    listadesoldados1 = []
    listadesoldados2= []

    # Inicialização dos soldados verdes
    svesquerda = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
    svcima = Sprite("Imagens/Jogo/soldadoverdecima.png", 1)
    svbaixo = Sprite("Imagens/Jogo/soldadoverdebaixo.png", 1)

    # Dicionário com a direção dos soldados verdes
    svdirecao = {'esquerda': svesquerda, 'cima': svcima, 'baixo': svbaixo}

    # Inicialização dos soldados pratas
    spesquerda = Sprite("Imagens/Jogo/soldadoprataesquerda.png", 1)
    spcima = Sprite("Imagens/Jogo/soldadopratacima.png", 1)
    spbaixo = Sprite("Imagens/Jogo/soldadopratabaixo.png", 1)

    # Dicionário com a direção dos soldados pratas
    spdirecao = {'esquerda': spesquerda, 'cima': spcima, 'baixo': spbaixo}

    # Inicialização dos pontos de mudança do caminho 1
    p1 = GameObject()
    p1.x = 672
    p1.y = 160
    p1.width = 1
    p1.height = 64
    p2 = GameObject()
    p2.x = 480
    p2.y = 96
    p2.width = 1
    p2.height = 128
    p3 = GameObject()
    p3.x = 288
    p3.y = 224
    p3.width = 1
    p3.height = 64
    p4 = GameObject()
    p4.x = 96
    p4.y = 0
    p4.width = 1
    p4.height = 224

    # Inicialização dos pontos de mudança do caminho 2
    p5 = GameObject()
    p5.x = 800
    p5.y = 416
    p5.width = 1
    p5.height = 288
    p6 = GameObject()
    p6.x = 672
    p6.y = 352
    p6.width = 1
    p6.height = 64
    p7 = GameObject()
    p7.x = 288
    p7.y = 224
    p7.width = 1
    p7.height = 256
    p8 = GameObject()
    p8.x = 96
    p8.y = 0
    p8.width = 1
    p8.height = 224

    # Dicionário de caminhos
    caminho1 = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4}
    caminho2 = {'p1': p5, 'p2': p6, 'p3': p7, 'p4': p8}
    caminhos = {'1': caminho1, '2': caminho2}

    # GameLoop
    while(not teclado.key_pressed("esc")):

        # Atualização do cronômetro
        cronometro += janela.delta_time()

        # Criação da lista de soldados
        if(cronometro >= 1.2 and wavest < dicio['wavestotais'] and wavessv < dicio['wavessv'] and qtddeinimigos < dicio['soldadosverdes']):
            cronometro = 0
            soldadoverde = Sprite("Imagens/Jogo/soldadoverdeesquerda.png",1)
            soldadoverde.x = 1024
            soldadoverde.y = 160
            soldadoverde.direction = 'esquerda'

            listadesoldados1.append(soldadoverde)

            soldadoverde1 = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
            soldadoverde1.x = 800
            soldadoverde1.y = 640
            soldadoverde1.direction = 'cima'

            listadesoldados2.append(soldadoverde1)

            qtddeinimigos += 1
        elif(qtddeinimigos == dicio['soldadosverdes'] and cronometro >= 15):
            qtddeinimigos = 0
            wavest += 1
            wavessv += 1

        # Atualização da posição dos inimigos
        atualizainimigo(listadesoldados1, listadesoldados2, caminho1, caminho2)

        # Desenho na tela
        background.draw()

        # Desenho dos inimigos e atualização da contagem de vidas
        vidas -= desenhainimigos(listadesoldados1, listadesoldados2, svdirecao)
        janela.update()

    # Retorna 0 para voltar ao menu no caso ESC
    return 0

def jogo(fase):

    #Inicialização da janela e background estático
    janela = Window(1024, 640)
    background = GameImage("Imagens/Jogo/background2.jpg")
    janela.set_title("Stolen Crown")

    # Inicialização do teclado e do mouse
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    # Dicionário de fases
    fase1 = {'wavestotais': 5, 'wavessv': 5, 'soldadosverdes': 5}
    fase2 = {'wavestotais': 7, 'wavessv': 5, 'soldadosverdes': 5, 'wavessp': 2, 'soldadospratas': 3}
    fase3 = {'wavestotais': 10, 'wavessv': 5, 'soldadosverdes': 7, 'wavessp': 5, 'soldadospratas': 5}

    while (not teclado.key_pressed("esc")):
        # Deixa o jogo pausado até clicarem espaço e direciona para a fase escolhida
        if(teclado.key_pressed("space") and fase == 1):
            FASE(fase1)
        elif(teclado.key_pressed("space") and fase == 2):
            FASE(fase2)
        elif(teclado.key_pressed("space") and fase == 3):
            FASE(fase3)
        # Desenho na tela
        background.draw()
        janela.draw_text("Pressione espaço para iniciar.", 150, 280, 50, [255, 255, 255], "Arial", True)
        janela.update()
        # Retorna 0 para voltar ao menu no caso ESC
    return 0

