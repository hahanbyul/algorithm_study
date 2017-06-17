from NTHLON import Nthlon

def test_lin_comb():
   nthlon = Nthlon()
   nthlon.diff_plus = [1, 9]
   nthlon.cost_plus = [21,10]
   print()
   nthlon.lin_comb(50)

def test_get_answer():
   nthlon = Nthlon()
   print()
   nthlon.diff_minus = [1,6,1]
   nthlon.cost_minus = [134,31,10]
   nthlon.get_answer(2)
   print()
   nthlon.diff_minus = [1,1,1,1]
   nthlon.cost_minus = [1,3,5,7]
   answer = nthlon.get_answer(4)
   print(answer)



