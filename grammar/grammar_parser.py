import itertools

def loadGrammar(grammarPath):
    file = open(grammarPath).read()
    T = file.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", "")
    V = file.split("Variables:\n")[1].split("Productions:\n")[0].replace("\n", "")
    P = file.split("Productions:\n")[1]

    T = T.replace('  ',' ').split(' ')
    V = V.replace('  ',' ').split(' ')

    pArr = []
    
    rawProduction = P.replace("\n", "").split(";")
    for production in rawProduction:
        lhs = production.split(" -> ")[0].replace(" ", '')
        rhs = production.split(" -> ")[0].split(" | ")
        for term in rhs:
            pArr.append((lhs, (term.split(" "))))
    
    return T, V, pArr