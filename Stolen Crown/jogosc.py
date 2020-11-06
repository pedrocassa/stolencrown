from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

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