from time import sleep
from utils.kbhit import getch
from utils.readfromstream import GetArrowKey, getKey
from utils.screenrefresh import refresh

def Selection(text, select = True):
    if select:
        print('\033[38;5;11m', end="")
        print(text)
    else:
       print('\033[38;5;231m', end="") 
       print(text)

def PrintList(list, highlight = 1):
    for i in range(list.__len__()):
        if (highlight - 1) == i:
            Selection("\t{}".format(list[i]))
            continue
        
        Selection("\t{}".format(list[i]), False)
      
def search(repository, authkeyBuffer):
    if not repository.IsAuthUser(authkeyBuffer):
        print('\033[38;5;196m', end="")
        print("\n\n\tYou are unauthorized to search for routes.")
        print("\tPlease, try registering or logging in.")
        print('\033[38;5;255m', end="")
        sleep(3)
        return

    routeList = []
    
    routeList.append('Rio de Janeiro -->      São Paulo     (15:20)')
    routeList.append('São Paulo      -->         Berlin     (22:40)')
    routeList.append('Macaé          -->          Paris     (16:15)')
    routeList.append('London         --> São João do Miriti (07:00)')
    routeList.append('Iran           -->       Salvador     (05:35)') 
    
    track = 0
    keyBuffer = []
    header = "\033[38;5;25mPLEASE SELECT THE DESIRED ROUTE:\033[38;5;255m\n\n"
    
    while True:
        
        if track == 0:
            refresh()
            print(header)
            PrintList(routeList)
            print("\n\n\t\t\033[38;5;136mPRESS (q) To Return\033[38;5;255m\n\n")
            track +=1
        
        GetArrowKey(keyBuffer)
        
        if keyBuffer.__len__() > 1:
            if keyBuffer[0] == '\x1b' and keyBuffer[1] == 66:
                if track != routeList.__len__():
                    track += 1
                refresh()
                print(header)
                PrintList(routeList, track)
                print("\n\n\t\t\033[38;5;136mPRESS (q) To Return\033[38;5;255m\n\n")
                
                
            if keyBuffer[0] == '\x1b' and keyBuffer[1] == 65:
                if track > 0:
                    track -= 1
                refresh()
                print(header)
                PrintList(routeList, track)
                print("\n\n\t\t\033[38;5;136mPRESS (q) To Return\033[38;5;255m\n\n")
                
            if keyBuffer[0] == 10:
                _track = 0
                while True:
                    if _track == 0:
                        refresh()
                        print(header)
                        PrintList(routeList, track)
                        print("\n\t\033[38;5;136mARE YOU SURE YOU WANT TO SELECT THIS ROUTE: (Y/N)\033[38;5;255m")
                        print("\n\n\t\t\033[38;5;136mPRESS (q) To Return\033[38;5;255m\n\n")
                        _track = 1
                    enter = getKey()
                    if enter == 'y' or enter == 'Y':
                        routeIndex = track - 1
                        repository.AssignRouteToUser(routeList[routeIndex], authkeyBuffer.userId)
                        print("\n\033[38;5;40mYOU HAVE BOUGHT A TICKET: \033[38;5;136m[ {} ]\033[38;5;255m".format(routeList[routeIndex]));
                        sleep(1.5)
                        track = 0
                        break
                        
                    elif enter == 'n' or enter == 'N':
                        track = 0
                        break
            
            if keyBuffer[0] == 113:
                return
            
            keyBuffer.clear()