from grammar import grammar_convert, grammar_parser
from fileProcessing import token
from CYK import cyk
import argparse,os
import CFGtoCNF

def banner():
    print("                             | |                    ")      
    print("          ___ _ __ ___   ___ | |_ ___             ")          
    print("         / __| '__/ _ \ / _ \| __/ __|          ")                            
    print("        | (__| | | (_) | (_) | |_\__ \        ")                              
    print("         \___|_|  \___/ \___/ \__|___/       ")



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
  t, v, p = grammar_parser.loadGrammar("./grammar/grammar.txt")
  rule = grammar_convert.convertToCNF(p, t, v)
  to_display = grammar_convert.displayCNF(rule)
  print(to_display)
  rule = grammar_convert.productionToDictionary(rule)
  verd = cyk.cyk(convertedTokens, rule)
  print("======================VERDICT=========================")
  print()
  print(verd)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()
