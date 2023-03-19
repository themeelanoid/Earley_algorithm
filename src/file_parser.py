from collections import defaultdict
import src.grammar as grammar


def get_alphabet_and_rules(file):
    lines = [line.rstrip() for line in file.readlines() if not line.isspace()]
    words = list()
    uppercase_alphabet = set()
    rules = defaultdict(list)
    for line in lines:
        non_term = line.split()[0]
        uppercase_alphabet.add(non_term)
        derivation = line.split()[-1]
        rules[non_term].append(grammar.Rule(non_term, derivation))
    return uppercase_alphabet, rules
