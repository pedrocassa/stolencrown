from menusc import menu
from menuconfigsc import menuconfig
from jogosc import jogo

gamestate = 0
fase = 1

while(True):
    if(gamestate == 0):
        gamestate = menu()
    elif (gamestate == 1):
        gamestate = jogo(fase)
    elif(gamestate == 2):
        fase = menuconfig()
        if(fase == 0):
            fase = 1
            gamestate = 0
        else:
            gamestate = jogo(fase)