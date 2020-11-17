from menusc import menu
from menuconfigsc import menuconfig
from jogosc import jogo

gamestate = 0
dificuldade = 1

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