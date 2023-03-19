import src.grammar as grammar

GR = grammar.Grammar("./tests/local_grammar.txt")
word = input("Print a word to test for belonging to your grammar:\n")
print("In grammar" if GR.word_is_suitable(word) else "Not in grammar")
