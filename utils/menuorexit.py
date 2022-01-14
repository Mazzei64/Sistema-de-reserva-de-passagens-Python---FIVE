from .readfromstream import getKey
from pages.exitanimation import ExitAnimation

def MainOrExit():
    print("\n\t\t\t\033[38;5;136m(1)MAIN MENU (2)EXIT\n\033[38;5;255m")    
    while True:
        key = getKey()
        if(key != '1' and key != '2'):
            continue
        
        num = int(key)
        if(num == 1):                                   
            return True
            
        elif(num == 2):
            ExitAnimation()