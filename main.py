import time
from funcs import *


class Program:
    spec = None

    @staticmethod
    def set_spec(spec):
        Program.spec = spec

    def __init__(self, code, depth=0, calculate=False):
        """
        create new program
        :param code: code of the program
        :param depth: number of current iteration
        :param calculate: if True calculate the outputs of the program (else the code of the program is not finished)
        """
        self.valid = True
        if calculate:
            try:
                self.outputs = [eval(code) for (x, _) in Program.spec]
            except:
                self.valid = False
        self.code = code
        self.depth = depth

    def calc(self):
        """
        calculate the outputs of the program from the input in the specifications
        :return: list of outputs as a string
        """
        try:
            self.outputs = []
            for (x, _) in Program.spec:
                self.outputs += [eval(self.code)]
            return str(self.outputs)
        except:
            self.valid = False

    def is_solving(self):
        """
        check whether the program satisfies the specifications
        :return: True if it is else False
        """
        return all(o1 == o2 for (o1, (_, o2)) in zip(self.outputs, Program.spec))


class Synthesizer:
    def __init__(self, grammar, spec, depth_limit=5, time_limit=100):
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
        """
        creating new programs from a derivation rule
        :param rule: derivation rule
        :return: new programs before pruning
        """
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
        """
        optimization for checking if a new program can be created
        :param non_terminals: non-terminals of the current rule
        :param depth: number of current iteration
        :return: True - if a program was created in the last
                 iterations from one of the non-terminals of the rule
                 False - else
        """
        return any(self.vars_depth[non_terminal] == depth-1 for non_terminal in non_terminals)

    def grow(self, derivation_rules, depth):
        """
        iterating other all the derivation rules and if a rule can be applied a function calling. Afterwards perform
        pruning out of the new programs
        :param derivation_rules: derivation rules of the grammar
        :param depth: number of current iteration
        :return: program that satisfies the specifications if exists else None
        """
        new_programs = {}
        for var in derivation_rules:
            for single_rule in derivation_rules[var]:
                if all(len(self.P[x]) > 0 for x in single_rule[1]) and self.check_depth(single_rule[1], depth):
                    if var not in new_programs.keys():
                        new_programs[var] = []
                    new_programs[var] += self.create_programs(single_rule[0])

        for var in new_programs.keys(): #Todo: check if only compare programs from same var
            for new_program in new_programs[var]:
                if time.time() - self.time > self.time_limit:
                    raise TimeoutError
                if new_program.depth < depth-1:
                    continue
                curr_outputs = new_program.calc()
                if not new_program.valid or curr_outputs in self.seen_outputs[var]:
                    continue
                new_program.depth = depth
                self.P[var] += [new_program]
                self.seen_outputs[var].add(curr_outputs)
                self.vars_depth[var] = depth
                if var == 'S' and new_program.is_solving():
                    return new_program.code

    def parse_grammar(self):
        """
        creating derivation rules of the grammar as a dictionary in the form of: Var -> (list of rules derived by the var)
        ,without adding rules of terminals. Creating programs out of terminal rules
        :return:
        """
        derivation_rules = {}
        for derivation_rule in self.grammar:
            left, right = derivation_rule.split('::=')
            left = left.strip()
            right = right.split()
            self.vars_depth[left] = 0
            if left not in derivation_rules.keys():
                derivation_rules[left], self.P[left], self.seen_outputs[left] = [], [], set()
            if all(not symbol.isupper() for symbol in right):
                new_prog = Program(' '.join(right), calculate=True)
                if not new_prog.valid:
                    continue
                if left == 'S' and new_prog.is_solving():
                    return derivation_rules, new_prog
                self.P[left] += [new_prog]
                self.seen_outputs[left].add(str(new_prog.outputs))
                continue
            derivation_rules[left] += [(right, [symbol for symbol in right if symbol.isupper()])]
        return derivation_rules, None

    def bottom_up(self):
        """
        main function, running a loop which expands the number of programs each iterations until a program is found
        or certain conditions are met as specified below
        :return: program that satisfies the specifications - if exists
                'no program under time limitations' - if time passed the limit
                'no program' - if the number of programs didn't change between iterations
                'no program under depth limitations' - if number of iterations passed the limit
        """
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
    grammar = ["S ::= std_filter ( FILTARG , L )", "S ::= std_map ( MAPTARG , L )", "L ::= x",
               "FILTARG ::= lambda y : y <= NUM", "MAPTARG ::= lambda y : y * y", "NUM ::= 1", "NUM ::= ( NUM + NUM )"]
    grammar_arith = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0",
                     "N ::= 10"]
    spec1 = [([0,2,1,4], [0,2,1]), ([1,0], [1,0]), ([4,3,5,4], []), ([2,1,4], [2,1])]
    spec2 = [([0,0,0,0], [0,0,0,0]), ([1,4,2,5],[1,16,4,25]), ([3,2,2,7],[9,4,4,49])]
    spec3 = [(0, 20), (2, 30), (3, 50), (4, 88)]
    s = time.time()
    print(Synthesizer(grammar_arith, spec3).bottom_up())
    print(time.time()-s)

