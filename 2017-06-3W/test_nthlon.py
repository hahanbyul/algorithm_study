from NTHLON import Nthlon

def test_lin_comb():
   nthlon = Nthlon()
   # example 1
   nthlon.diff_plus = [4]
   nthlon.cost_plus = [7]

   nthlon.diff_minus = [1,1,1,1]
   nthlon.cost_minus = [1,3,5,7]

   print()
   print(f'answer: {nthlon.lin_comb(200)}')

   # example 2
   nthlon.diff_minus = [1, 9]
   nthlon.cost_minus = [21,10]

   nthlon.diff_plus = [99]
   nthlon.cost_plus = [1]

   nthlon.diff_plus, nthlon.diff_minus = nthlon.diff_minus, nthlon.diff_plus
   nthlon.cost_plus, nthlon.cost_minus = nthlon.cost_minus, nthlon.cost_plus

   print()
   print(f'answer: {nthlon.lin_comb(200)}')

def test_cache():
   nthlon = Nthlon()
   # example 3
   nthlon.diff_minus = [2]
   nthlon.cost_minus = [21]

   nthlon.diff_plus = [3]
   nthlon.cost_plus = [1]

   print()
   print(f'answer: {nthlon.lin_comb(200)}')

def test_get_answer():
   nthlon = Nthlon()
   print()
   nthlon.diff_minus = [1,6,1]
   nthlon.cost_minus = [134,31,10]
   nthlon.make_minus_graph()
   nthlon.get_answer(2)
   print()
   nthlon.diff_minus = [1,1,1,1]
   nthlon.cost_minus = [1,3,5,7]
   nthlon.make_minus_graph()
   answer = nthlon.get_answer(4)
   print(answer)



