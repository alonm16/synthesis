import unittest
from synthesizer import Synthesizer
import time
from random import randint


class SynthesizerTest(unittest.TestCase):
    arithmetic_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )",
                          "S ::= ( S / S )", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]

    string_grammar = ["S ::= x", "S ::= ( S + S )", "S ::= S [ N ]", "S ::= std_lower ( S )",
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

    list_grammar = ["F ::= ( std_find( S , N ) )", "S ::= std_sort ( S )", "S ::=  x", "S ::= S [ :  F ]",
                    "S ::= [ N ]", "N ::= 1", "N ::= ( N + N )", "S ::= std_reverse ( S )", "S ::= std_reverse ( S )",
                    "N ::= 4", "S ::= ( S + S )"]
    list_grammar2 = ["S ::= x", "S ::= [ ]", "S ::= ( S + S )", "N ::= 1", "N ::= ( N + N )", "S ::= S [ : N ]",
                     "S ::= S [ N : ] ", "S ::= std_sort ( S )", "S ::= std_reverse ( S )", "S ::= std_find ( S , N )"]

    condition_abduction_grammar = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )",
                                   "N ::= 0", "N ::= 1", "N ::= ( N + N )"]
    boolean_grammar = ["S ::= x", "S ::= N", "N ::= 0", "N ::= 1", "N ::= ( N + N )", "S ::= ( not ( S ) )",
                       "S ::= ( S < S )", "S ::= ( S > S )", "S ::= ( S == S )", "S ::= S % N == 0"]

    @staticmethod
    def found_sol(sol):
        return not sol.startswith('no program')

    #arithmetic synthesize test  start
    def test_arith_constant_func(self):
        print("running test_arith_constant_func")
        s = Synthesizer(self.arithmetic_grammar, [(134, 1), (20, 1), (3, 1), (0, 1)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_arith_constant_func", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'w') as f:
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
            with open("tests_results/test_arith_pow_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_arith_mul2_minus4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_arith_pow2_div_by_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_arith_pow2_div_by_3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_arith_two_pow_x_unrealizable(self):
        print("running test_arith_2_pow_x_unrealizable")
        s = Synthesizer(self.arithmetic_grammar, [(2, 4), (6, 48), (10, 1024), (1, 2)])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_arith_2_pow_x_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_arith_x_plus_1_pow_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_arith_x_plus_1_pow_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")
    #arithmetic synthesize test  end

    #string synthesize test start
    def test_string_concat_o(self):
        print("running test_string_concat_o")
        s = Synthesizer(self.string_grammar, [("hell", "hello"), ("br", "bro"), ("n", "no"), ("finit", "finito")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_string_concat_o", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_string_concat_o, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_pow_3(self):
        print("running test_string_concat")
        s = Synthesizer(self.string_grammar, [("hi", "hihihi"), ("love", "lovelovelove"), ("n", "nnn"), ("bla", "blablabla")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_string_pow_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_string_pow_3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_second_letter_upper(self):
        print("running test_string_second_letter_upper")
        s = Synthesizer(self.string_grammar,[("hi", "I"), ("love", "O"), ("drunk", "R"), ("bla", "L")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_string_second_letter_upper", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_string_lower_upper_concat", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_string_lower_upper_concat, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_string_last_letter_unrealizable(self):
        print("running test_string_last_letter_unrealizable")
        s = Synthesizer(self.string_grammar, [("I", "I"), ("lOvE", "E"), ("SynThesis", "s")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_string_last_letter_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_string_first_letter_plus_n_plus_lower_x", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_string_first_letter_plus_n_plus_lower_x, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")
    #string synthesis test end

    #list synthesis test start

    def test_list_constant_1(self):
        print("running test list constant 1")
        s = Synthesizer(self.list_grammar, [([1, 2, 3, 4, 5, 6], [1]), ([4, 5, 6], [1]), ([3, 4], [1]),
                                            ([], [1])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()

        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_list_constant_1.csv", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_list_constant_1, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_list_id(self):
        print("running test list id")
        s = Synthesizer(self.list_grammar, [([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]), ([4, 5, 6], [4, 5, 6]),
                                            ([3, 4], [3, 4]), ([], [])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()

        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_list_id.csv", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_list_id, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_list_reverse_sort(self):
        print("running test reverse sort")
        s = Synthesizer(self.list_grammar, [([1, 2, 4, 3, 5, 6], [6, 5, 4, 3, 2, 1]), ([5, 4, 6], [6, 5, 4]),
                                            ([3, 4], [4, 3]), ([], [])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()

        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_list_reverse_sort.csv", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_list_reverse_sort, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_list_sort_until_below_5(self):
        print("running test list sort until below 5")
        s = Synthesizer(self.list_grammar, [([1, 2, 4, 3, 5, 6], [1, 2, 3, 4]), ([5, 4, 6], []),
                                            ([3, 4, 1, 2, 6, 5, 7], [1, 2, 3, 4, 6]), ([2, 1, 5], [1, 2])],
                        depth_limit=7)
        start = time.time()
        sol = s.find_solution()
        end = time.time()

        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_list_sort_until_below_5.csv", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_list_sort_until_below_5, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_list_unrealizable(self):
        print("running test list unique sort unrealizable")
        s = Synthesizer(self.list_grammar, [([1, 2, 1, 2, 3, 4, 2], [1, 2, 3, 4]), ([6, 5, 4, 7, 6], [4, 5, 6, 7])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()

        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_list_unrealizable_unique_sort.csv", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_list_unrealizable_unique_sort, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    #list synthesis test end

    #lambda synthesis test start

    def test_lambda_filter_leq_3(self):
        print("running test_lambda_filter_leq_3")
        s = Synthesizer(self.lambda_grammar, [([10, 3, 2], [3, 2]), ([1, 0], [1, 0]), ([4, 5, 6], [])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_filter_leq_3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_map_pow_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_map_pow2_filter_leq4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_lambda_map_pow2_filter_leq4, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_geq_3_unrealizable(self):
        print("running test_lambda_geq_3_unrealizable")
        s = Synthesizer(self.lambda_grammar, [([10, 3, 2], [10, 3]), ([1, 0, 6], [6]), ([2, 4, 1, 6], [4, 6])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_geq_3_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_x_pow_4", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_less_5_pow5_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_lambda_less_5_pow5_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2], [243, 32]), ([5, 2], [32]), ([4, 5, 1], [1024, 1])],
                        lambda_instances=lambda: randint(1, 7))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_less_5_pow5_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_less_4_concat_pow3_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_lambda_less_4_concat_pow3_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2,  [([6, 3, 2], [3, 2, 216, 27, 8]), ([5, 2], [2,125,8]), ([4, 5, 1], [1, 64, 125, 1])],
                        lambda_instances=lambda: randint(1, 7))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_less_4_concat_pow3_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_1_if_list_distinct_unrealizable_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_1_if_list_distinct_unrealizable_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_lambda_1_if_list_distinct_unrealizable_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_lambda_even_less_4_pow_4(self):
        print("running test_lambda_even_less_4_pow_4")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [16]), ([5, 2, 4, 12], [16, 256]), ([7, 10, 0, 1], [0])])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_even_less_4_pow_4_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(
                f"test_lambda_even_less_4_pow_4_not_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [16]), ([5, 2, 4, 12], [16, 256]), ([7, 10, 0, 1], [0])],
                        lambda_instances=lambda: randint(0, 8))
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_even_less_4_pow_4_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(
                f"test_lambda_even_less_4_pow_4_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")

    def test_lambda_optimized_modulo3_concat_even_pow_2(self):
        print("running test_lambda_modulo3_concat_even_pow_2")
        s = Synthesizer(self.lambda_grammar2, [([6, 3, 2, 8], [6, 3, 36, 4, 64]), ([5, 2, 9, 12], [9, 12, 4, 144]), ([3, 15, 0, 1],
                        [3, 15, 0, 0])], depth_limit=6)
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_lambda_modulo3_concat_even_pow_2_not_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
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
            with open("tests_results/test_lambda_modulo3_concat_even_pow_2_optimized", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(
                f"test_lambda_modulo3_concat_even_pow_2_optimized, {'Found' if self.found_sol(sol) else 'Not Found'}"
                f", {end - start}\n")
        #lambda optimization synthesis test end

    #symbolic example test start
    def test_sym_ex_lst_reverse(self):
        print("running test_sym_ex_lst_reverse")
        s = Synthesizer(self.list_grammar2, [], spec_with_symbolic_ex=[("[a, b, 1]", "[1, b, a]")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_lst_reverse", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_lst_reverse, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_lst_from_second_to_fourth(self):
        print("running test_sym_lst_from_second_to_fourth")
        s = Synthesizer(self.list_grammar2, [], spec_with_symbolic_ex=[("[a, 3, 1, b, 4]", "[3, 1, b]")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_lst_from_second_to_fourth", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_lst_from_second_to_fourth, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_ex_arith_a_plus_1_pow2(self):
        print("running test_sym_ex_arith_a_plus_1_pow2")
        s = Synthesizer(self.arithmetic_grammar, [], spec_with_symbolic_ex=[("a", "(a+1) * (a+1)")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_arith_a_plus_1_pow2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_arith_a_plus_1_pow2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_ex_arith_div_by_2(self):
        print("running test_sym_ex_arith_div_by_2")
        s = Synthesizer(self.arithmetic_grammar, [], spec_with_symbolic_ex=[("2*a", "a")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_arith_div_by_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_arith_div_by_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_ex_map_pow_2(self):
        print("running test_sym_ex_map_pow_2")
        s = Synthesizer(self.lambda_grammar, [], spec_with_symbolic_ex=[("[a, 1]", "[a*a, 1]"),
                                                                        ("[a, b, 0]", "[a*a, b*b, 0]")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_map_pow_2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_map_pow_2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_ex_list_last_element(self):
        print("running test_sym_ex_list_last_element")
        s = Synthesizer(self.list_grammar2, [], spec_with_symbolic_ex=[("[a, 3, 1, b, 4]", "[4]")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_list_last_element", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_list_last_element, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    def test_sym_ex_list_reverse_from_third(self):
        print("running test_sym_ex_list_reverse_from_third")
        s = Synthesizer(self.list_grammar2, [], spec_with_symbolic_ex=[("[a, 3, 1, b, 4]", "[4, b, 1]")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_list_reverse_from_third", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_list_reverse_from_third, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    #unrealizable because of depth limitation
    def test_sym_ex_div_by_5_unrealizable(self):
        print("running test_sym_ex_div_by_5_unrealizable")
        s = Synthesizer(self.arithmetic_grammar, [], spec_with_symbolic_ex=[("5*a", "a")])
        start = time.time()
        sol = s.find_solution()
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_sym_ex_div_by_5_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_sym_ex_div_by_5_unrealizable, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    """1 if x<=2 else 2x"""
    def test_condition_abduction_test1(self):
        print("running test_condition_abduction_test1")
        s = Synthesizer(self.condition_abduction_grammar,  [(0, 1), (2, 1), (4, 8), (5, 10)])
        start = time.time()
        sol = s.find_solution_with_condition_abduction(self.boolean_grammar)
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_condition_abduction_test1", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_condition_abduction_test1, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    """2x if even else x"""
    def test_condition_abduction_test2(self):
        print("running test_condition_abduction_test2")
        s = Synthesizer(self.condition_abduction_grammar, [(8, 16), (4, 8), (2, 4), (3, 3), (7, 7)])
        start = time.time()
        sol = s.find_solution_with_condition_abduction(self.boolean_grammar)
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_condition_abduction_test2", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_condition_abduction_test2, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    """x + 2 if x!=2 else 1"""
    def test_condition_abduction_test3(self):
        print("running test_condition_abduction_test3")
        s = Synthesizer(self.condition_abduction_grammar, [(2, 1), (6, 8), (3, 5), (1, 3)])
        start = time.time()
        sol = s.find_solution_with_condition_abduction(self.boolean_grammar)
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_condition_abduction_test3", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_condition_abduction_test3, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    """x*3 if primary else 2"""
    def test_condition_abduction_test4_unrealizable(self):
        print("running test_condition_abduction_test4_unrealizable")
        s = Synthesizer(self.condition_abduction_grammar, [(2, 6), (6, 2), (3, 9), (5, 15), (12, 36)])
        start = time.time()
        sol = s.find_solution_with_condition_abduction(self.boolean_grammar)
        end = time.time()
        assert (not SynthesizerTest.found_sol(sol))
        if not SynthesizerTest.found_sol(sol):
            with open("tests_results/test_condition_abduction_test4_unrealizable", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_condition_abduction_test4_unrealizable, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")

    """2x+2 if x % 3 == 0 else x^2"""
    def test_condition_abduction_test5(self):
        print("running test_condition_abduction_test5")
        s = Synthesizer(self.condition_abduction_grammar, [(4, 16), (6, 14), (3, 8), (5, 25)])
        start = time.time()
        sol = s.find_solution_with_condition_abduction(self.boolean_grammar)
        end = time.time()
        assert (SynthesizerTest.found_sol(sol))
        if SynthesizerTest.found_sol(sol):
            with open("tests_results/test_condition_abduction_test5", 'w') as f:
                f.write(sol)
        with open("synthesizer_tests_report.csv", 'a') as f:
            f.write(f"test_condition_abduction_test5, {'Found' if self.found_sol(sol) else 'Not Found'}"
                    f", {end - start}\n")


if __name__ == '__main__':
    unittest.main()
