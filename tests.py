import unittest
from synthesizer import  Synthesizer
import time




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