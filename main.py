import time

"""if every nonterminal in the programs is already in a program we created then a new program can be created"""
def can_create_program(non_terminals,keys):
    for non_terminal in non_terminals:
        if not non_terminal in keys:
            return False
    return True


def create_programs(P, rule):
    if len(rule) == 1 and not rule[0].isupper():
        return []
    new_programs = []
    for symbol in rule:
        cur_len = len(new_programs)
        if symbol.isupper():
            for i in range(cur_len):
                iteration_programs = []
                for old_program in P[symbol]:
                    iteration_programs += [new_programs[i] + old_program]
                new_programs += iteration_programs
            new_programs = new_programs[cur_len:]
            if cur_len == 0:
                for old_program in P[symbol]:
                    new_programs += [old_program[:]]
        else:
            for i in range(cur_len):
                new_programs[i] += symbol
            if cur_len == 0:
                new_programs = [[symbol]]
    print(len(new_programs))
    return new_programs


"""iterating other all the derivation rules and if a rule can be applied a new program is created"""
def grow(P, derivation_rules, spec):  #Todo pruning and child form last iteration
    keys = P.keys()
    new_programs = {}
    for var in derivation_rules:
        for single_rule in derivation_rules[var]:
            non_terminals = [symbol for symbol in single_rule if symbol.isupper()]
            if can_create_program(non_terminals, keys):
                if var not in new_programs.keys():
                    new_programs[var] = []
                new_programs[var] += create_programs(P, single_rule)
    prune_programs = {}
    for var in new_programs.keys(): #Todo: check if only compare programs from same var
        for new_program in new_programs[var]:
            for old_program in P[var]:
                if compare(new_program, old_program, spec):
                    break
            if var not in prune_programs.keys():
                prune_programs[var] = []
            prune_programs[var] += [new_program[:]]

    return prune_programs


def compare(p1, p2, spec):
    p1 = ''.join(p1)
    p2 = ''.join(p2)
    for (x, _) in spec:
        if eval(p1) != eval(p2):
            return False
    return True


def validate(p, spec):
    program = ''.join(p)
    for (x, o) in spec:
        if eval(program) != o:
            return False
    return True


"""creating terminal rules and all derivation rules as a dectionary of the form: Var -> list of rules derived by the var"""
def parse_grammer(grammer):
    derivation_rules = {}
    terminals_rules = {}
    for derivation_rule in grammer:
        left, right = derivation_rule.split('::=')
        left = left.strip()
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
    P = {}
    for key in terminals_rules.keys():
        P[key] = terminals_rules[key][:]
    if 'S' not in P.keys():
        P['S'] = []
    while True:
        new_programs = grow(P, derivation_rules, spec)
        if not new_programs:
            return 'no program'
        for var in new_programs.keys():
            if var not in P.keys():
                P[var] = []
            P[var] += new_programs[var]
        for p in new_programs['S']:
            if validate(p, spec):
                return p


if __name__ == "__main__":
    grammer = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0", "N ::= 1"]
    print(bottom_up(grammer, [(0, 0), (2, 4), (3, 9), (4, 16)]))
