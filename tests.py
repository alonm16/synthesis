import unittest
from synthesizer import Synthesizer
import time


class SynthesizerTest(unittest.TestCase):
    arithmetic_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )",
                          "S ::= ( S / S )", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    string_grammar = ["S ::= x", "S ::= ( S + S )", "S ::= ( S * N )", "S ::= S [ N ]", "S ::= std_lower ( S )",
                       "S ::= std_upper ( S )", "S ::= CHAR", "CHAR ::= 'n'", "CHAR ::= 'm'", "CHAR ::= 'o'",
                       "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    lambda_grammar = ["S ::= std_filter ( FILTARG , L )", "S ::= std_map ( MAPTARG , L )", "L ::= x", "L ::= [ ]",
                      "L ::= [ N ]", "L ::= ( L + L )", "FILTARG ::= lambda y : y <= N", "MAPTARG ::= lambda y : y * y",
                      "N ::= 1", "N ::= ( N + N )"]

    @staticmethod
    def found_sol(sol):
        return not sol.startswith('no program')

    """arithmetic synthesize test  start
    
    def test_aarith_constant_func(self):
        print("running test_arith_constant_func")
        s = Synthesizer(self.arithmetic_grammar, [(134, 1), (20, 1), (3, 1), (0, 1)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_constant_func", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_constant_func, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end-start}\n")

    def test_arith_pow_3(self):
        print("running test_arith_pow_3")
        s = Synthesizer(self.arithmetic_grammar, [(0, 0), (5, 125), (3, 27), (10, 1000)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_pow_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_pow_3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_arith_mul2_minus4(self):
        print("running test_arith_mul2_minus4")
        s = Synthesizer(self.arithmetic_grammar, [(1, -2), (5, 6), (3, 2), (10, 16)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_mul2_minus4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_mul2_minus4, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_arith_pow2_div_by_3(self):
        print("running test_arith_pow2_div_by_3")
        s = Synthesizer(self.arithmetic_grammar, [(9, 27), (6, 12), (12, 48), (15, 75)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_pow2_div_by_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_pow2_div_by_3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_arith_2_pow_x_unrealizable(self):
        print("running test_arith_2_pow_x_unrealizable")
        s = Synthesizer(self.arithmetic_grammar, [(2, 4), (6, 48), (10, 1024), (1, 2)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_2_pow_x_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_2_pow_x_unrealizable, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_arith_x_plus_1_pow_2(self):
        print("running test_arith_x_plus_1_pow_2")
        s = Synthesizer(self.arithmetic_grammar, [(2, 9), (6, 49), (10, 121), (1, 4)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_arith_x_plus_1_pow_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'w') as f:
            f.write(f"test_arith_x_plus_1_pow_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")
    arithmetic synthesize test  end"""

    """string synthesize test start
    def test_string_concat(self):
        print("running test_string_concat")
        s = Synthesizer(self.string_grammar, [("hell", "hello"), ("br", "bro"), ("n", "no"), ("finit", "finito")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_concat", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_concat, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_pow_3(self):
        print("running test_string_concat")
        s = Synthesizer(self.string_grammar, [("hi", "hihihi"), ("love", "lovelovelove"), ("n", "nnn"), ("bla", "blablabla")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_pow_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_concat, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_second_letter_upper(self):
        print("running test_string_second_letter_upper")
        s = Synthesizer(self.string_grammar,[("hi", "I"), ("love", "O"), ("drunk", "R"), ("bla", "L")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_second_letter_upper", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_second_letter_upper, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

    def test_string_lower_upper_concat(self):
        print("running test_string_lower_upper_concat")
        s = Synthesizer(self.string_grammar, [("I", "iI"), ("lOvE", "loveLOVE"), ("SynThesis", "synthesisSYNTHESIS")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_lower_upper_concat", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_lower_upper_concat, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_last_letter_unrealizable(self):
        print("running test_string_last_letter_unrealizable")
        s = Synthesizer(self.string_grammar, [("I", "I"), ("lOvE", "E"), ("SynThesis", "s")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_last_letter_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_last_letter_unrealizable, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_first_letter_plus_n_plus_lower_x(self):
        print("running test_string_first_letter_plus_n_plus_lower_x")
        s = Synthesizer(self.string_grammar, [("noaM", "nnnoam"), ("aLOn", "analon"), ("ShlOmiT", "Snshlomit")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_string_first_letter_plus_n_plus_lower_x", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_string_first_letter_plus_n_plus_lower_x, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")
    string synthesize test end"""

    lambda_grammar = ["S ::= std_filter ( FILTARG , S )", "S ::= std_map ( MAPTARG , S )", "S ::= x", "S ::= [ ]",
                      "S ::= [ N ]", "S ::= ( S + S )", "FILTARG ::= lambda y : y <= N", "MAPTARG ::= lambda y : y * y",
                      "N ::= 1", "N ::= ( N + N )"]

    """ lambda synthesis test start"""

    def test_lambda_filter_leq_3(self):
        print("running test_lambda_filter_leq_3")
        s = Synthesizer(self.lambda_grammar, [([10, 3, 2], [3, 2]), ([1, 0], [1, 0]), ([4, 5, 6], [])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_filter_leq_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_filter_leq_3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_map_pow_2(self):
        print("running test_lambda_map_pow_2")
        s = Synthesizer(self.lambda_grammar, [([1, 3, 2], [1, 9, 4]), ([1, 0], [1, 0]), ([4, 5, 6], [16, 25, 36])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_map_pow_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_map_pow_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_map_pow2_filter_leq4(self):
        print("running test_lambda_map_pow2_filter_leq4")
        s = Synthesizer(self.lambda_grammar, [([10, 3, 2], [4]), ([1, 0, 6], [1, 0]), ([2, 4, 1, 6], [4, 1])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_map_pow2_filter_leq4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_map_pow2_filter_leq4, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")


if __name__ == '__main__':
    unittest.main()






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