import os, sys, re

def lexxer(text):
    pos = 0             # Postiton in the text
    currPos = 1         # position relative to line as if in javascript code
    line = 1            # current line as in code
    convertedTokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr    
            
            regex = re.compile(pattern)
            flag = regex.match(text, pos)

            if flag:
                # texts = flag.group(0)
                if tag:
                    token = tag
                    convertedTokens.append(token)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {currPos}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        currPos += 1

    return convertedTokens

tokenExprs = [
    # Not token
    (r'[ \t]+',                                      None), # Skip over whitespaces and tabs
    (r'#[^\n]*',                                     None),
    (r'\/\*[\n]+[ \t]*[(?!(\*\/))\w\W]\*\/',                    None), # Comments inline
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',             "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',             "MULTILINE"),
    (r'\n',                                          "NEWLINE"),

    # Operator
    (r'\^', "XORS"),
    (r'\&', "ANDS"),
    (r'\|', "ORS"),
    (r'\!', "SERU"),
    (r'\?', "QUEST"),
    (r'\%', "PERSEN"),
    (r'\.', "DOTS"),
    (r'\#', "HASHTAG"),
    (r'\$', "DOLLAR"),
    (r'\(', "NBO"),
    (r'\)', "NBC"),
    (r'\~', "WAVE"),
    (r'\*', "MUL"),
    (r'\*\*', "POW"),
    (r'\+', "PLUS"),
    (r'\+\+', "INCR"),
    (r'\-', "MIN"),
    (r'\-\-', "DECR"),
    (r'\,', "COMMA"),
    (r'\\', "DIVIDE"),
    (r'\:', "COLON"),
    (r'\<', "LESS"),
    (r'\=', "EQUAL"),
    (r'\>', "GREAT"),
    (r'\[', "SBO"),
    (r'\]', "SBC"),
    (r'\_', "UNDERSCORE"),
    (r'\{', "CBO"),
    (r'\}', "CBC"),
    (r'\'', "PETIK1"),
    (r'\"', "PETIK2"),
    (r'\;', "SEMICOLON"),

    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    # (r'\bdict\b',               "TYPE"),
    # (r'\bint\b',                "TYPE"),
    # (r'\bstr\b',                "TYPE"),
    # (r'\bfloat\b',              "TYPE"),
    # (r'\bcomplex\b',            "TYPE"),
    # (r'\blist\b',               "TYPE"),
    # (r'\btuple\b',              "TYPE"),

    # keyword
    (r'\bnew\b',                "NEWS"),
    (r'\bthis\b',                "THISS"),
    (r'\bnull\b',                "NULLS"),
    (r'\binstanceof\b',                "INSTANCEOFS"),
    (r'\bnone\b',                "NONES"),
    (r'\bdelete\b',                "DELETES"),
    (r'\bswitch\b',                "SWITCHS"),
    (r'\bcase\b',                "CASES"),
    (r'\bvoid\b',                "VOIDS"),
    (r'\btypeof\b',                "TYPEOFS"),
    (r'\band\b',                "ANDS"),
    (r'\btry\b',                "TRYS"),
    (r'\bor\b',                "ORS"),
    (r'\bis\b',                "ISS"),
    (r'\bin\b',                "INS"),
    (r'\bnot\b',                "NOTS"),
    (r'\btrue\b',                "TRUES"),
    (r'\bfalse\b',                "FALSES"),
    (r'\bfor\b',                "FORS"),
    (r'\bdo\b',                "DOS"),
    (r'\bwhile\b',                "WHILES"),
    (r'\belse\b\bif\b',                "ELIFS"),
    (r'\bif\b',                "IFS"),
    (r'\belse\b',                "ELSES"),
    (r'\bbreak\b',                "BREAKS"),
    (r'\bcontinue\b',                "CONTINUES"),
    (r'\bfinally\b',                "FINALLYS"),
    (r'\bcatch\b',                "CATCHS"),
    (r'\bfunction\b',                "FUNCTIONS"),
    (r'\breturn\b',                "RETURNS"),
    (r'\bclass\b',                "CLASS"),
    (r'\bfrom\b',                "FROMS"),
    (r'\bimport\b',                "IMPORTS"),
    (r'\bvar\b',                "VAR"),
    (r'\bexport\b',                "EXPORT"),
    (r'\bextends\b',                "EXTENDSS"),
    (r'\blet\b',                   "LETS"),
    (r'\bconst\b',                "CONSTS"),
    (r'\bsuper\b',                "SUPERS"),
    (r'\bwith\b',                "WITHS"),
    (r'\byield\b',                "YIELDS"),
    (r'\bdefault\b',                "DEFAULTS"),
    (r'\bthrow\b',                "THROWS"),
    (r'\bstatic\b',                "STATIC"),

    # Exception for variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),
  ]

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters)
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
