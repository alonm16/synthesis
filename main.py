"""if every nonterminal in the programs is already in a program we created then a new program can be created"""
def can_create_program(non_terminals,keys):
    for non_terminal in non_terminals:
        if not non_terminal in keys:
            return False
    return True


def create_programs(P, rule):
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
                new_programs[i] += symbol #TODO check whether its a fun ction
            if cur_len == 0:
                new_programs = [[symbol]]
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
    return new_programs


def validate(p, spec):
    for (i, o) in spec:
        if eval(p, {"__builtins__": None}, {'i': i}) != o:
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
        for p in P['S']:
            if validate(p, spec):
                return p


if __name__ == "__main__":
    grammer = ["C ::= 'a'", "C ::= 'b'", "C ::= 'c'", "S ::= C", "S ::= ( S + S )"
            , "S ::= ( S * N )", "S ::= S [ N ]" , "S ::= x", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    bottom_up(grammer, [])
