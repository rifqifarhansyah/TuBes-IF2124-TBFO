import CFGtoCNF
import argparse
from grammar import grammar_convert, grammar_parser
from CYK import cyk
from fileProcessing import token

parser = argparse.ArgumentParser(description='Syntax linting for javascript.')
parser.add_argument('filename', type=str, help="The name of the file that is meant to lint")
args = parser.parse_args()

p = CFGtoCNF.convertCFG()
w = token.createToken(args.filename)
accepted = cyk.cyk(w, p)
print(accepted)

