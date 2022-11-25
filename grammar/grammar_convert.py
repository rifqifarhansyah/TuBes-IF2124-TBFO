
left, right = 0, 1

# def generateBooleanMatrix(n):
#     res = [[0 for i in range(2**n)] for i in range(n)]


# def isEpsilon(prod, productions):
#     allProd = getAllLeft(productions, prod)
#     for production in allProd:
#         if len(production[right]):
#             return True
#     return False

# def isEpsilonImmutable(prod, variables, productions):
#     if isEpsilon(prod, variables, productions):
#         allLeft = getAllLeft(productions, prod[left])
#         return len(allLeft) == 1
#     return False

# def getAllLeft(prod, leftProd):
#     result = []
#     for production in prod:
#         if production[left] == leftProd:
#             result.append(production)
#     return result

# def adjustEpsilon(prodList):


# def epsilonRoutine(prodList, variables):
#     newProdList = prodList.copy()
#     for production in prodList:
#         if not isEpsilonImmutable(production, variables, prodList):
#             newProdList.append(production)
#     toAdd = []
#     for production in prodList:
#         if isEpsilon(production, prodList):
#             allLeft = getAllLeft(production, prodList)
#         else:

def getAllLeft(productions, lhs):
    result = []
    for production in productions:
        if production[left] == lhs:
            result.append(production)
    return result

def hasUnitProduction(prod, variables):
    for production in prod:
        if isUnitProduction(production, variables):
            return True
    return False

def generatingProduction(productions, terminals, variables):
    result = {}
    for production in productions:
        if production[left] in variables and production[right][0] in terminals and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result

def isUnitProduction(prod, variables):
    a = prod[left] in variables
    b = len(prod[right]) == 1
    c = prod[right][0] in variables
    if prod[left] in variables and len(prod[right]) == 1 and prod[right][0] in variables:
        return True
    else:
        return False

def isSimpleForm(t, var, prod):
    return prod[left] in var and len(prod[right]) == 1 and prod[right][0] in t

def removeUnitProduction(productions, variables):
    unitaries, result = [], []
    for production in productions:
        if isUnitProduction(production, variables):
            unitaries.append((production[left], production[right][0]))
        else:
            result.append(production)
    for unitP in unitaries:
        for production in productions:
            if unitP[right] == production[left] and unitP[left] != production[left]:
                result.append((unitP[left], production[right]))
    return result

def unitProductionRoutine(productions, variables):
    unitaries, result = [], []
    for production in productions:
        if isUnitProduction(production, variables):
            unitaries.append((production[left], production[right]))
        else:
            result.append(production)
    visited = []
    while hasUnitProduction(unitaries, variables):
        for unitP in unitaries:
            if (isUnitProduction(unitP, variables)):
                for production in productions:
                    if unitP[right][0] == production[left] and unitP[left] != production[left] and not production[left] in visited:
                        visited.append(production[left])
                        allSameVar = getAllLeft(productions, production[left])
                        for same in allSameVar:
                            currProd = (unitP[left], same[right])
                            if currProd not in unitaries:
                                unitaries.append(currProd)
            unitaries.remove(unitP)

    for unitP in unitaries:
        result.append(unitP)

    return result
    

def productionToDictionary(productions):
    res = {}
    for production in productions:
        if (production[left] not in res.keys()):
            res[production[left]] = []
        res[production[left]].append(production[right])
    return res

def convertToCNF(productions, terminals, variables):
    
    # Membuat sebuah start state
    nVar = variables + ['S0']
    rules = [('S0', [variables[0]])] + productions

    
    # Hapus produksi yang menghasilkan variable dan terminal sekaligus
    new_prod = []
    dictionary = generatingProduction(rules, terminals, nVar)
    num = 1
    for prod in rules:
        if isSimpleForm(terminals, nVar, prod):
            new_prod.append(prod)
        else:
            for t in terminals:
                for i, v in enumerate(prod[right]):
                    if t == v and not t in dictionary:
                        dictionary[t] = 'A' + str(num)
                        num += 1
                        nVar.append(dictionary[t])
                        new_prod.append((dictionary[t], t))
                        prod[right][i] = dictionary[t]
                    elif t == v:
                        prod[right][i] = dictionary[t]
            new_prod.append((prod[left], prod[right]))
    rules = new_prod

    # Meringkas semua produksi yang menghasilkan lebih dari dua variabel
    result = []
    for production in rules:
        k = len(production[right])
        if k <= 2:
            result.append(production)
        else:
            curVar = 'A' + str(num)
            nVar.append(curVar+'1')
            result.append((production[left], [production[right][0]]+[curVar+'1']))
            for i in range(1, k-2 ):
                var, var2 = curVar+str(i), curVar+str(i+1)
                nVar.append(var2)
                result.append((var, [production[right][i], var2]))
            result.append((curVar+str(k-2), production[right][k-2:k])) 
            num += 1
    rules = result
    result = unitProductionRoutine(rules, nVar)
    rules = result
    return rules

def displayCNF(rules):
	dictionary = {}
	for rule in rules:
		if rule[left] in dictionary:
			dictionary[rule[left]] += ' | '+' '.join(rule[right])
		else:
			dictionary[rule[left]] = ' '.join(rule[right])
	result = ""
	for key in dictionary:
		result += key+" -> "+dictionary[key]+"\n"
	return result
        

