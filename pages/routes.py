from time import sleep

from utils.kbhit import getch
from utils.readfromstream import getKey
from utils.screenrefresh import refresh

def PrintRoutesList(list):
    for i in range(list.__len__()):
        print("\t{}".format(list[i]))
        
def routes(repository, authKey):
    if not repository.IsAuthUser(authKey):
        print('\033[38;5;196m', end="")
        print("\n\n\tYou have no routes in your wallet")
        print("\tPlease, try registering or logging in.")
        print('\033[38;5;255m', end="")
        sleep(2)
        return
    
    if not repository.UserHasRoutes(authKey.userId):
        print('\033[38;5;11m', end="")
        print("You have no routes in your wallet")
        print('\033[38;5;255m', end="")
        sleep(1.5)
        return
    
    routes = []
    repository.GetRoustesListByUserId(routes, authKey.userId)
    if routes == 0:
        print("You have no routes in your wallet")
        sleep(2)
        return
    
    track = 0
    while True:
        if track == 0:
            refresh()
            print("\033[38;5;25mYOUR WALLET:\033[38;5;255m\n\n")
            # print("\033[48;5;22m", end="")
            print("\033[48;5;25m", end="")
            # print("\033[38;5;208m")
            print("\033[38;5;16m")
            print("\033[1m", end="")
            PrintRoutesList(routes)
            print("\033[0m", end="")
            print("\033[38;5;255m")
            print("\033[48;5;233m", end="")
            print("\n\n\t\t\033[38;5;136mPRESS (q) To Return\033[38;5;255m")
            track = 1
    
        key = getKey()
        if key == 'q':
            return
    