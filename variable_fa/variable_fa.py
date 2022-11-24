def astate1(c) :
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or ord(c) == 95:
        return 2
    else:
        return 3

def astate2(c):
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or ord(c) == 95 or (ord(c) >= 48 and ord(c) <= 57):
        return 2
    else:
        return 3

def astate3(c):
    return 3

def bstate1(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return 1
    else:
        return 2

def bstate2(c):
    return 2

def isValidVarName(s):
    state = 1
    for i in range(len(s)):
        if state == 1:
            state = astate1(s[i])
        elif state == 2:
            state = astate2(s[i])
        else:
            state = astate3(s[i])
    return state == 2

def isNumber(s):
    state = 1
    for i in range(len(s)):
        if state == 1:
            state = bstate1(s[i])
        else:
            state = bstate2(s[i])
    return state == 1