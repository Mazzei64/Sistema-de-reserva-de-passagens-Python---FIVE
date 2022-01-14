from utils.haschar import HasChar, HasCharsCountStrict

def NameFormat(name):
    unwantedChars = '!@#$%*()_1234567890-=+[{]\}|],.<>;:/?"\\\''
    discard = HasChar(name, unwantedChars)
    if(discard):
        return False
    return True

def EmailFormat(email):
    commonChars = 'qwertyuiopasdfghjklçzxcvbnm'    
    discard = HasCharsCountStrict(email, '@', 1) & HasCharsCountStrict(email, '.', 1) & HasChar(email, commonChars)
    if(not discard):
        return False
    return True


def CPFFormat(cpf):
    discard = True
    length = len(cpf)
    steps = 0
    founds = 0
    for i in range(length - 3):
        if(steps == 3 and cpf[i] == '.'):
            founds += 1
            steps = -1
        steps += 1
    
    if founds != 2:
        discard = False
    
    if(not cpf[(length - 6):-3].isdigit() or len(cpf[(length - 6):-3]) != 3):
        discard = False
    
    if(not cpf[(length - 2):].isdigit() or len(cpf[(length - 2):]) != 2 or cpf[length - 3:-2] != '-'):
        discard = False
    
    return discard

def PasswordFormat(password):
    numChars = '1234567890'
    signChars = '!@#$%*()-_=+\'`[{~^]},<.>;:/?\\|"'
    capsChars = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
    discard = HasChar(password, numChars) & HasChar(password, signChars) & HasChar(password, capsChars)
    if(not discard):
        return False
    return True

def StringGetDigits(string):
    _string = ""
    strDigits = '1234567890'
    for i in range(string.__len__()):
        for j in range(strDigits.__len__()):
            if(string[i] == strDigits[j]):
                _string += string[i]
    return _string