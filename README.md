# Earley algorithm implementation / Formal Languages course project
## Few words to say...
This is yet another implementation of __Earley algorithm__, which checks, whether given word can be derived by given grammar or not.

In my implementation empty word is __$__, nonterminal symbols are uppercase letters and terminal symbols are lowercase letters. Starting nonterminal symbol is __S__.
## Usage
Put the grammar into "__tests/local_grammar.txt__" in format: **Non_terminal_character -> Derivation** (e.g. S -> AaB). Execute __main.py__ and type the word in terminal.

There are also pytests included in project ("__./tests/test_words.py__"), to start them enter:

> make test

Coverage test:

> make test-cov

Coverage information is collected in ("__./htmlcov/index.html__").