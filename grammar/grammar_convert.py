
import copy

left, right = 0, 1

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
    i = 0
    while hasUnitProduction(unitaries, variables) and i < 500:
        visited = []
        for unitP in unitaries:
            remove = False
            if (isUnitProduction(unitP, variables)):
                for production in productions:
                    if unitP[right][0] == production[left] and unitP[left] != production[left] and not production[left] in visited:
                        visited.append(production[left])
                        allSameVar = getAllLeft(productions, production[left])
                        for same in allSameVar:
                            currProd = (unitP[left], same[right])
                            if currProd not in unitaries:
                                remove = True
                                unitaries.append(currProd)
            unitaries.remove(unitP)
            if not remove:
                unitaries.append(unitP)
        i += 1


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
                        new_prod.append((dictionary[t], [t]))
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
    result = removeUnitProduction(rules, nVar)
    temp = removeUnitProduction(result, nVar)
    i = 0
    while result != temp and i < 1000:
        result = removeUnitProduction(rules, nVar)
        temp = removeUnitProduction(result, nVar)
        i += 1
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
        

