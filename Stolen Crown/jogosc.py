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

    # Caminho 1
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
    # Caminho 2
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

    # Inicializa e posiciona os slots
    slotarma = Sprite("Imagens/Jogo/slotarma.png")
    slotarma.x = 0
    slotarma.y = 64
    slotarma1 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma1.x = 0
    slotarma1.y = 128
    slotarma2 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma2.x = 0
    slotarma2.y = 192
    slotarma3 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma3.x = 64
    slotarma3.y = 256
    slotarma4 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma4.x = 128
    slotarma4.y = 256
    slotarma5 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma5.x = 192
    slotarma5.y = 256
    slotarma6 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma6.x = 192
    slotarma6.y = 320
    slotarma7 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma7.x = 192
    slotarma7.y = 384
    slotarma8 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma8.x = 192
    slotarma8.y = 448
    slotarma9 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma9.x = 256
    slotarma9.y = 512
    slotarma10 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma10.x = 320
    slotarma10.y = 512
    slotarma11 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma11.x = 384
    slotarma11.y = 512
    slotarma12 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma12.x = 448
    slotarma12.y = 512
    slotarma13 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma13.x = 512
    slotarma13.y = 512
    slotarma14 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma14.x = 576
    slotarma14.y = 512
    slotarma15 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma15.x = 640
    slotarma15.y = 512
    slotarma16 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma16.x = 704
    slotarma16.y = 512
    slotarma17 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma17.x = 896
    slotarma17.y = 512
    slotarma18 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma18.x = 896
    slotarma18.y = 448
    slotarma19 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma19.x = 896
    slotarma19.y = 384
    slotarma20 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma20.x = 896
    slotarma20.y = 320
    slotarma21 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma21.x = 896
    slotarma21.y = 256
    slotarma22 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma22.x = 832
    slotarma22.y = 256
    slotarma23 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma23.x = 768
    slotarma23.y = 256
    slotarma24 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma24.x = 704
    slotarma24.y = 256
    slotarma25 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma25.x = 640
    slotarma25.y = 256
    slotarma26 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma26.x = 576
    slotarma26.y = 320
    slotarma27 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma27.x = 512
    slotarma27.y = 320
    slotarma28 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma28.x = 448
    slotarma28.y = 320
    slotarma29 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma29.x = 384
    slotarma29.y = 320
    slotarma30 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma30.x = 576
    slotarma30.y = 192
    slotarma31 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma31.x = 896
    slotarma31.y = 64
    slotarma32 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma32.x = 832
    slotarma32.y = 64
    slotarma33 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma33.x = 768
    slotarma33.y = 64
    slotarma34 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma34.x = 704
    slotarma34.y = 0
    slotarma35 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma35.x = 640
    slotarma35.y = 0
    slotarma36 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma36.x = 576
    slotarma36.y = 0
    slotarma37 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma37.x = 512
    slotarma37.y = 0
    slotarma38 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma38.x = 448
    slotarma38.y = 0
    slotarma39 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma39.x = 384
    slotarma39.y = 128
    slotarma40 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma40.x = 384
    slotarma40.y = 64
    slotarma41 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma41.x = 320
    slotarma41.y = 64
    slotarma42 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma42.x = 256
    slotarma42.y = 64
    slotarma43 = Sprite("Imagens/Jogo/slotarma.png")
    slotarma43.x = 192
    slotarma43.y = 64

    # Cria uma lista com os slots inicializados
    listaslots = {slotarma, slotarma1, slotarma2, slotarma3, slotarma4, slotarma5, slotarma6, slotarma7, slotarma8, slotarma9, slotarma10, slotarma11, slotarma12, slotarma13, slotarma14, slotarma15, slotarma16, slotarma17, slotarma18, slotarma19, slotarma20, slotarma20, slotarma21, slotarma22, slotarma23, slotarma24, slotarma25, slotarma26, slotarma27, slotarma28, slotarma29, slotarma30, slotarma31, slotarma32, slotarma33, slotarma34, slotarma35, slotarma36, slotarma37, slotarma38, slotarma39, slotarma40, slotarma41, slotarma42, slotarma43}

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

        # Desenha slots
        for i in listaslots:
            i.draw()

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
