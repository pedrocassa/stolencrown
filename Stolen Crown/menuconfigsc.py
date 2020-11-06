from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

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