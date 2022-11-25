import os, sys, re

def lexxer(text):
    pos = 0             # Postiton in the text
    posOnLine = 1         # position relative to line as if in javascript code
    line = 1            # current line as in code
    convertedTokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            posOnLine = 1

        flag = None
        for tokenExpr in tokenExprs:
            regPattern, regToken = tokenExpr    
            
            regex = re.compile(regPattern)
            flag = regex.match(text, pos)
            if flag:
                if regToken:
                    convertedTokens.append(regToken)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {posOnLine}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        posOnLine += flag.end(0) - flag.start(0)

    return convertedTokens

tokenExprs = [
    # Not token
    (r'[ \t]+',                                      None), # Skip over whitespaces and tabs
    (r'\/\/[^\n]*',                                  None),
    (r'[\n]*[ \t]*\/\*[(?!(\/\*))\w\W]*\*\/',        None), # Multiline comment
    (r'\n',                                          "nl"),

    (r'\=', "eq"),
    (r'\!\=', "neq"),
    (r'\+\=', "pluseq"),

    (r'\-\=', "mineq"),
    (r'\*\=', "muleq"),
    (r'\/\=', "diveq"),
    (r'\%\=', "modeq"),
    (r'\*\*\=', "poweq"),
    (r'\&\=', "ampeq"),
    (r'\|\=', "boreq"),
    (r'\^\=', "xoreq"),
    (r'\>\>\=', "sreq"),
    (r'\<\<\=', "sleq"),
    (r'\>\>\>\=', "usreq"),
    (r'\&\&\=', "andeq"),
    (r'\|\|\=', "oreq"),
    (r'\?\?', "nullishCoalescingEq"),
    (r'\-\-', "inc"),
    (r'\+\+', "dec"),
    (r'\!', "not"),
    (r'\&\&', "and"),
    (r'\|\|', "or"),
    (r"\=\=", "equal"),
    (r'\=\=\=', "strictEqual"),
    (r'\>', "gt"),
    (r'\>\=', "gte"),
    (r'\<\=', "lte"),
    (r'\<', "lt"),

    (r'\+', "plus"),

    (r'\-', "min"),
    (r'\~', "bnot"),

    (r'\*', "mult"),
    (r'\*\*', "pow"),
    (r'\/', "div"),
    (r'\%', "mod"),
    (r'\+', "plus"),
    (r'\-', "min"),
    (r'\<\<', "sl"),
    (r'\>\>', "sr"),
    (r'\>\>\>', "usr"),
    (r'\&', "amp"),
    (r'\|', "bor"),
    (r'\^', "xor"),

    (r'\bthrow\b', "throw"),
    (r'\"[^\"\n]*\"',           "str"),
    (r'\'[^\'\n]*\'',           "str"),
    (r'[\+\-]?[1-9][0-9]+',     "int"),
    (r'[\+\-]?[0-9]',           "int"),
     #xbo 
    (r'\,', "comma"),
    (r'\?', "question"),
    (r'\bfalse\b', "false"),
    (r'\btrue\b', "true"),
    (r'\bnull\b', "null"),
    (r'\bimport\b', "import"),
    (r'\bfrom\b', "from"),
    (r'\bas\b', "as"),
     #wildcard 
    (r'\{', "lc"),
    (r'\}', "rc"),
    (r'\[', "lb"),
    (r'\]', "rb"),
    (r'\(', "lp"),
    (r'\)', "rp"),

    (r'\belse\b', "else"),
    (r'\bif\b', "if"),
    (r'\bbreak\b', "break"),
    (r'\bcontinue\b', "continue"),
    (r'\bcase\b', "case"),
    (r'\bdefault\b', "default"),
    (r'\bconst\b', "const"),
    (r'\bvar\b', "var"),
    (r'\blet\b', "let"),
    (r'\bin\b', "in"),
    (r'\delete\b', "delete"),
    (r'\bwhile\b', "while"),
    (r'\bfor\b', "for"),
    (r'\bin\b', "in"),
    (r'\;','sc'),
    (r'\breturn\b', "return"),
    (r'\bfunction\b', "function"),
    (r'\bdef\b', "def"),
    (r'\bclass\b', "class"),
    (r'\:', "colon"),
    (r'\bbreak\b', "break"),

    

    # Type
    (r'[A-Za-z_][A-Za-z0-9_]*',   "id"),

  ]

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lexxer(characters)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)


    # Write file
    path = os.getcwd()
    fileWrite = open(path + "/result/tokenResult.txt", 'w')
    for token in tokenResult:
        fileWrite.write(str(token)+" ")
        # print(token)
    fileWrite.close()

    return tokenResult

