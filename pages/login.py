
import hashlib
from time import sleep
from backend.entities.user import User
from pages.register import FormatRow
from utils.formatvalidate import EmailFormat, PasswordFormat
from utils.getasterisks import GetAsterisks
from utils.menuorexit import MainOrExit
from utils.printregline import PrintRegLine

from utils.screenrefresh import refresh


def GetToken(name):
    hash = hashlib.sha1()
    hash.update(name.encode())
    return hash.digest()

def login(repository, authKey):
    filledLines = [];
    
    #   TEST    ------------------------
    #
    newUser = User()
    newUser.name = "Jonas"
    newUser.email = "email@gmail.com"
    newUser.cpf = "141.567.421-20"
    newUser.password = "Iron71@"
    newUser.id = repository.GetLastUsersID() + 1
    repository.CreateUser(newUser)

    #-----------------------------------
    
    qualified = 0
    
    refresh()
    while True:
        headerFormat = "\033[38;5;25mLOG IN:\033[38;5;136m\n(press \"esc\" to exit)\033[38;5;255m\n\n"
        if(qualified > 0):
            headerFormat += "\033[38;5;196m"
            headerFormat += "Email or Password are invalid\n\n"
            headerFormat += "\033[38;5;255m"
            
        if PrintRegLine(FormatRow("EMAIL:"), 1, headerFormat, EmailFormat, filledLines) == None:
            return False
    
        emailFormat = headerFormat + FormatRow("EMAIL:") + "\t{}\n".format(filledLines[0])
        if PrintRegLine(FormatRow("PASSWORD:"), 1, emailFormat, PasswordFormat, filledLines, False) == None:
            return False
        
        user = repository.FindUserByEmail(filledLines[0])
        if user == None:
            qualified = 1
            filledLines.clear()
            continue
        
        password = user.password
        if(password != user.password):
            qualified = 1
            filledLines.clear()
            continue
        
        authKey.userId = user.id
        authKey.token = GetToken(user.name)

        repository.AuthUser(authKey)
        
        headerFormat = "\033[38;5;25mLOG IN:\033[38;5;255m\n\n"
        emailFormat = headerFormat + FormatRow("EMAIL:") + "\t{}\n".format(filledLines[0])
        hiddenPass = GetAsterisks(filledLines[1])
        passFormat = emailFormat + FormatRow("PASSWORD:") + "\t{}\n".format(hiddenPass)
        refresh()
        
        print(passFormat)
        print('\033[38;5;40m', end="")
        print("\n\nYOU HAVE SUCCESSFULLY LOGGED IN!!\n")
        print('\033[38;5;231m', end="")
        sleep(0.5)
        
        return MainOrExit()