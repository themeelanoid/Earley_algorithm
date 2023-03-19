import src.grammar as grammar
import pytest


def test_word():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("aac")


def test_epsilon():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("aa$c")


def test_empty_word():
    GR = grammar.Grammar("./tests/test_homskiy.txt")
    assert GR.word_is_suitable("$$$")


def test_no_empty_word():
    GR = grammar.Grammar("./tests/test_no_eps.txt")
    assert not GR.word_is_suitable("$$$")


@pytest.mark.parametrize(("word", "answer"), [("aabaa", False), ("ababbbaba", True), ("aabbbabbabab", True)])
def test_huge(word, answer):
    GR = grammar.Grammar("./tests/test_huge.txt")
    assert GR.word_is_suitable(word) == answer
