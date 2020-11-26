from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def menu():
    # Inicialização da janela e do background estático
    janela = Window(500,500)
    background = GameImage("Imagens/Menu/fundomenu.jpg")
    janela.set_title("Stolen Crown")

    # Inicialização do mouse e do teclado
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    # Inicialização dos botões do menu, normais e rosas
    jogar = Sprite("Imagens/Menu/botaojogar.jpg",1)
    fases = Sprite("Imagens/Menu/botaofases.jpg",1)
    ranking = Sprite("Imagens/Menu/botaoranking.jpg",1)
    sair = Sprite("Imagens/Menu/botaosair.jpg",1)
    jogarrosa = Sprite("Imagens/Menu/botaojogarrosa.jpg", 1)
    fasesrosa = Sprite("Imagens/Menu/botaofasesrosa.jpg", 1)
    rankingrosa = Sprite("Imagens/Menu/botaorankingrosa.jpg", 1)
    sairrosa = Sprite("Imagens/Menu/botaosairrosa.jpg", 1)

    # Posicionamento dos botões
    jogar.x = janela.width / 2 - jogar.width / 2
    jogar.y = janela.height / 2 - jogar.height / 2 - 50
    jogarrosa.x = janela.width / 2 - jogarrosa.width / 2
    jogarrosa.y = janela.height / 2 - jogarrosa.height / 2 - 50
    fases.x = janela.width / 2 - fases.width / 2
    fases.y = janela.height / 2 - fases.height / 2
    fasesrosa.x = janela.width / 2 - fasesrosa.width / 2
    fasesrosa.y = janela.height / 2 - fasesrosa.height / 2
    ranking.x = janela.width / 2 - ranking.width / 2
    ranking.y = janela.height / 2 - ranking.height / 2 + 50
    rankingrosa.x = janela.width / 2 - rankingrosa.width / 2
    rankingrosa.y = janela.height / 2 - rankingrosa.height / 2 + 50
    sair.x = janela.width / 2 - sair.width / 2
    sair.y = janela.height / 2 - sair.height / 2 + 100
    sairrosa.x = janela.width / 2 - sairrosa.width / 2
    sairrosa.y = janela.height / 2 - sairrosa.height / 2 + 100

    # Loop do menu
    while(True):
        # Verifica se o mouse passou por cima do botão, e se houve clique
        if (mouse.is_over_area([jogar.x, jogar.y], [jogar.x + jogar.width, jogar.y + jogar.height]) and mouse.is_button_pressed(1)):
            return 1
        elif (mouse.is_over_area([fases.x, fases.y], [fases.x + fases.width, fases.y + fases.height]) and mouse.is_button_pressed(1)):
            return 2
        elif (mouse.is_over_area([ranking.x, ranking.y], [ranking.x + ranking.width, ranking.y + ranking.height]) and mouse.is_button_pressed(1)):
            gamestate = 3
            pass
        elif (mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1)):
            janela.close()

        # Desenha menu na tela
        background.draw()
        janela.draw_text("Stolen Crown", 25, 50, 70, (255,255,255),"Arial", True)
        if (mouse.is_over_area([jogar.x, jogar.y], [jogar.x + jogar.width, jogar.y + jogar.height])):
            jogarrosa.draw()
            fases.draw()
            ranking.draw()
            sair.draw()
        elif (mouse.is_over_area([fases.x, fases.y], [fases.x + fases.width, fases.y + fases.height])):
            jogar.draw()
            fasesrosa.draw()
            ranking.draw()
            sair.draw()
        elif (mouse.is_over_area([ranking.x, ranking.y], [ranking.x + ranking.width, ranking.y + ranking.height])):
            jogar.draw()
            fases.draw()
            rankingrosa.draw()
            sair.draw()
        elif (mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height])):
            jogar.draw()
            fases.draw()
            ranking.draw()
            sairrosa.draw()
        else:
            jogar.draw()
            fases.draw()
            ranking.draw()
            sair.draw()
        janela.update()