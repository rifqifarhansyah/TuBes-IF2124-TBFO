from grammar import grammar_convert, grammar_parser
from fileProcessing import token
from CYK import cyk
import argparse,os


def banner():
    print(" ____  __.                       _______                               ") 
    print("|    |/ _|____    _____  __ __   \      \ _____    ____ ___.__._____   ") 
    print("|      < \__  \  /     \|  |  \  /   |   \\__  \  /    <   |  |\__  \  ") 
    print("|    |  \ / __ \|  Y Y  \  |  / /    |    \/ __ \|   |  \___  | / __ \_") 
    print("|____|__ (____  /__|_|  /____/  \____|__  (____  /___|  / ____|(____  /") 
    print("        \/    \/      \/                \/     \/     \/\/          \/ ") 


def verdict():
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("file", type = argparse.FileType('r'))
  args = parser.parse_args()
  
  # Banner and verdict
  banner()
  print("\nLoading...")
  print("Checking your codes...")
  print("File name: " + str(args.file.name))
  print()
  
  # Token & CNF
  convertedTokens = token.createToken(str(args.file.name))
#   print(convertedTokens)
  # con = [x.lower() for x in token]
  t, v, p = grammar_parser.loadGrammar("./grammar/grammar.txt")
  rule = grammar_convert.convertToCNF(p, t, v)
  to_display = grammar_convert.displayCNF(rule)
#   print(to_display)
  rule = grammar_convert.productionToDictionary(rule)
  verd = cyk.cyk(convertedTokens, rule)
  res = "Rejected"
  if verd:
    res = "Accepted"
    
  print("======================VERDICT=========================")
  print()
  print(res)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()
