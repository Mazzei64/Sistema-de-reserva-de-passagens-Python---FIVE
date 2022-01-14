import os

def MoveCursor(x, y):
    print("\033[%d;%dH" % (y, x))

def EchoON(boolean):
    if(boolean):
        os.system("stty echo")
    else:
        os.system("stty -echo")

def CursorON(boolean):
    if(boolean):
        print('\033[?25h')
    else:
        print('\033[?25l')