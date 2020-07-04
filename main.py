
def terminal_rules(grammer):
    return [('S', '5')]


def grow(P, grammer, spec):
    return []


def prone(P, new_programs):
    return new_programs


def validate(p, spec):
    for (i, o) in spec:
        if eval(p, {"__builtins__": None}, {'i': i}) != o:
            return False
    return True


def bottom_up(grammer, spec):
    P = terminal_rules(grammer)
    while True:
        new_programs = grow(P, grammer, spec)
        new_programs = prone(P, new_programs)
        if not new_programs:
            return 'no program'
        P += new_programs
        for p in P:
            if p[0] == 'S' and validate(p[1], spec):  #assuming p is a tuple of (V, program)
                return p


if __name__ == "__main__":
    print(validate('i+1', [(1, 2)]))
