import reference.Program as Program

class Synthesizer(object):
    def __init__(self, grammar, specs, depth_limt=3, user_sketch=None):
        self.rules = self.parse_grammar(grammar)
        self.terminals = self.parse_terminals(self.rules)
        self.specs = specs
        self.inputs = [x[0] for x in specs]
        self.depth_limit = depth_limt
        if user_sketch is not None:
            self.rules["S"] = [user_sketch]

        print(self.rules)
        print(self.terminals)

        #self.outputs = specs.values()
    
    def parse_grammar(self, grammar):
        rules = {}
        for rule in grammar:
            left = rule.split("::=")[0].strip()
            right = rule.split("::=")[1].strip()
            if left in rules.keys():
                rules[left].append(right)
            
            else:
                rules[left] = [right]

        return rules

    def parse_terminals(self, grammar):
        terminals = {}
        for key, vals in grammar.items():
            for val in vals:
                if (not val.isupper()) or val.isdigit():
                    terminals[val] = key

        return terminals

    def synthesize(self):
        programs = Program.Programs(self.rules, self.terminals, self.inputs)
        stage = 0
        prog = None
        while not prog and stage < self.depth_limit:
            prog = programs.grow(stage, self.specs)
            stage += 1
        
        return prog
