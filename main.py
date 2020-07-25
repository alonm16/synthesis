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
                    iteration_programs += [(new_programs[i][0] + old_program[0], max(old_program[1], new_programs[i][1]))]
                new_programs += iteration_programs
            new_programs = new_programs[cur_len:]
            if cur_len == 0:
                for old_program in P[symbol]:
                    new_programs += [(old_program[0], old_program[1])]
        else:
            for i in range(cur_len):
                new_programs[i] = (new_programs[i][0] + symbol, new_programs[i][1])
            if cur_len == 0:
                new_programs = [(symbol, 0)]
    return new_programs


"""iterating other all the derivation rules and if a rule can be applied a new program is created"""
def grow(P, derivation_rules, spec, depth):  #Todo pruning and child form last iteration
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
            if new_program[1] < depth-1:
                continue
            flag = False
            for old_program in P[var]:
                if compare(new_program[0], old_program[0], spec): #Todo compare with programs from same depth
                    flag = True
                    break
            if flag:
                continue
            if var not in prune_programs.keys():
                prune_programs[var] = []
            prune_programs[var] += [(new_program[0], depth)]

    return prune_programs


def compare(p1, p2, spec):
    for (x, _) in spec:
        try:
            val1 = eval(p1)
        except Exception as e:
            val1 = str(e)
        try:
            val2 = eval(p2)
        except Exception as e:
            val2 = str(e)
        if val1 != val2:
            return False
    return True


def validate(p, spec):
    for (x, o) in spec:
        try:
            if eval(p) != o:
                return False
        except:
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
            terminals_rules[left] += [(''.join(right), 0)]
        if left not in derivation_rules.keys():
            derivation_rules[left] = []
        derivation_rules[left] += [right]
    return derivation_rules, terminals_rules


def bottom_up(grammer, spec):
    derivation_rules, P = parse_grammer(grammer)
    depth = 0
    if 'S' not in P.keys():
        P['S'] = []
    while True:
        new_programs = grow(P, derivation_rules, spec, depth)
        if not new_programs:
            return 'no program'
        for var in new_programs.keys():
            if var not in P.keys():
                P[var] = []
            P[var] += new_programs[var]
        for p in new_programs['S']:
            if validate(p[0], spec):
                print(P)
                return p[0]
        depth += 1


if __name__ == "__main__":
    grammer = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0", "N ::= 1"]
    print(bottom_up(grammer, [(0, 1), (2, 5), (3, 7), (4, 9)]))
