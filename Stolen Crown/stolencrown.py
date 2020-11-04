from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

gamestate = 0
dificuldade = 1

def menu():
    janela = Window(500,500)
    background = GameImage("fundomenu.jpg")
    janela.set_title("Stolen Crown")
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    jogar = Sprite("botaojogar.jpg",1)
    configurar = Sprite("botaoconfigurar.jpg",1)
    ranking = Sprite("botaoranking.jpg",1)
    sair = Sprite("botaosair.jpg",1)
    jogarhl = Sprite("botaojogarrosa.jpg", 1)
    configurarhl = Sprite("botaoconfigurarrosa.jpg", 1)
    rankinghl = Sprite("botaorankingrosa.jpg", 1)
    sairhl = Sprite("botaosairrosa.jpg", 1)

    jogar.x = janela.width / 2 - jogar.width / 2
    jogar.y = janela.height / 2 - jogar.height / 2 - 50
    jogarhl.x = janela.width / 2 - jogarhl.width / 2
    jogarhl.y = janela.height / 2 - jogarhl.height / 2 - 50
    configurar.x = janela.width / 2 - configurar.width / 2
    configurar.y = janela.height / 2 - configurar.height / 2
    configurarhl.x = janela.width / 2 - configurarhl.width / 2
    configurarhl.y = janela.height / 2 - configurarhl.height / 2
    ranking.x = janela.width / 2 - ranking.width / 2
    ranking.y = janela.height / 2 - ranking.height / 2 + 50
    rankinghl.x = janela.width / 2 - rankinghl.width / 2
    rankinghl.y = janela.height / 2 - rankinghl.height / 2 + 50
    sair.x = janela.width / 2 - sair.width / 2
    sair.y = janela.height / 2 - sair.height / 2 + 100
    sairhl.x = janela.width / 2 - sairhl.width / 2
    sairhl.y = janela.height / 2 - sairhl.height / 2 + 100

    while(True):
        if (mouse.is_over_area([jogar.x, jogar.y], [jogar.x + jogar.width, jogar.y + jogar.height]) and mouse.is_button_pressed(1)):
            return 1
        elif (mouse.is_over_area([configurar.x, configurar.y], [configurar.x + configurar.width, configurar.y + configurar.height]) and mouse.is_button_pressed(1)):
            return 2
        elif (mouse.is_over_area([ranking.x, ranking.y], [ranking.x + ranking.width, ranking.y + ranking.height]) and mouse.is_button_pressed(1)):
            gamestate = 3
            pass
        elif (mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1)):
            janela.close()
        background.draw()
        janela.draw_text("Stolen Crown", 25, 50, 70, (255,255,255),"Arial", True)
        if (mouse.is_over_area([jogar.x, jogar.y], [jogar.x + jogar.width, jogar.y + jogar.height])):
            jogarhl.draw()
            configurar.draw()
            ranking.draw()
            sair.draw()
        elif (mouse.is_over_area([configurar.x, configurar.y], [configurar.x + configurar.width, configurar.y + configurar.height])):
            jogar.draw()
            configurarhl.draw()
            ranking.draw()
            sair.draw()
        elif (mouse.is_over_area([ranking.x, ranking.y], [ranking.x + ranking.width, ranking.y + ranking.height])):
            jogar.draw()
            configurar.draw()
            rankinghl.draw()
            sair.draw()
        elif (mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height])):
            jogar.draw()
            configurar.draw()
            ranking.draw()
            sairhl.draw()
        else:
            jogar.draw()
            configurar.draw()
            ranking.draw()
            sair.draw()
        janela.update()

def menuconfig():
    janela = Window(500, 500)
    background = GameImage("fundomenu.jpg")
    janela.set_title("Stolen Crown")
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    facil = Sprite("botaofacil.jpg", 1)
    medio = Sprite("botaomedio.jpg", 1)
    dificil = Sprite("botaodificil.jpg", 1)
    facilhl = Sprite("botaofacilrosa.jpg", 1)
    mediohl = Sprite("botaomediorosa.jpg", 1)
    dificilhl = Sprite("botaodificilrosa.jpg", 1)

    facil.x = janela.width / 2 - facil.width / 2
    facil.y = janela.height / 2 - facil.height / 2 - 50
    facilhl.x = janela.width / 2 - facilhl.width / 2
    facilhl.y = janela.height / 2 - facilhl.height / 2 - 50
    medio.x = janela.width / 2 - medio.width / 2
    medio.y = janela.height / 2 - medio.height / 2
    mediohl.x = janela.width / 2 - mediohl.width / 2
    mediohl.y = janela.height / 2 - mediohl.height / 2
    dificil.x = janela.width / 2 - dificil.width / 2
    dificil.y = janela.height / 2 - dificil.height / 2 + 50
    dificilhl.x = janela.width / 2 - dificilhl.width / 2
    dificilhl.y = janela.height / 2 - dificilhl.height / 2 + 50

    while(not teclado.key_pressed("esc")):
        if (mouse.is_over_area([facil.x, facil.y], [facil.x + facil.width, facil.y + facil.height]) and mouse.is_button_pressed(1)):
            return 1
        elif (mouse.is_over_area([medio.x, medio.y], [medio.x + medio.width, medio.y + medio.height]) and mouse.is_button_pressed(1)):
            return 2
        elif (mouse.is_over_area([dificil.x, dificil.y], [dificil.x + dificil.width, dificil.y + dificil.height]) and mouse.is_button_pressed(1)):
            return 3
        background.draw()
        janela.draw_text("Dificuldades", 45, 65, 70, (255, 255, 255), "Arial", True)
        if (mouse.is_over_area([facil.x, facil.y], [facil.x + facil.width, facil.y + facil.height])):
            facilhl.draw()
            medio.draw()
            dificil.draw()
        elif (mouse.is_over_area([medio.x, medio.y], [medio.x + medio.width, medio.y + medio.height])):
            facil.draw()
            mediohl.draw()
            dificil.draw()
        elif (mouse.is_over_area([dificil.x, dificil.y], [dificil.x + dificil.width, dificil.y + dificil.height])):
            facil.draw()
            medio.draw()
            dificilhl.draw()
        else:
            facil.draw()
            medio.draw()
            dificil.draw()
        janela.update()
    return 0

def jogo(dificuldade):
    janela = Window(1024, 640)
    background = GameImage("background2.jpg")
    janela.set_title("Stolen Crown")
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()
    while(not teclado.key_pressed("esc")):
        background.draw()
        janela.update()
    return 0

while(True):
    if(gamestate == 0):
        gamestate = menu()
    elif (gamestate == 1):
        gamestate = jogo(dificuldade)
    elif(gamestate == 2):
        dificuldade = menuconfig()
        if(dificuldade == 0):
            dificuldade = 1
            gamestate = 0
        else:
            gamestate = jogo(dificuldade)