from grammar import grammar_convert, grammar_parser
from fileProcessing import token

# k, v, p = grammar_parser.loadGrammar("grammar/grammar.txt")
# print(p)
# pDict = grammar_convert.productionToDictionary(p)


token = token.createToken("coba.js")
print(token, "oke")
import re

t, v, p = grammar_parser.loadGrammar("./grammar/grammar.txt")
p = grammar_convert.convertToCNF(p, t, v)
res = grammar_convert.displayCNF(p)
print(res)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in car.items():
    print(i[1])
