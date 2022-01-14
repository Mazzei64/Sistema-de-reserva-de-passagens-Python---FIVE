def HasChar(string1, string2):
    for i in range(string1.__len__()):
        for j in range(string2.__len__()):
            if(string1[i] == string2[j]):
                return True
    return False

def HasCharsCount(string1, char, count):
    _count = 0
    for i in range(string1.__len__()):
        if string1[i] == char:
            _count += 1
            if(_count == count):
                return True
    return False

def HasCharsCountStrict(string1, char, count):
    _count = 0
    for i in range(string1.__len__()):
        if string1[i] == char:
            _count += 1
    if _count == count:
        return True
    return False