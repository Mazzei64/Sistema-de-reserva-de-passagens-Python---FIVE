import sys
from .readfromstream import ReadFromStream
from .screenrefresh import refresh

def PrintRegLine(title, option, previousFormat, ConditionFunc, storage, show = True):
    INVALID = 0
    TRACK = 0
    refresh()
    while True:
        if((TRACK & option) != 0):
            if(previousFormat != ""):
                print(previousFormat, end="")
            print('\033[38;5;196m', end="")
            print("WRONG {} TRY AGAIN!".format(title)) #INVALID
            print('\033[38;5;255m', end="")
            print("{}:\t".format(title), end="")
            sys.stdout.flush()
            read = ReadFromStream(show)
            if read == "":
                return None
            if(ConditionFunc(read)):
                refresh()
                print('{}:\t'.format(title) + read)
                INVALID |= option
                storage.append(read)
                return INVALID
            refresh()
            continue
        
        if(previousFormat != ""):
            print(previousFormat, end="")
        print("{}\t".format(title), end="")
        sys.stdout.flush()
        read = ReadFromStream(show)
        if read == "":
                return None
        if(ConditionFunc(read)):
            INVALID |= option
            storage.append(read)
            return INVALID
        refresh()
        TRACK |= option