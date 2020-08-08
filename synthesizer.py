import time
from funcs import *
from random import randint

class Program:
    spec = None
    lambda_instances = None

    def __init__(self, code, depth=0):
        """
        create new program
        :param code: code of the program
        :param depth: number of current iteration
        """
        self.code = code
        self.depth = depth

    def is_lambda(self):
        return Program.lambda_instances and self.code.strip().startswith('lambda')

    def calculate_outputs(self):
        """
        calculate the outputs of the program from the input in the specifications
        :return: True if the calculation didn't yield errors
        """
        try:
            if self.is_lambda():
                self.lambda_outputs = [eval('(' + self.code + ')' + '(z)') for z in Program.lambda_instances]
            else:
                self.outputs = [eval(self.code) for (x, _) in Program.spec]
        except:
            return False
        return True

    def is_solving(self):
        """
        check whether the program satisfies the specifications
        :return: True if it is else False
        """
        return all(o1 == o2 for (o1, (_, o2)) in zip(self.outputs, Program.spec))

    def get_correct_output_num(self):
        return sum([1 for (o1, (_, o2)) in zip(self.outputs, Program.spec) if o1 == o2])


class Synthesizer:
    def __init__(self, grammar, spec, depth_limit=5, time_limit=50, lambda_instances=None, spec_with_symbolic_ex = None):
        self.spec = spec
        if spec_with_symbolic_ex:
            self.add_to_spec(spec_with_symbolic_ex)
        self.grammar = grammar
        self.vars_depth = {}
        self.P = {}
        self.seen_outputs = {}
        self.seen_lambda_outputs = {}
        self.depth_limit = depth_limit
        self.time_limit = time_limit
        self.time = None
        if lambda_instances:
            Program.lambda_instances = [lambda_instances() for _ in range(30)]
        else:
            Program.lambda_instances = None
        Program.spec = spec


    def add_to_outputs(self, var, program):
        if program.is_lambda():
            self.seen_lambda_outputs[var].add(str(program.lambda_outputs))
        else:
            self.seen_outputs[var].add(str(program.outputs))

    def is_equivalent(self, var, program):
        if program.is_lambda():
            return str(program.lambda_outputs) in self.seen_lambda_outputs[var]
        else:
            return str(program.outputs) in self.seen_outputs[var]

    def add_to_spec(self, spec_with_symbolic_example):
        """
        creates specification out of the specification with the symbolic examples and
         adds them to the program specifications
        :param spec_with_symbolic_example: specification contains symbolic examples
        """
        a_values = [randint(0,100) for _ in range(20)]
        b_values = [randint(0,100) for _ in range(10)]
        for (input,output) in spec_with_symbolic_example:
            if 'a' in input and 'b' in input:
                for a_value in a_values[:10]:
                    for b_value in b_values:
                        self.spec += [(eval(input.replace('a',str(a_value)).replace('b',str(b_value))),
                                       eval(output.replace('a', str(a_value)).replace('b',str(b_value))))]
            else:
                for a_value in a_values:
                    self.spec += [(eval(input.replace('a', str(a_value))), eval(output.replace('a', str(a_value))))]

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
                    if time.time() - self.time > self.time_limit:
                        raise TimeoutError
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
                if new_program.depth < depth-1 or not new_program.calculate_outputs() or self.is_equivalent(var, new_program):
                    continue
                new_program.depth = depth
                self.P[var] += [new_program]
                self.add_to_outputs(var, new_program)
                self.vars_depth[var] = depth
                if var == 'S' and new_program.is_solving():
                    return new_program

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
                derivation_rules[left], self.P[left], self.seen_outputs[left], self.seen_lambda_outputs[left] = [], [], set(), set()
            if all(not symbol.isupper() for symbol in right):
                new_prog = Program(' '.join(right))
                if not new_prog.calculate_outputs():
                    continue
                if left == 'S' and new_prog.is_solving():
                    return derivation_rules, new_prog
                self.P[left] += [new_prog]
                self.add_to_outputs(left, new_prog)
                continue
            derivation_rules[left] += [(right, [symbol for symbol in right if symbol.isupper()])]
        return derivation_rules, None

    def find_solution(self):
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
        return program.code

    def find_solution_with_condition_abduction(self, condition_grammar):
        """
        selects the program with most correct outputs and creates another program for the rest and connects between them
        with an if statement
        :param condition_grammar: grammar to synthesize the condition
        :return: program with synthesized condition - if exist
                 else - "no program"
        """
        sol = self.find_solution()
        if not sol.startswith("no program"):
            return sol
        max_prog = None
        max_correct = 0
        for prog in self.P['S']:
            curr_correct = prog.get_correct_output_num()
            if curr_correct > max_correct:
                max_correct = curr_correct
                max_prog = prog
        wrong_input_outputs = [(i1, o2) for (o1, (i1, o2)) in zip(max_prog.outputs, self.spec) if o1 != o2]
        s1 = Synthesizer(self.grammar, wrong_input_outputs)
        sol1 = s1.find_solution()
        if sol1.startswith("no program"):
            return "no program"
        correct_inputs = [(i1, True) for (o1, (i1, o2)) in zip(max_prog.outputs, self.spec) if o1 == o2]
        spec_for_condition_abduction = [(i1, False) for (i1, _) in wrong_input_outputs] + correct_inputs
        s2 = Synthesizer(condition_grammar, spec_for_condition_abduction)
        sol_condition = s2.find_solution()
        if sol_condition.startswith("no program"):
            return "no program"
        return max_prog.code + " if " + sol_condition + " else  " + sol1
