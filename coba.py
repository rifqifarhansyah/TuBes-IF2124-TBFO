from grammar import grammar_convert, grammar_parser
from fileProcessing import token
import re

# k, v, p = grammar_parser.loadGrammar("grammar/grammar.txt")
# print(p)
# pDict = grammar_convert.productionToDictionary(p)


token = token.createToken("coba.js")
print(token)


t, v, p = grammar_parser.loadGrammar("./grammar/grammar3.txt")
# print(p)
a = grammar_convert.convertToCNF(p, t, v)
uwa = grammar_convert.displayCNF(a)
print(uwa)
