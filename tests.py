import unittest
from synthesizer import  Synthesizer
import time


class SynthesizerTest(unittest.TestCase):
    arithmetic_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )",
                          "S ::= ( S / S )", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]

    @staticmethod
    def found_sol(sol):
        return not sol.startswith('no program')

    def test_aarith_constant_func(self):
        print("running test_arith_constant_func")
        s = Synthesizer(self.arithmetic_grammar, [(134, 1), (20, 1), (3, 1), (0, 1)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_constant_func, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end-start}\n")

    def test_arith_pow_3(self):
        print("running test_arith_pow_3")
        s = Synthesizer(self.arithmetic_grammar, [(0, 0), (5, 125), (3, 27), (10, 1000)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_pow_3, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end - start}\n")

    def test_arith_mul2_minus4(self):
        print("running test_arith_mul2_minus4")
        s = Synthesizer(self.arithmetic_grammar, [(1, -2), (5, 6), (3, 2), (10, 16)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_mul2_minus4, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end - start}\n")

    def test_arith_pow2_div_by_3(self):
        print("running test_arith_pow2_div_by_3")
        s = Synthesizer(self.arithmetic_grammar, [(9, 27), (6, 12), (12, 48), (15, 75)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_pow2_div_by_3, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end - start}\n")

    def test_arith_2_pow_x_unrealizable(self):
        print("running test_arith_2_pow_x_unrealizable")
        s = Synthesizer(self.arithmetic_grammar, [(2, 4), (6, 48), (10, 1024), (1, 2)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_2_pow_x_unrealizable, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end - start}\n")

    def test_arith_x_plus_1_pow_2(self):
        print("running test_arith_x_plus_1_pow_2")
        s = Synthesizer(self.arithmetic_grammar, [(2, 9), (6, 49), (10, 121), (1, 4)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_x_plus_1_pow_2, {'Found, Program =' if self.found_sol(sol) else 'Not Found,'}"
                    f" {sol}, {end - start}\n")




if __name__ == '__main__':
    #unittest.main()
    arithmetic_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )",
                          "S ::= ( S / S )", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    print("running test_arith_x_plus_1_pow_2")
    s = Synthesizer(arithmetic_grammar, [(2, 9), (6, 49), (10, 121), (1, 4)])
    start = time.time()
    sol = s.find_solution()
    end = time.time()
    assert (SynthesizerTest.found_sol(sol))
    with open("synthesizer_tests.csv", 'a') as f:
        f.write(f"test_arith_x_plus_1_pow_2, {'Found, Program =' if SynthesizerTest.found_sol(sol) else 'Not Found,'}"
                f" {sol}, {end - start}\n")

"""
def random_int():
    return randint(0,10)

if __name__ == "__main__":

    grammar = ["S ::= std_filter ( FILTARG , L )", "S ::= std_map ( MAPTARG , L )", "L ::= x",
               "FILTARG ::= lambda y : y <= NUM", "MAPTARG ::= lambda y : y * y", "NUM ::= 1", "NUM ::= ( NUM + NUM )"]
    grammar_arith = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0",
                     "N ::= 10"]
    grammar_lst = ["S ::= x", "S ::= []", "S ::= [ INT ]", "S ::= ( S + S )", "S ::= S [ INT ]",   "INT ::= 0", "INT ::= 1", "INT ::= ( INT + INT )"]

    spec1 = [([0,2,1,4], [0,2,1]), ([1,0], [1,0]), ([4,3,5,4], []), ([2,1,4], [2,1])]
    spec2 = [([0,0,0,0], [0,0,0,0]), ([1,4,2,5],[1,16,4,25]), ([3,2,2,7],[9,4,4,49])]
    spec3 = [(0, 100), (2, 300), (3, 970), (4, 2740)]
    spec4_1 = [([1,2,3],2),([3,5,4,5],5),([1,3,4,5],3)]
    spec4_2 = [("[b,a]","a+b"),("[10,a,b]","a+b")]
    s = time.time()
   # print(Synthesizer(grammar, spec1, lambda_instances=random_int).bottom_up())
    print(Synthesizer(grammar_lst, [], spec_with_symbolic_ex=spec4_2).bottom_up())
    print(time.time()-s)

    grammar_arith = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "S ::= ( S / S )", "N ::= 0",
                     "N ::= 1", "N ::= ( N + N )"]
    spec = [(12,3),(20,5),(44,11),(64,16)]
    s = time.time()
    print(Synthesizer(grammar_arith, spec).bottom_up())
    print(time.time() - s)

"""