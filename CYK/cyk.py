from grammar import grammar_convert, grammar_parser

def cyk(w, grammarCNF):
    length = len(w)

    # Setup matriks set untuk algoritma CYK
    dp = [[set([]) for i in range(length)] for j in range(length)]

    for i in range(length):
        for var in grammarCNF.items():
            for t in var[1]:
                if len(t) == 1 and t[0] == w[i]:
                    dp[i][i].add(var[0])
    
    for l in range(2, length+1):
        for i in range(0, length - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for var in grammarCNF.items():
                    for prod in var[1]:
                        if len(prod) == 2:
                            if prod[0] in dp[i][k] and prod[1] in dp[k+1][j]:
                                dp[i][j].add(var[0])
    print(len(dp[0]))
    print(dp[0][length-1])
    print(dp[0])
    return "S" in dp[0][length-1]