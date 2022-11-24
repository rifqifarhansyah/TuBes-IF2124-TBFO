
left, right = 0, 1

def isUnitProduction(prod, variables):
    return prod[left] in variables and len(prod[right]) == 1 and prod[right][0] in variables

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
                result.append(unitP[left], production[right])
    return result

def productionToDictionary(productions):
    res = {}
    for production in productions:
        if (production[left] not in res.keys()):
            res[production[left]] = []
        res[production[left]].append(production[right])
    return res

