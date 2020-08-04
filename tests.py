import unittest
from synthesizer import Synthesizer
import time
from random import randint



class SynthesizerTest(unittest.TestCase):
    arithmetic_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )",
                          "S ::= ( S / S )", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    string_grammar = ["S ::= x", "S ::= ( S + S )", "S ::= ( S * N )", "S ::= S [ N ]", "S ::= std_lower ( S )",
                       "S ::= std_upper ( S )", "S ::= CHAR", "CHAR ::= 'n'", "CHAR ::= 'm'", "CHAR ::= 'o'",
                       "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    lambda_grammar = ["S ::= std_filter ( FILTARG , S )", "S ::= std_map ( MAPTARG , S )", "S ::= x", "S ::= [ ]",
                      "S ::= [ N ]", "S ::= ( S + S )", "FILTARG ::= lambda y : y <= N", "MAPTARG ::= lambda y : y * y",
                      "N ::= 1", "N ::= ( N + N )"]

    lambda_grammar2 = ["S ::= std_filter ( FILTARG , S )", "S ::= std_map ( MAPTARG , S )", "S ::= x",
                       "S ::= ( S + S )", "FILTARG ::= lambda y : ( y * N ) <= N",
                       "FILTARG ::= lambda y : ( y + ( y * N ) ) <= N",  "MAPTARG ::= lambda y : y ** N",
                       "MAPTARG ::= lambda y : y * ( y ** N )", "N ::= 1",  "N ::= 2", "N ::= ( N + N )",
                       "FILTARG ::= lambda y : y % N == 0"]

    @staticmethod
    def found_sol(sol):
        return not sol.startswith('no program')

    #arithmetic synthesize test  start
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
        with open("synthesizer_tests.csv", 'a') as f:
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
        with open("synthesizer_tests.csv", 'a') as f:
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
        with open("synthesizer_tests.csv", 'a') as f:
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
        with open("synthesizer_tests.csv", 'a') as f:
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
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_arith_x_plus_1_pow_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")
    #arithmetic synthesize test  end

    #string synthesize test start
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
    #string synthesize test end


    #lambda synthesis test start

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

    def test_lambda_geq_3_unrealizable(self):
        print("running test_lambda_geq_3_unrealizable")
        s = Synthesizer(self.lambda_grammar, [([10, 3, 2], [10, 3]), ([1, 0, 6], [6]), ([2, 4, 1, 6], [4, 6])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_geq_3_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_geq_3_unrealizable, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_x_pow_4(self):
        print("running test_lambda_x_pow_4")
        s = Synthesizer(self.lambda_grammar, [([1, 2, 3], [1, 16, 81]), ([1, 0, 6], [1, 0, 1296]),
                                              ([2, 4, 5], [16, 256, 625])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_x_pow_4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_x_pow_4, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")


    #lambda synthesize test  end

    # lambda optimization synthesis test start
    
    def test_lambda_less_5_pow5(self):
        print("running test_lambda_less_5_pow5")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2], [243, 32]), ([5, 2], [32]), ([4, 5, 1], [1024, 1])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_less_5_pow5_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_less_5_pow5_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2], [243, 32]), ([5, 2], [32]), ([4, 5, 1], [1024, 1])],
                        lambda_instances=lambda: randint(1, 7))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_less_5_pow5_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_less_5_pow5_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_less_4_concat_pow3(self):
        print("running test_lambda_less_4_concat_pow3")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2], [3, 2, 216, 27, 8]), ([5, 2], [2,125,8]), ([4, 5, 1], [1, 64, 125, 1])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_less_4_concat_pow3_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_less_4_concat_pow3_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2,  [([6, 3, 2], [3, 2, 216, 27, 8]), ([5, 2], [2,125,8]), ([4, 5, 1], [1, 64, 125, 1])],
                        lambda_instances=lambda: randint(1, 7))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_less_4_concat_pow3_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_less_4_concat_pow3_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_1_if_list_distinct_unrealizable(self):
        print("running test_lambda_1_if_list_distinct_unrealizable")
        s = Synthesizer(self.lambda_grammar2,
                        [([6, 3, 2], [1, 1, 1]), ([5, 2, 5], [5, 2, 5]), ([4, 6, 1], [1, 1, 1]), ([2, 4, 4], [2, 4, 4])],
                        time_limit=30)
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("test_lambda_1_if_list_distinct_unrealizable_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_1_if_list_distinct_unrealizable_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2,
                        [([6, 3, 2], [1, 1, 1]), ([5, 2, 5], [5, 2, 5]), ([4, 6, 1], [1, 1, 1]), ([2,4,4], [2,4,4])],
                        time_limit=30, lambda_instances=lambda: randint(1, 10))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("test_lambda_1_if_list_distinct_unrealizable_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(f"test_lambda_1_if_list_distinct_unrealizable_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_even_less_4_pow_4(self):
        print("running test_lambda_even_less_4_pow_4")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [16]), ([5, 2, 4, 12], [16,256]), ([7, 10, 0, 1], [0])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_even_less_4_pow_4_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(
                f"test_lambda_even_less_4_pow_4_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [16]), ([5, 2, 4, 12], [16,256]), ([7, 10, 0, 1], [0])],
                        lambda_instances=lambda: randint(0, 8))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_even_less_4_pow_4_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(
                f"test_lambda_even_less_4_pow_4_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

    def test_lambda_modulo3_concat_even_pow_2(self):
        print("running test_lambda_modulo3_concat_even_pow_2")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [6, 3, 36, 4, 64]), ([5, 2, 9, 12], [9, 12, 4, 144]), ([3, 15, 0, 1],
                        [3, 15, 0, 0])], depth_limit=6)
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_modulo3_concat_even_pow_2_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(
                f"test_lambda_modulo3_concat_even_pow_2_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2,[([6, 3, 2, 8], [6, 3, 36, 4, 64]), ([5, 2, 9, 12], [9, 12, 4, 144]), ([3, 15, 0, 1],
                        [3, 15, 0, 0])], depth_limit=6, lambda_instances=lambda: randint(0, 10))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("test_lambda_modulo3_concat_even_pow_2_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests.csv", 'a') as f:
            f.write(
                f"test_lambda_modulo3_concat_even_pow_2_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")
        #lambda optimization synthesis test start



if __name__ == '__main__':
    unittest.main()



"""
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