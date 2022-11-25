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


def read_input(filename):
    """
    Membaca file input.py di folder yang sama dan mengubahnya menjadi sebuah string.
    """

    # filename = os.path.join(os.curdir, ("./test/" + filename))
    with open(filename) as input_file:
        lines = input_file.readlines()
        input_string = ''

        for line in lines:
            input_string += line.strip('\t').strip(' ')
        
        input_string += '\n'
    return input_string

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
  print(convertedTokens)
  # con = [x.lower() for x in token]
  t, v, p = grammar_parser.loadGrammar("./grammar/grammar3.txt")
  rule = grammar_convert.convertToCNF(p, t, v)
  rule = grammar_convert.productionToDictionary(rule)
  print("======================VERDICT=========================")
  print()
  verd = cyk.cyk(convertedTokens, rule)
  print(verd)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()
