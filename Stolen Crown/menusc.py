from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

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