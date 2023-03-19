from src.file_parser import get_alphabet_and_rules


class Rule:
    def __init__(self, non_term_: str, derivation_: str):
        self.non_term = non_term_
        self.derivation = derivation_

    def __hash__(self):
        return hash(self.non_term) + hash(self.derivation)


class State:
    def __init__(self, rule_: Rule, dot_pos_: int, left_bound_: int):
        self.rule = rule_
        self.dot_pos = dot_pos_
        self.left_bound = left_bound_

    def fulfilled(self):
        return self.dot_pos >= len(self.rule.derivation)

    def __eq__(self, __o: object):
        return (
            hasattr(__o, "rule")
            and hasattr(__o, "dot_pos")
            and hasattr(__o, "left_bound")
            and self.rule == getattr(__o, "rule")
            and self.dot_pos == getattr(__o, "dot_pos")
            and self.left_bound == getattr(__o, "left_bound")
        )

    def __hash__(self):
        return hash(self.rule) * hash(self.dot_pos) * hash(self.left_bound)


class Grammar:
    def __init__(self, file_path: str):
        with open(file_path) as file:
            self.uppercase_alphabet, self.rules = get_alphabet_and_rules(file)
        self.rules["S'"].append(Rule("S'", "S"))
        self.uppercase_alphabet.add("S'")
        self.eliminate_epsilon()

    def eliminate_epsilon(self):
        for non_term in self.uppercase_alphabet:
            for rule in self.rules[non_term]:
                rule.derivation = rule.derivation.replace('$', '')

    def scan(self, states, level: int, word: str):
        for state in states[level - 1]:
            if not state.fulfilled():
                if state.rule.derivation[state.dot_pos] == word[level - 1]:
                    states[level].add(
                        State(state.rule, state.dot_pos + 1, state.left_bound))

    def complete(self, states, level: int):
        prev_set = states[level].copy()
        for state in prev_set:
            if not state.fulfilled():
                continue
            for prev_state in states[state.left_bound].copy():
                if not prev_state.fulfilled() and \
                        prev_state.rule.derivation[prev_state.dot_pos] == state.rule.non_term:
                    states[level].add(
                        State(prev_state.rule, prev_state.dot_pos + 1, prev_state.left_bound))
        return prev_set != states[level]

    def predict(self, states, level: int):
        prev_set = states[level].copy()
        for state in prev_set:
            if state.fulfilled():
                continue
            if state.rule.derivation[state.dot_pos] in self.uppercase_alphabet:
                for rule in self.rules[state.rule.derivation[state.dot_pos]]:
                    states[level].add(State(rule, 0, level))
        return prev_set != states[level]

    def word_is_suitable(self, word: str):
        word = word.replace('$', '')
        if len(word) == 0:
            for rule in self.rules['S']:
                if len(rule.derivation) == 0:
                    return True
            return False
        states = [set()]
        states[0].add(State(self.rules["S'"][0], 0, 0))
        for level in range(len(word) + 1):
            states.append(set())
            if level != 0:
                self.scan(states, level, word)
            while self.complete(states, level) or self.predict(states, level):
                continue
        finish_state = State(self.rules["S'"][0], 1, 0)
        return finish_state in states[len(word)]
