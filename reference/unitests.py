import unittest
import time
from Synthesizer import Synthesizer


class TestSynthesizer(unittest.TestCase):
    grammar_arith = ["S ::= x", "S ::= N", "S ::= ( S + S )", "S ::= ( S * S )", "S ::= ( S - S )", "N ::= 0", "N ::= 1"]

    grammar_str = ["C ::= 'a'", "C ::= 'b'", "C ::= 'c'", "S ::= C", "S ::= ( S + S )" 
            , "S ::= ( S * N )", "S ::= S [ N ]" , "S ::= x", "N ::= 0", "N ::= 1", "N ::= ( N + N )"]

    grammar_lst = ["S ::= x", "S ::= []", "S ::= [ INT ]", "S ::= ( S + S )", "S ::= S [ INT ]", "S ::= S [: INT ]", "INT ::= synthia_find ( S , INT )", 
            "S ::= synthia_reverse( S )", "S ::= synthia_sort( S )",  "S ::= synthia_find ( S , INT )", "INT ::= 0", "INT ::= 1" , "INT ::= ( INT + INT )"]

    grammar_sketch = ["NUM ::= 0", "NUM ::= 1", "NUM ::= NUM + NUM","EXP ::= EXP [ NUM ]", "NUM ::= len( EXP )", "EXP ::= x", "BOOL ::= NUM > NUM"]

    grammar_sketch2 = ["EMOJ ::= ':)'", "EMOJ ::= ':('", "NUM ::= 55", "NUM ::= 80", "NUM ::= 99", "EXP ::= x", "EXP ::= NUM", "BOOL ::= NUM > NUM", "NUM ::= grade"]

    """
        Arithmacy tests
    """
    def test_arith_syn_0(self):
        print("starting test_arith_syn_0")
        specs = [(0, 0), (2, 0), (3, 0), (6, 0)]
        synth = Synthesizer(self.grammar_arith, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_arith_syn_0", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_arith_syn_0, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")
        

    def test_arith_power_2(self): 
        print("starting test_arith_power_2")
        specs = [(0, 0), (2, 4), (3, 9), (4, 16)]
        synth = Synthesizer(self.grammar_arith, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_arith_power_2", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_arith_power_2, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_arith_div_2(self): # unrealizable
        print("starting test_arith_div_2")
        specs = [(0, 0), (2, 1), (4, 2), (3, 1), (8, 4)]
        synth = Synthesizer(self.grammar_arith, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_arith_div_2", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_arith_div_2, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_arith_2x_plus_1(self): 
        print("starting test_arith_2x_plus_1")
        specs = [(0, 1), (2, 5), (3, 7), (4, 9)]
        synth = Synthesizer(self.grammar_arith, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_arith_2x_plus_1", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_arith_2x_plus_1, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_arith_minus_3(self): 
        print("starting test_arith_minus_3")
        specs = [(0, -3), (2, -1), (3, 0), (4, 1)]
        synth = Synthesizer(self.grammar_arith, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_arith_minus_3", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_arith_minus_3, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    """
        String tests
    """
    def test_str_syn_abc(self):
        print("starting test_str_syn_abc")
        specs = [("0", "abc"), ("ab", "abc"), ("bac", "abc"), ("aaaaa", "abc")]
        synth = Synthesizer(self.grammar_str, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_str_syn_abc", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_str_syn_abc, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_str_repeat(self): 
        print("starting test_str_repeat")
        specs = [("a", "aa"), ("abc", "abcabc"), ("12", "1212")]
        synth = Synthesizer(self.grammar_str, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_str_repeat", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_str_repeat, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_str_concat_a(self): 
        print("starting test_str_concat_a")
        specs = [("0", "0a"), ("a", "aa"), ("ab", "aba")]
        synth = Synthesizer(self.grammar_str, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_str_concat_a", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_str_concat_a, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_str_first_concat_c(self): 
        print("starting test_str_first_concat_c")
        specs = [("acb", "ac"), ("csc", "cc"), ("aaaaa", "ac"), ("qwert", "qc")]
        synth = Synthesizer(self.grammar_str, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_str_first_concat_c", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_str_first_concat_c, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_str_last_letter(self): # unrealizable
        print("starting test_str_last_letter")
        specs = [("aaa", "a"), ("ac", "c"), ("qwerty", "y"), ("v", "v")]
        synth = Synthesizer(self.grammar_str, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_str_last_letter", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_str_last_letter, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    """
        List1 tests
    """
    def test_lst_smallest(self):
        print("starting test_lst_smallest")
        specs = [([3, 2, 1], 1), ([1], 1), ([2, 3], 2), ([4, 7, 3, 5], 3)]
        synth = Synthesizer(self.grammar_lst, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_lst_smallest", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_lst_smallest, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_lst_largest(self): 
        print("starting test_lst_largest")
        specs = [([3, 2, 1], 3), ([1], 1), ([2, 3], 3), ([4, 7, 3, 5], 7)]
        synth = Synthesizer(self.grammar_lst, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_lst_largest", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_lst_largest, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_lst_repeat(self):
        print("starting test_lst_repeat")
        specs = [([3, 2, 1], [3, 2, 1, 3, 2, 1]), ([1], [1, 1]), ([2, 3], [2, 3, 2, 3])]
        synth = Synthesizer(self.grammar_lst, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_lst_repeat", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_lst_repeat, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_lst_only_upto_0(self): 
        print("starting test_lst_find_2")
        specs = [([1, 4, 0 ,6], [1, 4]), ([2, 0 ,3, 4], [2])]
        synth = Synthesizer(self.grammar_lst, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_lst_find_2", "w") as f:
                f.write(prog.code)
                print(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_lst_only_upto_0, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    
    def test_lst_remove_last(self): # unrealizable
        print("starting test_lst_remove_last")
        specs = [([3, 2, 1], [3, 2]), ([2], []), ([3, 0, 2], [3, 0]), ([2, 3, 2, 3], [2, 3, 2])]
        synth = Synthesizer(self.grammar_lst, specs)
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_lst_remove_last", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_lst_remove_last, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    '''
        Sketch test
    '''

    def test_sketch_less_2(self):
        print("starting test_sketch_less_2")
        specs = [(0, True), (1, True), (2, False), (3, False)]
        synth = Synthesizer(self.grammar_sketch, specs, user_sketch="True if x < NUM else False")
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_sketch_less_2", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_sketch_less_2, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_sketch_check_bound(self):
        print("starting test_stest_sketch_check_boundketch_less_2")
        specs = [([], "error"), ([0], 0), ([1,2], 1), ([4, 3, 2, 1], 4)]
        synth = Synthesizer(self.grammar_sketch, specs, user_sketch="EXP if BOOL else 'error'")
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_sketchtest_sketch_check_bound_less_2", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_sketch_check_bound, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_sketch_grade_analysis(self):
        print("starting test_sketch_grade_analysis")
        specs = [([20, 30, 40, 80], [":("] * 4), ([60, 100, 99, 100], [":(", ":)"] * 2), ([80], [":("])]
        synth = Synthesizer(self.grammar_sketch2, specs, user_sketch="[ EMOJ if grade > NUM else EMOJ for grade in EXP ]")
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_sketch_grade_analysis", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_sketch_grade_analysis, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_sketch_grade_analysis(self):
        print("starting test_sketch_grade_analysis")
        specs = [([20, 30, 40, 80], [":("] * 4), ([60, 100, 99, 100], [":(", ":)"] * 2), ([80], [":("])]
        synth = Synthesizer(self.grammar_sketch2, specs, user_sketch="[ EMOJ if grade > NUM else EMOJ for grade in EXP ]")
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_sketch_grade_analysis", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_sketch_grade_analysis, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")

    def test_sketch_exception(self):
        print("starting test_sketch_exception")
        specs = [([0, 1], 'list index out of range'), ([1, 2, 3], 3), ([4, 5, 6, 7], 6), ([8], 'list index out of range')]
        # specs = [([1, 2, 3], 3), ([4, 5, 6, 7], 6)]
        synth = Synthesizer(self.grammar_sketch, specs, user_sketch="EXP")
        start = time.time()
        prog = synth.synthesize()
        end = time.time()
        if prog:
            with open("test_sketch_exception", "w") as f:
                f.write(prog.code)

        with open("summary.csv","a") as f:
            f.write(f"test_sketch_exception, {'SUCCESS' if prog is not None else 'FAILURE'}, {end-start}\n")


if __name__ == '__main__':
    unittest.main()