def loadGrammar(grammarPath):
    file = open(grammarPath).read()
    T = file.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", "")
    V = file.split("Variables:\n")[1].split("Production:\n")[0].replace("\n", "")
    P = file.split("Production:\n")[1]

    T = T.replace('  ',' ').split(' ')
    V = V.replace('  ',' ').split(' ')

    pArr = []
    
    rawProduction = P.split("\n")
    for production in rawProduction:
        huhah = production.split(" -> ")
        lhs = production.split(" -> ")[0].replace(" ", '')
        rhs = production.split(" -> ")[1].split(" | ")
        for term in rhs:
            pArr.append((lhs, (term.split(" "))))
    
    return T, V, pArr

if __name__ == "__main__":
    k, v, p = loadGrammar("./grammar/grammar3.txt")
    print(k)
    print(v)
    print(p)