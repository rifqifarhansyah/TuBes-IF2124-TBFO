from grammar import grammar_convert, grammar_parser

k, v, p = grammar_parser.loadGrammar("grammar/grammar.txt")
print(p)
pDict = grammar_convert.productionToDictionary(p)