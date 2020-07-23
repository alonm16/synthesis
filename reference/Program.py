import itertools
from helper import *
import time

class Program(object):
    def __init__(self, code, inputs, rule, stage):
        self.code = code
        self.rules = {rule}
        self.outputs = []
        for x in inputs:
            try:
                output = (x, eval(code))
            except Exception as e:
                output = (x, str(e))
            self.outputs.append(output)

        self.stage = stage


    def check_starting(self):
        return "S" in self.rules

    def add_rule(self, rules):
        self.rules = self.rules.union(rules)


class Programs(object):
    def __init__(self, rules, terminals, inputs, timeout = 60):
        self.sub_programs = [Program(t, inputs, r, 0) for (t, r) in terminals.items()] # No two terminals with the same nonterminal
        self.rules = rules
        self.inputs = inputs
        self.timeout = timeout

    def grow(self, stage, specs):
        start = time.time()
        print("grow")
        new_progs = []
        programs = self.sub_programs[:]
        for (key, values) in self.rules.items():
            for value in values:
                tags = [tag for tag in value.split(" ") if tag.isupper()]
                tag_prog = [[prog for prog in programs if tag in prog.rules] for tag in tags]
                tag_prog_prod = [prod for prod in itertools.product(*tag_prog) if any(map(lambda x: x.stage == stage, prod))]
                for prod in tag_prog_prod:
                    new_prog = value[:]
                    for (i, tag) in enumerate(tags):
                        new_prog = new_prog.replace(tag, prod[i].code, 1)

                    new_prog = Program(new_prog, self.inputs, key, stage + 1)
                    if new_prog.check_starting() and new_prog.outputs == specs:
                        return new_prog
                    new_progs.append(new_prog)
                    self.add_sub_program(new_prog)

                    if time.time()-start > self.timeout:
                        return None

        return None

    def add_sub_program(self, sub_prog):
        is_equiv = False

        for prog in self.sub_programs:
            if sub_prog.outputs == prog.outputs:
                is_equiv = True
                if sub_prog.code == prog.code:
                    prog.add_rule(sub_prog.rules)
        
        if not is_equiv:
            self.sub_programs.append(sub_prog)





