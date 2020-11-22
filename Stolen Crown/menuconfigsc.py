from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def menuconfig():
    # Inicialização da janela e do background estático
    janela = Window(500, 500)
    background = GameImage("Imagens/Menu/fundomenu.jpg")
    janela.set_title("Stolen Crown")

    # Inicialização do mouse e do teclado
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    # Inicialização dos botões, normais e rosas
    fase1 = Sprite("Imagens/Menu/botaofase1.jpg", 1)
    fase2 = Sprite("Imagens/Menu/botaofase2.jpg", 1)
    fase3 = Sprite("Imagens/Menu/botaofase3.jpg", 1)
    fase1rosa = Sprite("Imagens/Menu/botaofase1rosa.jpg", 1)
    fase2rosa = Sprite("Imagens/Menu/botaofase2rosa.jpg", 1)
    fase3rosa = Sprite("Imagens/Menu/botaofase3rosa.jpg", 1)

    # Posicionamento dos botões
    fase1.x = janela.width / 2 - fase1.width / 2
    fase1.y = janela.height / 2 - fase1.height / 2 - 50
    fase1rosa.x = janela.width / 2 - fase1rosa.width / 2
    fase1rosa.y = janela.height / 2 - fase1rosa.height / 2 - 50
    fase2.x = janela.width / 2 - fase2.width / 2
    fase2.y = janela.height / 2 - fase2.height / 2
    fase2rosa.x = janela.width / 2 - fase2rosa.width / 2
    fase2rosa.y = janela.height / 2 - fase2rosa.height / 2
    fase3.x = janela.width / 2 - fase3.width / 2
    fase3.y = janela.height / 2 - fase3.height / 2 + 50
    fase3rosa.x = janela.width / 2 - fase3rosa.width / 2
    fase3rosa.y = janela.height / 2 - fase3rosa.height / 2 + 50

    # Loop do menu de configuração
    while(not teclado.key_pressed("esc")):
        # Verifica se o mouse está em cima do botão e se houve clique
        if (mouse.is_over_area([fase1.x, fase1.y], [fase1.x + fase1.width, fase1.y + fase1.height]) and mouse.is_button_pressed(1)):
            return 1
        elif (mouse.is_over_area([fase2.x, fase2.y], [fase2.x + fase2.width, fase2.y + fase2.height]) and mouse.is_button_pressed(1)):
            return 2
        elif (mouse.is_over_area([fase3.x, fase3.y], [fase3.x + fase3.width, fase3.y + fase3.height]) and mouse.is_button_pressed(1)):
            return 3

        # Desenha o menu de configuração na tela
        background.draw()
        janela.draw_text("Fases", 150, 65, 70, (255, 255, 255), "Arial", True)
        if (mouse.is_over_area([fase1.x, fase1.y], [fase1.x + fase1.width, fase1.y + fase1.height])):
            fase1rosa.draw()
            fase2.draw()
            fase3.draw()
        elif (mouse.is_over_area([fase2.x, fase2.y], [fase2.x + fase2.width, fase2.y + fase2.height])):
            fase1.draw()
            fase2rosa.draw()
            fase3.draw()
        elif (mouse.is_over_area([fase3.x, fase3.y], [fase3.x + fase3.width, fase3.y + fase3.height])):
            fase1.draw()
            fase2.draw()
            fase3rosa.draw()
        else:
            fase1.draw()
            fase2.draw()
            fase3.draw()
        janela.update()
    return 0