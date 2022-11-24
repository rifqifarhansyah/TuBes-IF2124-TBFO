from grammar import grammar_convert, grammar_parser
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