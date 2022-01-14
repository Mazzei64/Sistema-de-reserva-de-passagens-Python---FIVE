
from time import sleep
from backend.entities.user import User
from utils.menuorexit import MainOrExit
from utils.printregline import PrintRegLine
from utils.formatvalidate import CPFFormat, EmailFormat, NameFormat, PasswordFormat
from utils.getasterisks import GetAsterisks
from utils.screenrefresh import refresh

def FormatRow(row):
    return "\033[48;5;255m\033[38;5;0m " + row + "\033[48;5;233m\033[38;5;255m"

def register(repository):    
    filledLines = [];
    
    while True:
        headerFormat = "\033[38;5;25mREGISTER A NEW USER:\n\033[38;5;136m(press \"esc\" to exit)\033[38;5;255m\n\n"
        if PrintRegLine(FormatRow("NAME:"), 1, headerFormat, NameFormat, filledLines) == None:
            return False
        
        nameFormat = headerFormat + FormatRow("NAME:") + "\t{}\n".format(filledLines[0])
        if PrintRegLine(FormatRow("EMAIL:"), 1, nameFormat, EmailFormat, filledLines) == None:
            return False
        
        emailFormat = nameFormat + FormatRow("EMAIL:") + "\t{}\n".format(filledLines[1])
        if PrintRegLine(FormatRow("CPF:"), 1, emailFormat, CPFFormat, filledLines) == None:
            return False
        
        PASSVAL = 0
        while True:
            wrongConfirmError = "\033[38;5;196mPASSWORD CONFIRMATION MUST BE THE SAME AS PASSWORD\033[38;5;255m"
            if(PASSVAL == 1):
                cpfFormat = emailFormat + FormatRow("CPF:") + "\t{}\n{}\n".format(filledLines[2], wrongConfirmError)
            else:    
                cpfFormat = emailFormat + FormatRow("CPF:") + "\t{}\n".format(filledLines[2])
                
            if PrintRegLine(FormatRow("PASSWORD:"), 1, cpfFormat, PasswordFormat, filledLines, False) == None:
                return False

            hiddenPass = GetAsterisks(filledLines[3])
            passwordFormat = cpfFormat + FormatRow("PASSWORD:") + "\t{}\n".format(hiddenPass)
            if PrintRegLine(FormatRow("CONFIRM PASSWORD:"), 1, passwordFormat, PasswordFormat, filledLines, False) == None:
                return False
            
            if (filledLines[3] != filledLines[4]):
                filledLines.pop()
                filledLines.pop()
                PASSVAL = 1
            else:
                refresh()
                hiddenPassConf = GetAsterisks(filledLines[4])
                emailFormat = nameFormat + FormatRow("EMAIL:") + "\t{}\n".format(filledLines[1])
                cpfFormat = emailFormat + FormatRow("CPF:") + "\t{}\n".format(filledLines[2])
                passwordFormat = cpfFormat + FormatRow("PASSWORD:") + "\t{}\n".format(hiddenPass)
                print(passwordFormat + FormatRow("CONFIRM PASSWORD:") + "\t{}\n".format(hiddenPassConf))
                break
            
        newUser = User()
        newUser.name = filledLines[0]
        newUser.email = filledLines[1]
        newUser.cpf = filledLines[2]
        newUser.password = filledLines[3]
        newUser.id = repository.GetLastUsersID() + 1
        repository.CreateUser(newUser)
        
        filledLines.clear()
        
        print('\033[38;5;40m', end="")
        print("YOU'VE BEEN SUCCESSFULLY REGISTERED!!\n")
        print("\t\tWELCOME!")
        print('\033[38;5;231m', end="")
        sleep(0.5)
        
        if MainOrExit() == True:
            return