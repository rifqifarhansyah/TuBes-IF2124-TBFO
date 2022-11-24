from grammar import grammar_convert, grammar_parser
from fileProcessing import token

# k, v, p = grammar_parser.loadGrammar("grammar/grammar.txt")
# print(p)
# pDict = grammar_convert.productionToDictionary(p)


token = token.createToken("coba.js")
print(token, "oke")