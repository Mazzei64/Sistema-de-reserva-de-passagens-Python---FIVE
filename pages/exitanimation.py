from os import system
import sys
import time
from utils.cursors import CursorON
from utils.screenrefresh import refresh

def ExitAnimation():
    refresh()
    bye = "GOOD BYE!!"
    print('\033[38;5;40m', end="")
    print('\033[1m', end="")
    for i in range(bye.__len__()):
        sys.stdout.write(bye[i])
        sys.stdout.flush()
        time.sleep(0.20)
    print('\033[38;5;231m', end="")
    print('\033[0m', end="")
    print()
    system('clear')
    CursorON(True)
    exit()