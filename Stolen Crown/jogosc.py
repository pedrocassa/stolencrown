from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *

# Verifica a quantidade de vidas e se o jogador perdeu
def gameover(vidas, janela):
    if(vidas == 0):
        janela.draw_text("Game Over!", 230, 250, 100, [255, 255, 255], "Arial", True)
        janela.update()
        janela.delay(3000)
        return True

# Verifica se chegou ao final da lista fase
def victory(fase, x, soldados, janela):
    if (x == len(fase) and soldados == []):
        janela.draw_text("Victory", 350, 250, 100, [255, 255, 255], "Arial", True)
        janela.update()
        janela.delay(3000)
        return True

# Pausa o jogo caso o jogador clique no enter e despausa quando aperta space
def pausado(janela, background, teclado):
    pause = True
    while (pause == True):
        if (teclado.key_pressed("space")):
            pause = False
        background.draw()
        janela.draw_text("Pressione espaço para continuar.", 110, 280, 50, [255, 255, 255], "Arial", True)
        janela.update()
    return pause

# Verifica se o inimigo colidiu com as linhas de subida ou descida
def colidiu(x, c1):
    if (x.collided(c1['p1'])):
        x.direction = 'cima'
        return 0, -30
    elif (x.collided(c1['p2'])):
        x.direction = 'baixo'
        return 0, 30
    elif (x.collided(c1['p3'])):
        x.direction = 'cima'
        return 0, -30
    elif (x.collided(c1['p4'])):
        x.direction = 'cima'
        return 0, -30
    else:
        x.direction = 'esquerda'
        return -30, 0

# Atualiza a posição dos soldados na tela, pelo caminho 1
def atualizainimigo(soldados, c1, c2, janela):
    for i in soldados:
        if(i.path == 1):
            andax, anday = colidiu(i, c1)
            i.move_x(andax * janela.delta_time())
            i.move_y(anday * janela.delta_time())
            i.centro.move_x(andax * janela.delta_time())
            i.centro.move_y(anday * janela.delta_time())
        else:
            andax, anday = colidiu(i, c2)
            i.move_x(andax * janela.delta_time())
            i.move_y(anday * janela.delta_time())
            i.centro.move_x(andax * janela.delta_time())
            i.centro.move_y(anday * janela.delta_time())

# Cria a lista de soldados
def crialistasdesoldados(lista1, cronometro1, cronometro2, fase1, waves_totais, qtd1, qtd2, x):
    acabouw1 = False
    acabouw2 = False

    if(x < len(fase1) - 1 and fase1[x] != 0 and fase1[x + 1] != 0):
        if (cronometro1 >= 2.5 and waves_totais < len(fase1) / 2 and x < len(fase1) and qtd1 < fase1[x]):
            cronometro1 = 0
            qtd1 += 1
            soldadoverde = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
            soldadoverde.x = 1024
            soldadoverde.y = 160
            soldadoverde.direction = 'esquerda'
            soldadoverde.morto = False
            soldadoverde.vida = 100
            soldadoverde.path = 1
            centro = Sprite("Imagens/Jogo/centro.jpg", 1)
            centro.x = 1019 + soldadoverde.width/2
            centro.y = 155 + soldadoverde.height/2
            soldadoverde.centro = centro
            lista1.append(soldadoverde)

        elif (x < len(fase1) and qtd1 == fase1[x]and fase1[x] != 0):
            acabouw1 = True

        if (cronometro2 >= 2.5 and waves_totais < len(fase1) / 2 and x < len(fase1) - 1 and qtd2 < fase1[x + 1] and fase1[x + 1] != 0):
            cronometro2 = 0
            qtd2 += 1
            soldadoverde1 = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
            soldadoverde1.x = 800
            soldadoverde1.y = 640
            soldadoverde1.direction = 'cima'
            soldadoverde1.morto = False
            soldadoverde1.vida = 100
            soldadoverde1.path = 2
            centro = Sprite("Imagens/Jogo/centro.jpg")
            centro.width = 10
            centro.height = 10
            centro.x = 795 + soldadoverde1.width / 2
            centro.y = 635 + soldadoverde1.height / 2
            soldadoverde1.centro = centro
            lista1.append(soldadoverde1)

        elif (x < len(fase1) - 1 and qtd2 == fase1[x + 1] and fase1[x + 1] != 0):
            acabouw2 = True

        if (acabouw1 == True and acabouw2 == True and cronometro1 >= 10):
            qtd1 = 0
            qtd2 = 0
            waves_totais += 1
            x += 2
    else:
        if (cronometro1 >= 2.5 and waves_totais < len(fase1)/2 and x < len(fase1) and qtd1 < fase1[x]):
            cronometro1 = 0
            qtd1 += 1
            soldadoverde = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
            soldadoverde.x = 1024
            soldadoverde.y = 160
            soldadoverde.direction = 'esquerda'
            soldadoverde.morto = False
            soldadoverde.vida = 100
            soldadoverde.path = 1
            centro = Sprite("Imagens/Jogo/centro.jpg")
            centro.width = 10
            centro.height = 10
            centro.x = 1019 + soldadoverde.width / 2
            centro.y = 155 + soldadoverde.height / 2
            soldadoverde.centro = centro
            lista1.append(soldadoverde)

        elif (x < len(fase1) and qtd1 == fase1[x] and cronometro1 >= 10 and fase1[x] != 0):
            qtd1 = 0
            waves_totais += 1
            x += 2

        if (cronometro2 >= 2.5 and waves_totais < len(fase1) / 2 and x < len(fase1) - 1 and qtd2 < fase1[x + 1] and fase1[x + 1] != 0):
            cronometro2 = 0
            qtd2 += 1
            soldadoverde1 = Sprite("Imagens/Jogo/soldadoverdeesquerda.png", 1)
            soldadoverde1.x = 800
            soldadoverde1.y = 640
            soldadoverde1.direction = 'cima'
            soldadoverde1.morto = False
            soldadoverde1.vida = 100
            soldadoverde1.path = 2
            centro = Sprite("Imagens/Jogo/centro.jpg")
            centro.width = 10
            centro.height = 10
            centro.x = 795 + soldadoverde1.width / 2
            centro.y = 635 + soldadoverde1.height / 2
            soldadoverde1.centro = centro
            lista1.append(soldadoverde1)

        elif (x < len(fase1) - 1 and qtd2 == fase1[x + 1] and cronometro2 >= 10 and fase1[x + 1] != 0):
            qtd2 = 0
            waves_totais += 1
            x += 2

    return waves_totais, cronometro1, cronometro2, qtd1, qtd2, x

# Atualiza a direção da arma de acordo com a posição do primeiro soldado dentro do range
def armadirecao(soldados, armas):
    for i in armas:
        for j in soldados:
            if(dentrodorange(i, j)):
                
                # Se entrar, siginifica que o soldado está a direita da arma
                if (i.x + i.width/2 + 19 < j.x + j.width / 2):
                    # Verifica e classifica de acordo com a altura do soldado
                    if (i.y + i.height/2 + 19 < j.y + j.height / 2):
                        i.direction = 'Sudeste'
                    elif (i.y + i.height/2 + 7 < j.y + j.height / 2):
                            i.direction = 'Leste/Sudeste'
                    elif (i.y + i.height/2 - 19 > j.y + j.height / 2):
                        i.direction = 'Nordeste'
                    elif (i.y + i.height/2 - 7 > j.y + j.height / 2):
                            i.direction = 'Leste/Nordeste'
                    else:
                        i.direction = 'Leste'
                        
                # Se entrar, siginifica que o soldado está a esquerda da arma
                elif (i.x + i.width/2 - 19 > j.x + j.width / 2):
                    # Verifica e classifica de acordo com a altura do soldado
                    if (i.y + i.height / 2 + 19 < j.y + j.height / 2):
                        i.direction = 'Sudoeste'
                    elif (i.y + i.height / 2 + 7 < j.y + j.height / 2):
                        i.direction = 'Oeste/Sudoeste'
                    elif (i.y + i.height / 2 - 19 > j.y + j.height / 2):
                        i.direction = 'Noroeste'
                    elif (i.y + i.height / 2 - 7 > j.y + j.height / 2):
                        i.direction = 'Oeste/Noroeste'
                    else:
                        i.direction = 'Oeste'
                        
                # Condição para as direções encontradas na parte de cima ou de baixo do lado direito, entre norte e nordeste, e entre sul e sudeste
                elif (i.x + i.width / 2 + 7 < j.x + j.width / 2):
                    if (i.y + i.height / 2 < j.y + j.height / 2):
                        i.direction = 'Sul/Sudeste'
                    elif (i.y + i.height / 2 > j.y + j.height / 2):
                        i.direction = 'Norte/Nordeste'
                        
                # Condição para as direções encontradas na parte de cima ou de baixo do lado esquerdo, entre norte e noroeste, e entre sul e sudoeste
                elif (i.x + i.width / 2 - 7 > j.x + j.width / 2):
                    if (i.y + i.height / 2 < j.y + j.height / 2):
                            i.direction = 'Sul/Sudoeste'
                    elif (i.y + i.height / 2 > j.y + j.height / 2):
                            i.direction = 'Norte/Noroeste'
                        
                # Condição para as direções restantes
                else:
                    if (i.y + i.height / 2 > j.y + j.height / 2):
                        i.direction = 'Norte'
                    if (i.y + i.height / 2 < j.y + j.height / 2):
                        i.direction = 'Sul'
                break

# Cria lista de armas
def crialistadearmas(armas, slots, mouse, dinheiro):
    for i in slots:
        if (mouse.is_over_area([i.x, i.y], [i.x + 64, i.y + 64]) and mouse.is_button_pressed(1) and dinheiro >= 100):
            arma1 = Sprite("Imagens/Jogo/basearma1.png")
            arma1.x = i.x
            arma1.y = i.y
            arma1.direction = 'Norte'
            i.used = True
            armas.append(arma1)
            dinheiro -= 100
    return dinheiro

# Verifica se o soldado está dentro do range da arma
def dentrodorange(arma, soldado):
    if(soldado.x >= arma.x - 100  and soldado.x <= arma.x + arma.width + 100 and soldado.y >= arma.y - 100 and soldado.y <= arma.y + arma.height + 100):
        return 1
    return 0

# Cria os tiros e coloca em uma lista
def criatiros(lista, armas, soldados, cronometro):
    if(cronometro >= 1):
        for i in armas:
            for j in soldados: 
                if(dentrodorange(i, j)):
                    tiro = Sprite("Imagens/Jogo/bullet.png")
                    tiro.x = i.x + i.width/2 - tiro.width/2
                    tiro.y = i.y + i.height/2 - tiro.height/2
                    tiro.dano = 25
                    tiro.alvo = j
                    lista.append(tiro)
                    break
        cronometro = 0
    return cronometro

# Atualiza a posição do tiro
def atualizpostiro(tiros, dinheiro):
    for i in tiros:
        if(not i.collided(i.alvo.centro)):
            i.move_x((i.alvo.centro.x - i.x)/10)
            i.move_y((i.alvo.centro.y - i.y)/10)
        else:
            i.alvo.vida -= i.dano
            if (i.alvo.vida <= 0):
                i.alvo.morto = True
                dinheiro += 20
            tiros.remove(i)
    return dinheiro

# Remove o soldado morto da lista
def limpalista(soldados):
    for i in soldados:
        if(i.morto == True):
            soldados.remove(i)

# Desenha os inimigos da lista se ainda não chegaram ao fim
def desenhainimigos(lista1, direcao):
    cont = 0

    # Desenha os inimigos de acordo com a direção
    for i in lista1:
        if (i.y + i.height < 0):
            lista1.remove(i)
            cont += 1
        elif (i.direction == 'esquerda'):
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

# Desenha arma de acordo com a direção dela
def desenhaarma1(armas, direcao):
    for i in armas:
        if (i.direction == 'Norte'):
            direcao['Norte'].x = i.x
            direcao['Norte'].y = i.y
            direcao['Norte'].draw()
        elif (i.direction == 'Leste'):
            direcao['Leste'].x = i.x
            direcao['Leste'].y = i.y
            direcao['Leste'].draw()
        elif (i.direction == 'Sul'):
            direcao['Sul'].x = i.x
            direcao['Sul'].y = i.y
            direcao['Sul'].draw()
        elif (i.direction == 'Oeste'):
            direcao['Oeste'].x = i.x
            direcao['Oeste'].y = i.y
            direcao['Oeste'].draw()
        elif (i.direction == 'Nordeste'):
            direcao['Nordeste'].x = i.x
            direcao['Nordeste'].y = i.y
            direcao['Nordeste'].draw()
        elif (i.direction == 'Sudeste'):
            direcao['Sudeste'].x = i.x
            direcao['Sudeste'].y = i.y
            direcao['Sudeste'].draw()
        elif (i.direction == 'Noroeste'):
            direcao['Noroeste'].x = i.x
            direcao['Noroeste'].y = i.y
            direcao['Noroeste'].draw()
        elif (i.direction == 'Sudoeste'):
            direcao['Sudoeste'].x = i.x
            direcao['Sudoeste'].y = i.y
            direcao['Sudoeste'].draw()
        elif (i.direction == 'Norte/Nordeste'):
            direcao['Norte/Nordeste'].x = i.x
            direcao['Norte/Nordeste'].y = i.y
            direcao['Norte/Nordeste'].draw()
        elif (i.direction == 'Norte/Noroeste'):
            direcao['Norte/Noroeste'].x = i.x
            direcao['Norte/Noroeste'].y = i.y
            direcao['Norte/Noroeste'].draw()
        elif (i.direction == 'Leste/Nordeste'):
            direcao['Leste/Nordeste'].x = i.x
            direcao['Leste/Nordeste'].y = i.y
            direcao['Leste/Nordeste'].draw()
        elif (i.direction == 'Leste/Sudeste'):
            direcao['Leste/Sudeste'].x = i.x
            direcao['Leste/Sudeste'].y = i.y
            direcao['Leste/Sudeste'].draw()
        elif (i.direction == 'Sul/Sudeste'):
            direcao['Sul/Sudeste'].x = i.x
            direcao['Sul/Sudeste'].y = i.y
            direcao['Sul/Sudeste'].draw()
        elif (i.direction == 'Sul/Sudoeste'):
            direcao['Sul/Sudoeste'].x = i.x
            direcao['Sul/Sudoeste'].y = i.y
            direcao['Sul/Sudoeste'].draw()
        elif (i.direction == 'Oeste/Sudoeste'):
            direcao['Oeste/Sudoeste'].x = i.x
            direcao['Oeste/Sudoeste'].y = i.y
            direcao['Oeste/Sudoeste'].draw()
        else:
            direcao['Oeste/Noroeste'].x = i.x
            direcao['Oeste/Noroeste'].y = i.y
            direcao['Oeste/Noroeste'].draw()

# Função da fase
def FASE(janela, background, mouse, teclado, fase):

    # Inicicialização de variáveis importantes
    vidas = 10
    dinheiro = 100
    pause = False
    GO = False
    GG = False
    indice = 0
    cronometro1 = 0
    cronometro2 = 0
    cronometro3 = 0
    qtddeinimigos1 = 0
    qtddeinimigos2 = 0
    waves_totais = 0
    listadesoldados = []
    listadearmas = []
    listadetiros = []

    # Inicializa sprites da arma em todas as direções
    arma1Norte = Sprite("Imagens/Jogo/Arma1/arma1cima.png", 1)
    arma1Nordeste = Sprite("Imagens/Jogo/Arma1/arma1nordeste.png", 1)
    arma1Leste = Sprite("Imagens/Jogo/Arma1/arma1direita.png", 1)
    arma1Sudeste = Sprite("Imagens/Jogo/Arma1/arma1sudeste.png", 1)
    arma1Sul = Sprite("Imagens/Jogo/Arma1/arma1baixo.png", 1)
    arma1Sudoeste = Sprite("Imagens/Jogo/Arma1/arma1sudoeste.png", 1)
    arma1Oeste = Sprite("Imagens/Jogo/Arma1/arma1esquerda.png", 1)
    arma1Noroeste = Sprite("Imagens/Jogo/Arma1/arma1noroeste.png", 1)
    arma1NorteNordeste = Sprite("Imagens/Jogo/Arma1/arma1NNL.png", 1)
    arma1NorteNoroeste = Sprite("Imagens/Jogo/Arma1/arma1NON.png", 1)
    arma1LesteNordeste = Sprite("Imagens/Jogo/Arma1/arma1NLL.png", 1)
    arma1LesteSudeste = Sprite("Imagens/Jogo/Arma1/arma1LSL.png", 1)
    arma1SulSudeste = Sprite("Imagens/Jogo/Arma1/arma1SLS.png", 1)
    arma1SulSudoeste = Sprite("Imagens/Jogo/Arma1/arma1SSO.png", 1)
    arma1OesteSudoeste = Sprite("Imagens/Jogo/Arma1/arma1SOO.png", 1)
    arma1OesteNoroeste = Sprite("Imagens/Jogo/Arma1/arma1ONO.png", 1)

    # Dicionário com as direções das armas
    rota_arma = {'Norte': arma1Norte, 'Nordeste': arma1Nordeste, 'Leste': arma1Leste, "Sudeste": arma1Sudeste,
                 'Sul': arma1Sul, 'Sudoeste': arma1Sudoeste, 'Oeste': arma1Oeste, 'Noroeste': arma1Noroeste,
                 'Norte/Nordeste': arma1NorteNordeste, 'Norte/Noroeste': arma1NorteNoroeste, 'Leste/Nordeste': arma1LesteNordeste,
                 'Leste/Sudeste': arma1LesteSudeste, 'Sul/Sudeste': arma1SulSudeste, 'Sul/Sudoeste': arma1SulSudoeste,
                 'Oeste/Sudoeste': arma1OesteSudoeste, 'Oeste/Noroeste': arma1OesteNoroeste}

    # Inicializa e posiciona os slots
    slotarma = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma.x = 0
    slotarma.y = 64
    slotarma.used = False
    slotarma1 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma1.x = 0
    slotarma1.y = 128
    slotarma1.used = False
    slotarma2 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma2.x = 0
    slotarma2.y = 192
    slotarma2.used = False
    slotarma3 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma3.x = 64
    slotarma3.y = 256
    slotarma3.used = False
    slotarma4 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma4.x = 128
    slotarma4.y = 256
    slotarma4.used = False
    slotarma5 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma5.x = 192
    slotarma5.y = 256
    slotarma5.used = False
    slotarma6 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma6.x = 192
    slotarma6.y = 320
    slotarma6.used = False
    slotarma7 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma7.x = 192
    slotarma7.y = 384
    slotarma7.used = False
    slotarma8 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma8.x = 192
    slotarma8.y = 448
    slotarma8.used = False
    slotarma9 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma9.x = 256
    slotarma9.y = 512
    slotarma9.used = False
    slotarma10 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma10.x = 320
    slotarma10.y = 512
    slotarma10.used = False
    slotarma11 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma11.x = 384
    slotarma11.y = 512
    slotarma11.used = False
    slotarma12 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma12.x = 448
    slotarma12.y = 512
    slotarma12.used = False
    slotarma13 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma13.x = 512
    slotarma13.y = 512
    slotarma13.used = False
    slotarma14 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma14.x = 576
    slotarma14.y = 512
    slotarma14.used = False
    slotarma15 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma15.x = 640
    slotarma15.y = 512
    slotarma15.used = False
    slotarma16 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma16.x = 704
    slotarma16.y = 512
    slotarma16.used = False
    slotarma17 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma17.x = 896
    slotarma17.y = 512
    slotarma17.used = False
    slotarma18 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma18.x = 896
    slotarma18.y = 448
    slotarma18.used = False
    slotarma19 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma19.x = 896
    slotarma19.y = 384
    slotarma19.used = False
    slotarma20 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma20.x = 896
    slotarma20.y = 320
    slotarma20.used = False
    slotarma21 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma21.x = 896
    slotarma21.y = 256
    slotarma21.used = False
    slotarma22 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma22.x = 832
    slotarma22.y = 256
    slotarma22.used = False
    slotarma23 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma23.x = 768
    slotarma23.y = 256
    slotarma23.used = False
    slotarma24 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma24.x = 704
    slotarma24.y = 256
    slotarma24.used = False
    slotarma25 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma25.x = 640
    slotarma25.y = 256
    slotarma25.used = False
    slotarma26 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma26.x = 576
    slotarma26.y = 320
    slotarma26.used = False
    slotarma27 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma27.x = 512
    slotarma27.y = 320
    slotarma27.used = False
    slotarma28 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma28.x = 448
    slotarma28.y = 320
    slotarma28.used = False
    slotarma29 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma29.x = 384
    slotarma29.y = 320
    slotarma29.used = False
    slotarma30 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma30.x = 576
    slotarma30.y = 192
    slotarma30.used = False
    slotarma31 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma31.x = 896
    slotarma31.y = 64
    slotarma31.used = False
    slotarma32 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma32.x = 832
    slotarma32.y = 64
    slotarma32.used = False
    slotarma33 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma33.x = 768
    slotarma33.y = 64
    slotarma33.used = False
    slotarma34 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma34.x = 704
    slotarma34.y = 0
    slotarma34.used = False
    slotarma35 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma35.x = 640
    slotarma35.y = 0
    slotarma35.used = False
    slotarma36 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma36.x = 576
    slotarma36.y = 0
    slotarma36.used = False
    slotarma37 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma37.x = 512
    slotarma37.y = 0
    slotarma37.used = False
    slotarma38 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma38.x = 448
    slotarma38.y = 0
    slotarma38.used = False
    slotarma39 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma39.x = 384
    slotarma39.y = 128
    slotarma39.used = False
    slotarma40 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma40.x = 384
    slotarma40.y = 64
    slotarma40.used = False
    slotarma41 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma41.x = 320
    slotarma41.y = 64
    slotarma41.used = False
    slotarma42 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma42.x = 256
    slotarma42.y = 64
    slotarma42.used = False
    slotarma43 = Sprite("Imagens/Jogo/slotarma.png", 1)
    slotarma43.x = 192
    slotarma43.y = 64
    slotarma43.used = False

    # Cria uma lista com os slots inicializados
    listaslots = {slotarma, slotarma1, slotarma2, slotarma3, slotarma4, slotarma5, slotarma6, slotarma7, slotarma8,
                  slotarma9, slotarma10, slotarma11, slotarma12, slotarma13, slotarma14, slotarma15, slotarma16,
                  slotarma17, slotarma18, slotarma19, slotarma20, slotarma20, slotarma21, slotarma22, slotarma23,
                  slotarma24, slotarma25, slotarma26, slotarma27, slotarma28, slotarma29, slotarma30, slotarma31,
                  slotarma32, slotarma33, slotarma34, slotarma35, slotarma36, slotarma37, slotarma38, slotarma39,
                  slotarma40, slotarma41, slotarma42, slotarma43}

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
    while (not teclado.key_pressed("esc")):

        # Pausa o jogo caso o jogador clique enter
        if (teclado.key_pressed("enter")):
            pause = pausado(janela, background, teclado)

        # Se o jogo estiver despausado
        if (pause == False):

            # Atualização do cronômetro
            cronometro1 += janela.delta_time()
            cronometro2 += janela.delta_time()
            cronometro3 += janela.delta_time()

            # Criação das listas de soldados
            waves_totais, cronometro1, cronometro2, qtddeinimigos1, qtddeinimigos2, indice = \
                crialistasdesoldados(listadesoldados, cronometro1, cronometro2, fase, waves_totais, qtddeinimigos1,
                                     qtddeinimigos2, indice)


            # Cria lista de armas
            dinheiro = crialistadearmas(listadearmas, listaslots, mouse, dinheiro)

            # Cria lista de tiros
            cronometro3 = criatiros(listadetiros, listadearmas, listadesoldados, cronometro3)

            # Atualização da posição dos inimigos
            atualizainimigo(listadesoldados, caminho1, caminho2, janela)
            
            # Atualiza a posição do tiro
            dinheiro = atualizpostiro(listadetiros, dinheiro)
            
            # Remove os soldados mortos da lista
            limpalista(listadesoldados)

            # Atualiza direção da arma em relação ao primeiro inimigo do caminho 1
            if(listadesoldados != [] and listadearmas != []):
                armadirecao(listadesoldados, listadearmas)

            # Desenho na tela
            background.draw()

            # Desenha slots
            for i in listaslots:
                if(i.used == False):
                    i.draw()

            # Desenha armas
            desenhaarma1(listadearmas, rota_arma)

            # Desenho dos inimigos e atualização da contagem de vidas
            vidas -= desenhainimigos(listadesoldados, svdirecao)

            # Desenha os tiros
            for i in listadetiros:
                i.draw()

            # Verifica se houve o game over
            GO = gameover(vidas, janela)

            # Verifica condição de vitória
            GG = victory(fase, indice, listadesoldados, janela)

            # Verifica se houve vitória ou derrota e sai do loop
            if(GG == True or GO == True):
                break

            # Desenha a quantidade de vidas e do dinheiro na tela
            janela.draw_text(f"Vidas: {vidas}", 780, 10, 20, [255, 255, 255], "Arial", True)
            janela.draw_text(f"Dinheiro: {dinheiro}", 880, 10, 20, [255, 255, 255], "Arial", True)

            # Update da janela
            janela.update()

    # Retorna 0 para voltar ao menu no caso ESC
    return GG, GO


def jogo(fase):

    # Inicialização da janela e background estático
    janela = Window(1024, 640)
    background = GameImage("Imagens/Jogo/backgroundoficial.jpg")
    janela.set_title("Stolen Crown")

    # Inicialização do teclado e do mouse
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    venceu = False
    perdeu = False

    # Listas de fases
    fase1 = [5, 0, 5, 0, 0, 5, 0, 5, 5, 5]
    fase2 = [5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 7, 0, 0, 7, 7, 7]
    fase3 = [5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 7, 0, 0, 7, 7, 7, 10, 0, 0, 10, 10, 10]

    while (not teclado.key_pressed("esc")):

        # Deixa o jogo pausado até clicarem espaço e direciona para a fase escolhida
        if (teclado.key_pressed("space") and fase == 1):
            venceu, perdeu = FASE(janela, background, mouse, teclado, fase1)
            
            # Se o jogador venceu o nivel, ele pode escolher entre continuar para o nivel 2 ou sair para o menu
            if(venceu == True):
                while(True):
                    if(teclado.key_pressed("s")):
                        fase = 2
                        break
                    elif(teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Deseja continuar? (s -> Sim e n -> Não).", 35, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()
            
            # Se o jogar perdeu, ele pode tentar o nivel novamente ou voltar para o menu
            if(perdeu == True):
                while(True):
                    if (teclado.key_pressed("s")):
                        break
                    elif(teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Tentar Novamente? (s -> Sim e n -> Não).", 25, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()

        elif (teclado.key_pressed("space") and fase == 2):
            venceu, perdeu = FASE(janela, background, mouse, teclado, fase2)

            # Se o jogador venceu o nivel, ele pode escolher entre continuar para o nivel 3 ou sair para o menu
            if (venceu == True):
                while (True):
                    if (teclado.key_pressed("s")):
                        fase = 3
                        break
                    elif (teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Deseja continuar? (s -> Sim e n -> Não).", 35, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()

            # Se o jogar perdeu, ele pode tentar o nivel novamente ou voltar para o menu
            if (perdeu == True):
                while (True):
                    if (teclado.key_pressed("s")):
                        break
                    elif (teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Tentar Novamente? (s -> Sim e n -> Não).", 25, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()

        elif (teclado.key_pressed("space") and fase == 3):
            venceu, perdeu = FASE(janela, background, mouse, teclado, fase3)

            # Se o jogador venceu o nivel, ele pode escolher entre jogar novamente as fases existentes do início ou sair para o menu
            if (venceu == True):
                while(True):
                    if(teclado.key_pressed("s")):
                        fase = 1
                        break
                    elif(teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Jogar Novamente? (s -> Sim e n -> Não).", 25, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()

            # Se o jogar perdeu, ele pode tentar o nivel novamente ou voltar para o menu
            if(perdeu == True):
                while (True):
                    if (teclado.key_pressed("s")):
                        break
                    elif (teclado.key_pressed("n")):
                        return 0
                    background.draw()
                    janela.draw_text("Tentar Novamente? (s -> Sim e n -> Não).", 25, 280, 50, [255, 255, 255], "Arial",
                                     True)
                    janela.update()

        # Desenho na tela
        background.draw()
        janela.draw_text("Pressione espaço para iniciar.", 150, 280, 50, [255, 255, 255], "Arial", True)
        janela.update()

        # Retorna 0 para voltar ao menu no caso ESC
    return 0
