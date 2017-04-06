import cProfile
import random
from RUNNINGMEDIAN import Heap

pr = cProfile.Profile()
pr.enable()

N, a, b = (10000, 1273, 4936)

h = Heap()
gen = h.generator(a, b)

part_sum = 0
for _ in range(N):
    h.put_inorder(gen.__next__())
    part_sum += h.get_median()
#print(part_sum % 20090711)

pr.disable()
pr.print_stats(sort='time')

pr = cProfile.Profile()
pr.enable()

f1.max_rect_fast()

pr.disable()
pr.print_stats(sort='time')
