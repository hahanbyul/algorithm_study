from NTHLON import Nthlon
import random

def test_lin_comb():
   nthlon = Nthlon()
   # example 1
   nthlon.diff_plus = [4]
   nthlon.cost_plus = [7]

   nthlon.diff_minus = [1,1,1,1]
   nthlon.cost_minus = [1,3,5,7]

   print()
   print(f'answer: {nthlon.solve()}')

   # example 2
   nthlon.diff_minus = [1, 9]
   nthlon.cost_minus = [21,10]

   nthlon.diff_plus = [99]
   nthlon.cost_plus = [1]

   nthlon.diff_plus, nthlon.diff_minus = nthlon.diff_minus, nthlon.diff_plus
   nthlon.cost_plus, nthlon.cost_minus = nthlon.cost_minus, nthlon.cost_plus

   print()
   print(f'answer: {nthlon.solve()}')

def test_cache():
   nthlon = Nthlon()
   # example 3
   nthlon.diff_minus = [2]
   nthlon.cost_minus = [21]

   nthlon.diff_plus = [3]
   nthlon.cost_plus = [1]

   print()
   print(f'answer: {nthlon.solve()}')

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

def test_random_input():
   nthlon = Nthlon()
   M = random.randint(1, 500)
   A = [random.randint(1, 200) for _ in range(M)]
   B = [random.randint(1, 200) for _ in range(M)]
   nthlon.diff(A, B)
   print()
   nthlon.print_var()
   print(nthlon.solve())

"""
def test_all_same_input():
   nthlon = Nthlon()
   M = random.randint(1, 500)
   A = [random.randint(1, 200) for _ in range(M)]
   nthlon.diff(A, A)
   nthlon.print_var()
   print(nthlon.solve())

def test_all_input():
   nthlon = Nthlon()
   M = random.randint(1, 500)
   A = [200 for _ in range(M)]
   B = [1 for _ in range(M)]
   nthlon.diff(A, B)
   nthlon.print_var()
   print(nthlon.solve())
"""
