from backend.entities.auth import Auth
from .exitanimation import ExitAnimation
from pages.login import login
from pages.register import register
from pages.routes import routes
from pages.search import search
from utils.readfromstream import getKey
from utils.screenrefresh import refresh

def mainmenu(repository):
    
    authKey = Auth()
    logged = False
    while True:
        key = ''
        refresh()
        if(logged == False):
            print("\033[38;5;25m(1)LOGIN (2)REGISTER (3)SEARCH ROUTES (4)EXIT\033[38;5;255m")
            while True:
                key = getKey()
                if(key != '1' and key != '2' and key != '3' and key != '4'):
                    continue
                
                num = int(key)
                if(num == 1):
                    logged = login(repository, authKey)
                    refresh()
                    break
                    
                elif(num == 2):
                    register(repository)
                    break

                elif(num == 3):
                    search(repository, authKey)
                    break
                elif(num == 4):
                    ExitAnimation()
        else:
            print("\033[38;5;25m(1)LOGOUT (2)SEARCH ROUTES (3)ROUTES (4)EXIT\033[38;5;255m")
            while True:
                key = getKey()
                if(key != '1' and key != '2' and key != '3' and key != '4'):
                    continue
                
                num = int(key)
                if(num == 1):
                    logged = False
                    repository.RemoveAuthUser(authKey)
                    break
                
                elif(num == 2):
                    search(repository, authKey)
                    break
                
                elif (num == 3):
                    routes(repository, authKey)
                    break
                
                elif(num == 4):
                    ExitAnimation()