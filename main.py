import time
from funcs import *


class Program:
    spec = None

    @staticmethod
    def set_spec(spec):
        Program.spec = spec

    def __init__(self, code, depth=0, calculate=False):
        self.valid = True
        if calculate:
            try:
                self.outputs = [eval(code) for (x, _) in Program.spec]
            except:
                self.valid = False
        self.code = code
        self.depth = depth

    def calc(self):
        try:
            self.outputs = []
            for (x, _) in Program.spec:
                self.outputs += [eval(self.code)]
        except:
            self.valid = False

    def is_solving(self):
        return all(o1 == o2 for (o1, (_, o2)) in zip(self.outputs, Program.spec))

    def get_outputs_string(self):
        return str(self.outputs)



class Synthesizer:
    def __init__(self, grammar, spec, depth_limit=5, time_limit=100): #TODO change timelimit
        self.spec = spec
        self.grammar = grammar
        self.vars_depth = {}
        self.P = {}
        self.seen_outputs = {}
        self.depth_limit = depth_limit
        self.time_limit = time_limit
        self.time = None
        Program.set_spec(spec)

    def create_programs(self, rule):
        new_programs = [Program("")]
        for symbol in rule:
            iteration_programs = []
            cur_len = len(new_programs)

            if symbol.isupper():
                for i in range(cur_len):
                    iteration_programs += [Program(new_programs[i].code + " " + old_program.code,
                                                   max(old_program.depth, new_programs[i].depth)) for old_program in self.P[symbol]]
                new_programs = iteration_programs
            else:
                for i in range(cur_len):
                    new_programs[i].code += " " + symbol
        return new_programs

    def check_depth(self, non_terminals, depth):
        return any(self.vars_depth[non_terminal] == depth-1 for non_terminal in non_terminals)

    """iterating other all the derivation rules and if a rule can be applied a new program is created"""
    def grow(self, derivation_rules, depth):
        keys = self.P.keys()
        new_programs = {}
        for var in derivation_rules:
            for single_rule in derivation_rules[var]:
                if all(x in keys for x in single_rule[1]) and self.check_depth(single_rule[1], depth):
                    if var not in new_programs.keys():
                        new_programs[var] = []
                    new_programs[var] += self.create_programs(single_rule[0])

        for var in new_programs.keys(): #Todo: check if only compare programs from same var
            for new_program in new_programs[var]:
                if time.time() - self.time > self.time_limit:
                    raise TimeoutError
                if new_program.depth < depth-1:
                    continue
                new_program.calc()

                if not new_program.valid:
                    continue
                if var not in self.seen_outputs.keys():
                    self.seen_outputs[var] = set()
                curr_outputs = new_program.get_outputs_string()
                if curr_outputs in self.seen_outputs[var]:
                    continue
                if ' std_reverse(  std_reverse( x ) )' == new_program.code:
                    print(new_program.code)
                if var not in self.P.keys():
                    self.P[var] = []
                new_program.depth = depth
                self.P[var] += [new_program]
                self.seen_outputs[var].add(curr_outputs)
                self.vars_depth[var] = depth
                if var == 'S' and new_program.is_solving():
                    return new_program.code
        return None

    """creating terminal rules and all derivation rules as a dictionary of the form: Var -> list of rules derived by the var
        ,not adding rules of terminals"""
    def parse_grammar(self):
        derivation_rules = {}
        program = None
        for derivation_rule in self.grammar:
            left, right = derivation_rule.split('::=')
            left = left.strip()
            right = right.split()
            self.vars_depth[left] = 0
            if len(right) == 1 and not (right[0]).isupper():
                new_prog = Program(''.join(right), calculate=True)
                if not new_prog.valid:
                    continue
                if left == 'S' and new_prog.is_solving():
                    program = new_prog
                    break
                if left not in self.P.keys():
                    self.P[left] = []
                self.P[left] += [new_prog]
                if left not in self.seen_outputs.keys():
                    self.seen_outputs[left] = set()
                self.seen_outputs[left].add(new_prog.get_outputs_string())
                continue
            if left not in derivation_rules.keys():
                derivation_rules[left] = []
            derivation_rules[left] += [(right, [symbol for symbol in right if symbol.isupper()])]
        return derivation_rules, program

    def bottom_up(self):
        derivation_rules, program = self.parse_grammar()
        depth = 1
        previous_len = sum(len(self.P[var]) for var in self.P.keys())
        new_len = previous_len
        while not program and depth < self.depth_limit:
            self.time = time.time()
            previous_len = new_len
            try:
                program = self.grow(derivation_rules, depth)
            except TimeoutError:
                return 'no program under time limitations'
            new_len = sum(len(self.P[var]) for var in self.P.keys())
            if previous_len == new_len:
                return 'no program'
            depth += 1
        if not program:
            return 'no program under depth limitations'
        return program


if __name__ == "__main__":
    grammer = ["S ::= x", "S ::= []", "S ::= [ INT ]", "S ::= S [ INT ]", "S ::= S [: INT ]", "INT ::= std_find ( S , INT )",
            "S ::= std_reverse( S )",  "S ::= std_find ( S , INT )", "INT ::= 0"]

    spac = [([3, 2, 1], [3, 2]), ([2], []), ([3, 0, 2], [3, 0]), ([2, 3, 2, 3], [2, 3, 2])]
    s = time.time()
    print(Synthesizer(grammer, spac).bottom_up())
    print(time.time()-s)
