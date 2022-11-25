from grammar import grammar_convert, grammar_parser
import re

t, v, p = grammar_parser.loadGrammar("./grammar/grammar2.txt")
# print(p)
grammar_convert.convertToCNF(p, t, v)
uwa = grammar_convert.displayCNF(p)
print(uwa)