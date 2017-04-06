import cProfile
import random
from RUNNINGMEDIAN import Heap
from RUNNING_MEDIAN_FAST import Fast_median

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

fast_me = Fast_median()
gen = h.generator(a, b)

part_sum = 0
for _ in range(N):
    fast_me.put(gen.__next__())
    part_sum += fast_me.median

pr.disable()
pr.print_stats(sort='time')
