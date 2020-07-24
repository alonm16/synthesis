"""if every nonterminal in the programs is already in a program we created then a new program can be created"""
def can_create_program(non_terminals,keys):
    for non_terminal in non_terminals:
        if not non_terminal in keys:
            return False
    return True


def create_programs(P, rule): #not good!
    new_programs = []
    for symbol in rule:
        if symbol.isupper():
            for i in range(len(new_programs)):
                for old_program in P[symbol]:
                    new_programs[i] += old_program
        else:
            for i in range(len(new_programs)):
                new_programs[i] += symbol #TODO check whether its a function
    return new_programs



def grow(P, derivation_rules, spec):  #Todo pruning and child form last iteration
    keys = P.keys()
    new_programs = {}
    for derivation_rule in derivation_rules:
        for single_rule in derivation_rule[1]:
            non_terminals = [symbol for symbol in single_rule if symbol.isupper()]
            if can_create_program(non_terminals, keys):
                new_programs[derivation_rule[0]] += [create_programs(P, single_rule)]
    return new_programs


def validate(p, spec):
    for (i, o) in spec:
        if eval(p, {"__builtins__": None}, {'i': i}) != o:
            return False
    return True


def parse_grammer(grammer):
    derivation_rules = {}
    terminals_rules = {}
    for derivation_rule in grammer:
        left, right = derivation_rule.split('::=')
        right = right.split()
        if len(right) == 1 and not (right[0]).isupper():
            if left not in terminals_rules.keys():
                terminals_rules[left] = []
            terminals_rules[left] += [right]
        if left not in derivation_rules.keys():
            derivation_rules[left] = []
        derivation_rules[left] += [right]
    return derivation_rules, terminals_rules


def bottom_up(grammer, spec):
    derivation_rules, terminals_rules = parse_grammer(grammer)
    P = terminals_rules
    while True:
        new_programs = grow(P, derivation_rules, spec)
        if not new_programs:
            return 'no program'
        P += new_programs
        for p in P:
            if p[0] == 'S' and validate(p[1], spec):  #assuming p is a tuple of (V, program)
                return p


if __name__ == "__main__":
    grammer, terminals = parse_grammer(["C ::= 'a'", "C ::= 'b'", "C ::= 'c'", "S ::= C", "S ::= ( S + S )"
            , "S ::= ( S * N )", "S ::= S [ N ]" , "S ::= x", "N ::= 0", "N ::= 1", "N ::= ( N + N )"])
    print("grammer")
    print(grammer)
    print("terminals")
    print(terminals)
