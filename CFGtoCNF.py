import itertools
import sys 
variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5",
"A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6", "U6", "V6", "W6", "X6", "Y6", "Z6",
"A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7", "Y7", "Z7",
"A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8", "N8", "O8", "P8", "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8",
"A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9", "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9",
"A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "K10", "L10", "M10", "N10", "O10", "P10", "Q10", "R10", "S10", "T10", "U10", "V10", "W10", "X10", "Y10", "Z10",
"A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11", "I11", "J11", "K11", "L11", "M11", "N11", "O11", "P11", "Q11", "R11", "S11", "T11", "U11", "V11", "W11", "X11", "Y11", "Z11",
"A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12", "I12", "J12", "K12", "L12", "M12", "N12", "O12", "P12", "Q12", "R12", "S12", "T12", "U12", "V12", "W12", "X12", "Y12", "Z12",
"A13", "B13", "C13", "D13", "E13", "F13", "G13", "H13", "I13", "J13", "K13", "L13", "M13", "N13", "O13", "P13", "Q13", "R13", "S13", "T13", "U13", "V13", "W13", "X13", "Y13", "Z13",
"A14", "B14", "C14", "D14", "E14", "F14", "G14", "H14", "I14", "J14", "K14", "L14", "M14", "N14", "O14", "P14", "Q14", "R14", "S14", "T14", "U14", "V14", "W14", "X14", "Y14", "Z14",
"A15", "B15", "C15", "D15", "E15", "F15", "G15", "H15", "I15", "J15", "K15", "L15", "M15", "N15", "O15", "P15", "Q15", "R15", "S15", "T15", "U15", "V15", "W15", "X15", "Y15", "Z15",
"A16", "B16", "C16", "D16", "E16", "F16", "G16", "H16", "I16", "J16", "K16", "L16", "M16", "N16", "O16", "P16", "Q16", "R16", "S16", "T16", "U16", "V16", "W16", "X16", "Y16", "Z16",
"A17", "B17", "C17", "D17", "E17", "F17", "G17", "H17", "I17", "J17", "K17", "L17", "M17", "N17", "O17", "P17", "Q17", "R17", "S17", "T17", "U17", "V17", "W17", "X17", "Y17", "Z17",
"A18", "B18", "C18", "D18", "E18", "F18", "G18", "H18", "I18", "J18", "K18", "L18", "M18", "N18", "O18", "P18", "Q18", "R18", "S18", "T18", "U18", "V18", "W18", "X18", "Y18", "Z18",
"A19", "B19", "C19", "D19", "E19", "F19", "G19", "H19", "I19", "J19", "K19", "L19", "M19", "N19", "O19", "P19", "Q19", "R19", "S19", "T19", "U19", "V19", "W19", "X19", "Y19", "Z19",
"A20", "B20", "C20", "D20", "E20", "F20", "G20", "H20", "I20", "J20", "K20", "L20", "M20", "N20", "O20", "P20", "Q20", "R20", "S20", "T20", "U20", "V20", "W20", "X20", "Y20", "Z20",
"A21", "B21", "C21", "D21", "E21", "F21", "G21", "H21", "I21", "J21", "K21", "L21", "M21", "N21", "O21", "P21", "Q21", "R21", "S21", "T21", "U21", "V21", "W21", "X21", "Y21", "Z21",
"A22", "B22", "C22", "D22", "E22", "F22", "G22", "H22", "I22", "J22", "K22", "L22", "M22", "N22", "O22", "P22", "Q22", "R22", "S22", "T22", "U22", "V22", "W22", "X22", "Y22", "Z22",
"A23", "B23", "C23", "D23", "E23", "F23", "G23", "H23", "I23", "J23", "K23", "L23", "M23", "N23", "O23", "P23", "Q23", "R23", "S23", "T23", "U23", "V23", "W23", "X23", "Y23", "Z23",
"A24", "B24", "C24", "D24", "E24", "F24", "G24", "H24", "I24", "J24", "K24", "L24", "M24", "N24", "O24", "P24", "Q24", "R24", "S24", "T24", "U24", "V24", "W24", "X24", "Y24", "Z24",
"A25", "B25", "C25", "D25", "E25", "F25", "G25", "H25", "I25", "J25", "K25", "L25", "M25", "N25", "O25", "P25", "Q25", "R25", "S25", "T25", "U25", "V25", "W25", "X25", "Y25", "Z25",
"A26", "B26", "C26", "D26", "E26", "F26", "G26", "H26", "I26", "J26", "K26", "L26", "M26", "N26", "O26", "P26", "Q26", "R26", "S26", "T26", "U26", "V26", "W26", "X26", "Y26", "Z26",
"A27", "B27", "C27", "D27", "E27", "F27", "G27", "H27", "I27", "J27", "K27", "L27", "M27", "N27", "O27", "P27", "Q27", "R27", "S27", "T27", "U27", "V27", "W27", "X27", "Y27", "Z27",
"A28", "B28", "C28", "D28", "E28", "F28", "G28", "H28", "I28", "J28", "K28", "L28", "M28", "N28", "O28", "P28", "Q28", "R28", "S28", "T28", "U28", "V28", "W28", "X28", "Y28", "Z28",
"A29", "B29", "C29", "D29", "E29", "F29", "G29", "H29", "I29", "J29", "K29", "L29", "M29", "N29", "O29", "P29", "Q29", "R29", "S29", "T29", "U29", "V29", "W29", "X29", "Y29", "Z29",
"A30", "B30", "C30", "D30", "E30", "F30", "G30", "H30", "I30", "J30", "K30", "L30", "M30", "N30", "O30", "P30", "Q30", "R30", "S30", "T30", "U30", "V30", "W30", "X30", "Y30", "Z30",
"A31", "B31", "C31", "D31", "E31", "F31", "G31", "H31", "I31", "J31", "K31", "L31", "M31", "N31", "O31", "P31", "Q31", "R31", "S31", "T31", "U31", "V31", "W31", "X31", "Y31", "Z31",
"A32", "B32", "C32", "D32", "E32", "F32", "G32", "H32", "I32", "J32", "K32", "L32", "M32", "N32", "O32", "P32", "Q32", "R32", "S32", "T32", "U32", "V32", "W32", "X32", "Y32", "Z32",
"A33", "B33", "C33", "D33", "E33", "F33", "G33", "H33", "I33", "J33", "K33", "L33", "M33", "N33", "O33", "P33", "Q33", "R33", "S33", "T33", "U33", "V33", "W33", "X33", "Y33", "Z33",
"A34", "B34", "C34", "D34", "E34", "F34", "G34", "H34", "I34", "J34", "K34", "L34", "M34", "N34", "O34", "P34", "Q34", "R34", "S34", "T34", "U34", "V34", "W34", "X34", "Y34", "Z34",
"A35", "B35", "C35", "D35", "E35", "F35", "G35", "H35", "I35", "J35", "K35", "L35", "M35", "N35", "O35", "P35", "Q35", "R35", "S35", "T35", "U35", "V35", "W35", "X35", "Y35", "Z35",
"A36", "B36", "C36", "D36", "E36", "F36", "G36", "H36", "I36", "J36", "K36", "L36", "M36", "N36", "O36", "P36", "Q36", "R36", "S36", "T36", "U36", "V36", "W36", "X36", "Y36", "Z36",
"A37", "B37", "C37", "D37", "E37", "F37", "G37", "H37", "I37", "J37", "K37", "L37", "M37", "N37", "O37", "P37", "Q37", "R37", "S37", "T37", "U37", "V37", "W37", "X37", "Y37", "Z37",
"A38", "B38", "C38", "D38", "E38", "F38", "G38", "H38", "I38", "J38", "K38", "L38", "M38", "N38", "O38", "P38", "Q38", "R38", "S38", "T38", "U38", "V38", "W38", "X38", "Y38", "Z38",
"A39", "B39", "C39", "D39", "E39", "F39", "G39", "H39", "I39", "J39", "K39", "L39", "M39", "N39", "O39", "P39", "Q39", "R39", "S39", "T39", "U39", "V39", "W39", "X39", "Y39", "Z39",
"A40", "B40", "C40", "D40", "E40", "F40", "G40", "H40", "I40", "J40", "K40", "L40", "M40", "N40", "O40", "P40", "Q40", "R40", "S40", "T40", "U40", "V40", "W40", "X40", "Y40", "Z40",
"A41", "B41", "C41", "D41", "E41", "F41", "G41", "H41", "I41", "J41", "K41", "L41", "M41", "N41", "O41", "P41", "Q41", "R41", "S41", "T41", "U41", "V41", "W41", "X41", "Y41", "Z41",
"A42", "B42", "C42", "D42", "E42", "F42", "G42", "H42", "I42", "J42", "K42", "L42", "M42", "N42", "O42", "P42", "Q42", "R42", "S42", "T42", "U42", "V42", "W42", "X42", "Y42", "Z42"]

def readGrammarFile(file): # Membaca file grammar
    Terminal = file.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", "")
    Variables = file.split("Variables:\n")[1].split("Production:\n")[0].replace("Production:\n", "").replace("\n", "")
    RawProd = file.split("Production:\n")[1]
    finalProd = []
    Terminal = Terminal.replace('  ', ' ').split(' ')
    Variables = Variables.replace('  ', ' ').split(' ')
    Rules = RawProd.split("\n")
    for rule in Rules:
        leftproduction = rule.split(' -> ')[0].replace(" ", "")
        rightproduction = rule.split(' -> ')[1].split(" | ")
        for terms in rightproduction:
            finalProd.append((leftproduction, terms.split(' ')))
    return Terminal, Variables, finalProd

def isUnit(rules, Variables): # Menentukan apakah sebuah rule menghasilkan 1 variabel saja
    if (rules[0] in Variables) and rules[1][0] in Variables and len(rules[1]) == 1:
        return True
    else:
        return False

def isOneTerminal(rules, Variables, Terminal): # Menentukan apakah sebuah rule hanya menghasilkan 1 terminal saja
    if rules[0] in Variables and rules[1][0] in Terminal and len(rules[1]) == 1:
        return True
    else:
        return False

def replaceStart(Productions, Variables): # Mengganti Start Symbol menjadi S0 (berjaga-jaga apabila ada rule yang memproduksi start state)
    Variables.append('S0')
    return [('S0', [Variables[0]])] + Productions   

def makeDict(Productions, Variables, Terminal): # Membuat dictionary dengan tiap terminal menjadi key
    dict = {}
    for prod in Productions:
        if prod[0] in Variables and prod[1][0] in Terminal and len(prod[1]) == 1:
            dict[prod[1][0]] = prod[0]
    return dict

def replaceTerminal(Productions, Variables, Terminal): # Mengubah semua rule yang mengandung variabel dan juga terminal, contoh: A->Sa menjadi A -> SZ dan Z -> a
    new_prod = []
    dict = makeDict(Productions, Variables, Terminal) # Membuat dictionary untuk semua terminal
    for rules in Productions:
        if (isOneTerminal(rules, Variables, Terminal)): # Apabila rule hanya menghasilkan 1 terminal saja tidak ada yang perlu diganti
            new_prod.append(rules)
        else:
            for term in Terminal:
                for index, value in enumerate(rules[1]):
                    if term == value and not term in dict:
                        dict[term] = variablesJar.pop()
                        Variables.append(dict[term])
                        new_prod.append((dict[term], [term]))

                        rules[1][index] = dict[term]
                    elif term == value:
                        rules[1][index] = dict[term]
            new_prod.append((rules[0], rules[1]))
    
    return new_prod

def remove2PlusVariable(Productions, Variables): # Menghapus rule rule yang menghasilkan 2 variabel lebih menjadi 2 variabel atau 1 variabel saja
    new_prod = []
    for rules in Productions:
        panjang = len(rules[1])
        if panjang <= 2:
            new_prod.append(rules)
        else:
            temp1 = variablesJar.pop(0)
            Variables.append(temp1+'1')
            new_prod.append((rules[0], [rules[1][0]]+[temp1+'1']))
            i = 1
            
            for i in range(1, panjang-2):
                temp2 = temp1+str(i)
                temp3 = temp1+str(i+1)
                Variables.append(temp3)
                new_prod.append((temp2, [rules[1][i], temp3]))
            new_prod.append((temp1+str(panjang-2), rules[1][panjang-2:panjang]))
    return new_prod

def pisahUnit(rules, variables): # Memisahkan rule yang menjadi 1 variabel saja dengan yang tidak
    unit, non_unit = [], []
    for rule in rules:
        if isUnit(rule, variables):
            unit.append((rule[0], rule[1][0]))
        else:
            non_unit.append(rule)
    
    for rule_unit in unit:
        for rule in rules:
            if rule_unit[1] == rule[0] and rule_unit[0] != rule[0]:
                non_unit.append((rule_unit[0], rule[1]))
    return non_unit

def removeUnit(Productions, Variables): # Menghapus unit production
    i = 0
    new_prod = pisahUnit(Productions, Variables)
    temp = pisahUnit(new_prod, Variables)
    while new_prod != temp and i < 1500:
        new_prod = pisahUnit(temp, Variables)
        temp = pisahUnit(new_prod, Variables)
        i += 1
    return new_prod


def ProdDict(Productions) : # Membuat dictionary untuk production akhir
    new_dict = {}
    for prod in Productions:
        if (prod[0] in new_dict.keys()):
            new_dict[prod[0]].append(prod[1])
        else:
            new_dict[prod[0]] = []
            new_dict[prod[0]].append(prod[1])
    return new_dict

def convertCFG():   # Mengubah CFG menjadi CNF dengan menggunakan function-function diatas
    Terminal, Variabel, Production = [], [], []
    grammar = open('./grammar/grammar.txt').read()
    Terminal, Variabel, Production = readGrammarFile(grammar)
    for var in Variabel:    # Apabila ada variabel yang kebetulan sama dengan variabel dalam variablesJar 
        if var in variablesJar: # maka variabel tersebut akan dihapus dari variablesJar agar tidak terjadi ambiguitas pada dictionary
            variablesJar.remove(var)
    Production = replaceStart(Production, Variabel)
    Production = replaceTerminal(Production, Variabel, Terminal)    
    Production = remove2PlusVariable(Production, Variabel)
    Production = removeUnit(Production, Variabel)
    Production = ProdDict(Production)
    return Production

def displayCNF(rules):
    result = ""
    for key in rules:
        result += key+" -> "+rules[key]+"\n"
    return result

if __name__ == "__main__":
    p = convertCFG()
    print(p)
