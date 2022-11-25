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

            # varRegex = re.compile(r'[A-Za-z0-9_]*')
            # varFlag = varRegex.match(text, pos)
            # print(flag)
            if flag:
                # texts = flag.group(0)
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
    # sc apa

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

    # bnot apa
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
     #xbo apa
    (r'\,', "comma"),

    (r'\?', "question"),

    (r'\bfalse\b', "false"),
    (r'\btrue\b', "true"),
    (r'\bnull\b', "null"),
    (r'\bimport\b', "import"),
    (r'\bfrom\b', "from"),
    (r'\bas\b', "as"),
     #wildcard apa
  
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

    

    



    # (r'\>', "GREAT"),
    # (r'\[', "SBO"),
    # (r'\]', "SBC"),
    # (r'\_', "UNDERSCORE"),
    # (r'\{', "CBO"),
    # (r'\}', "CBC"),
    # (r'\'', "PETIK1"),
    # (r'\"', "PETIK2"),
    # (r'\;', "SEMICOLON"),

    # Special char or number

    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),
    # (r'',       ""),

    # Type
    (r'[A-Za-z_][A-Za-z0-9_]*',   "id"),
    # (r'[a-zA-Z]',               "ALPHABET"),
    # (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    # (r'[\+\-]?[1-9][0-9]+',     "INT"),
    # (r'[\+\-]?[0-9]',           "INT"),
    # (r'\"[^\"\n]*\"',           "STRING"),
    # (r'\'[^\'\n]*\'',           "STRING"),

    # keyword
    # (r'\bnew\b',                    "NEWS"),
    # (r'\bthis\b',                   "THISS"),
    # (r'\bnull\b',                   "NULLS"),
    # (r'\binstanceof\b',             "INSTANCEOFS"),
    # (r'\bnone\b',                   "NONES"),
    # (r'\bdelete\b',                 "DELETES"),
    # (r'\bswitch\b',                 "SWITCHS"),
    # (r'\bcase\b',                   "CASES"),
    # (r'\bvoid\b',                   "VOIDS"),
    # (r'\btypeof\b',                 "TYPEOFS"),
    # (r'\band\b',                    "ANDS"),
    # (r'\btry\b',                    "TRYS"),
    # (r'\bor\b',                     "ORS"),
    # (r'\bis\b',                     "ISS"),
    # (r'\bin\b',                     "INS"),
    # (r'\bnot\b',                    "NOTS"),
    # (r'\btrue\b',                   "TRUES"),
    # (r'\bfalse\b',                  "FALSES"),
    # (r'\bfor\b',                    "FORS"),
    # (r'\bdo\b',                     "DOS"),
    # (r'\bwhile\b',                  "WHILES"),
    # (r'\belse if\b',                "ELIFS"),
    # (r'\bif\b',                     "IFS"),
    # (r'\belse\b',                   "ELSES"),
    # (r'\bbreak\b',                  "BREAKS"),
    # (r'\bcontinue\b',               "CONTINUES"),
    # (r'\bfinally\b',                "FINALLYS"),
    # (r'\bcatch\b',                  "CATCHS"),
    # (r'\bfunction\b',               "FUNCTIONS"),
    # (r'\breturn\b',                 "RETURNS"),
    # (r'\bclass\b',                  "CLASS"),
    # (r'\bas\b',                     "ASS"),
    # (r'\bfrom\b',                   "FROMS"),
    # (r'\bimport\b',                 "IMPORTS"),
    # (r'\bexport\b',                 "EXPORT"),
    # (r'\bextends\b',                "EXTENDSS"),
    # (r'\blet\b',                    "LETS"),
    # (r'\bvar\b',                    "VAR"),
    # (r'\bconst\b',                  "CONSTS"),
    # (r'\bsuper\b',                  "SUPERS"),
    # (r'\bwith\b',                   "WITHS"),
    # (r'\byield\b',                  "YIELDS"),
    # (r'\bdefault\b',                "DEFAULTS"),
    # (r'\bthrow\b',                  "THROWS"),
    # (r'\bstatic\b',                 "STATIC"),
    # (r'\btarget\b',                 "TARGET"),

    # Exception for variable
    # (r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),
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

# if __name__ == "__main__": 
#     path = os.getcwd()
#     createToken(path + "/test/inputAcc.txt")
