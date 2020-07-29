class Program:
    def __init__(self, code, depth=0, calculate=False):
        if calculate:
            self.outputs = [eval(code) for (x, _) in spec]
        self.code = code
        self.depth = depth

    def calc(self):
        self.outputs = [eval(self.code) for (x, _) in spec]

    def compare(self, old_programs):
        for old_program in old_programs:
            if all(o1 == o2 for (o1, o2) in zip(self.outputs, old_program.outputs)):
                return True
        return False

    def validate(self):
        return all(o1 == o2 for (o1, (i, o2)) in zip(self.outputs, spec))


def create_programs(P, rule):
    new_programs = [Program("")]
    for symbol in rule:
        iteration_programs = []
        cur_len = len(new_programs)
        if symbol.isupper():
            for i in range(cur_len):
                iteration_programs += [Program(new_programs[i].code + " " + old_program.code, max(old_program.depth, new_programs[i].depth)) for old_program in P[symbol]]
            new_programs = iteration_programs
        else:
            for i in range(cur_len):
                new_programs[i].code += " " + symbol
    return new_programs


def check_depth(vars_depth, non_terminals, depth):
    return any(vars_depth[non_terminal] == depth-1 for non_terminal in non_terminals)


"""iterating other all the derivation rules and if a rule can be applied a new program is created"""
def grow(P, derivation_rules, depth, vars_depth):
    keys = P.keys()
    new_programs = {}
    for var in derivation_rules:
        for single_rule in derivation_rules[var]:
            if all(x in keys for x in single_rule[1]) and check_depth(vars_depth, single_rule[1], depth):
                if var not in new_programs.keys():
                    new_programs[var] = []
                new_programs[var] += create_programs(P, single_rule[0])

    for var in new_programs.keys(): #Todo: check if only compare programs from same var
        for new_program in new_programs[var]:
            if new_program.depth < depth-1:
                continue
            new_program.calc()
            if new_program.compare(P[var]):
                continue
            if var not in P.keys():
                P[var] = []
            new_program.depth = depth
            P[var] += [new_program]
            vars_depth[var] = depth
            if var == 'S' and new_program.validate():
                return new_program.code
    return None


"""creating terminal rules and all derivation rules as a dectionary of the form: Var -> list of rules derived by the var
    ,not adding rules of terminals"""
def parse_grammer():
    derivation_rules = {}
    terminals_programs = {}
    vars_depth = {}
    program = None
    for derivation_rule in grammar:
        left, right = derivation_rule.split('::=')
        left = left.strip()
        right = right.split()
        vars_depth[left] = 0
        if len(right) == 1 and not (right[0]).isupper():
            new_prog = Program(''.join(right), calculate=True)
            if new_prog.validate():
                program = new_prog
                break
            if left not in terminals_programs.keys():
                terminals_programs[left] = []
            terminals_programs[left] += [new_prog]
            continue
        if left not in derivation_rules.keys():
            derivation_rules[left] = []
        derivation_rules[left] += [(right, [symbol for symbol in right if symbol.isupper()])]
    return derivation_rules, terminals_programs, vars_depth, program


def bottom_up():
    derivation_rules, P, vars_depth ,program = parse_grammer()
    depth = 1
    while not program:
        previous_len = sum(len(P[var]) for var in P.keys())
        program = grow(P, derivation_rules, depth, vars_depth)
        new_len = sum(len(P[var]) for var in P.keys())
        if previous_len == new_len:
            return 'no program'
        depth += 1
    return program


if __name__ == "__main__":
    grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0", "N ::= 10"]
    spec = [(0, 10), (2, 26), (3, 91), (4, 266)]
    print(bottom_up())
